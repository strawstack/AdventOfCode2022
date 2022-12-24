import math
import heapq
import json

D = False

def loads(state):
    return json.loads(state)

def dumps(state):
    return json.dumps(state)

def copyState(state):
    newState = {}
    for k in state:
        newState[k] = state[k]
    return newState

def buildBot(blueprint, dState, botKey, limit, q):
    state = loads(dState)

    # Number of bots that you have is more than
    # what you would need in one turn
    if limit[botKey] <= state[botKey] and not botKey == "geoBot":
        return None

    # How long do we have to wait to have resources to
    # build botKey
    botCost = blueprint[botKey]

    if D: print(f"  buildBot: {botKey}")
    if D:
        for k in botCost:
            print(f"    {k}: {botCost[k]}")

    collectTime = 0
    for oreKey in botCost:
        numBots = state[f"{oreKey}Bot"]
        if numBots > 0:
            reqOre = botCost[oreKey] - state[oreKey]
            if reqOre <= 0:
                timeToCollect = 0
            else:
                timeToCollect = math.ceil(reqOre / numBots)
            collectTime = max(collectTime, timeToCollect)
        else:
            return None

    if D: print(f"    collectTime: {collectTime}")

    buildTime = 1
    if collectTime + buildTime <= state["time"]:

        # Remove time
        state["time"] -= collectTime

        # Add mining results
        for oreKey in ["ore", "clay", "obs", "geo"]:
            state[oreKey] += collectTime * state[f"{oreKey}Bot"]

        # Charge cost
        for oreKey in botCost:
            cost = botCost[oreKey]
            state[oreKey] -= cost

        # Time to build bot
        state["time"] -= buildTime

        # One min mine during purchase
        for oreKey in ["ore", "clay", "obs", "geo"]:
            state[oreKey] += state[f"{oreKey}Bot"]

        # Grant bot
        state[botKey] += 1

        # Add state to heap
        heapq.heappush(q, (state["geo"], dumps(state)))
        while len(q) > 300000:
            q.pop()

    return None

def getMaxPossible(dState):
    state = loads(dState)
    geos = state["geo"]
    for i in range(state["time"]):
        geos += state["geoBot"]
        state["geoBot"] += 1
    return geos

# Tries all possible branches from a given state
# and reports back the best geo outcome
def tryAll(blueprint, limit, initState):

    if D: print(f"tryAll called")

    q = [] # heap
    heapq.heappush(q, (initState["geo"], dumps(initState)))

    bestGeo = 0
    while len(q) > 0:
        state = loads(heapq.heappop(q)[1])

        if D:
            for k in state:
                print(f"{k}: {state[k]}")

        geo = state["geoBot"] * state["time"] + state["geo"]
        bestGeo = max(bestGeo, geo)

        maxPossible = getMaxPossible(dumps(state))

        if bestGeo < maxPossible:

            if D: print(f"geoScore: {geo}")

            if state["time"] > 3:
                for botKey in ["oreBot", "clayBot", "obsBot", "geoBot"]:
                    buildBot(blueprint, dumps(state), botKey, limit, q)

            elif state["time"] == 3:
                for botKey in ["oreBot", "obsBot", "geoBot"]:
                    buildBot(blueprint, dumps(state), botKey, limit, q)

            elif state["time"] == 2:
                buildBot(blueprint, dumps(state), "geoBot", limit, q)

    return bestGeo

# Get the limit for amount of each resource
def getLimits(blueprint):
    limits = {
        "oreBot":  0,
        "clayBot": 0,
        "obsBot":  0,
        "geoBot":  0
    }
    for botKey in blueprint:
        for oreKey in blueprint[botKey]:
            value = blueprint[botKey][oreKey]
            if limits[f"{oreKey}Bot"] < value:
                limits[f"{oreKey}Bot"] = value
    return limits

# Get the max geo that this blueprint can create
def getMaxGeos(blueprint):

    #limit = getLimits(blueprint)

    state = {
        "time": 32,
        "ore":  0,
        "clay": 0,
        "obs":  0,
        "geo":  0,
        "oreBot":  1,
        "clayBot": 0,
        "obsBot":  0,
        "geoBot":  0
    }

    limit = getLimits(blueprint)

    geos = tryAll(blueprint, limit, state)

    return geos

def sol(lines):
    lines = [
        [y.split(" ")
        for y in x.split(": ")[1].split(". ")]
        for x in lines.split("\n")]

    blueprints = []
    for line in lines:
        oreBotCost  = {line[0][-1]: int(line[0][-2])}
        clayBotCost = {line[1][-1]: int(line[1][-2])}
        obsBotCost  = {
            line[2][-4]: int(line[2][-5]),
            line[2][-1]: int(line[2][-2]),
        }
        geoBotCost  = {
            line[3][-4]: int(line[3][-5]),
            line[3][-1][:-6]: int(line[3][-2])
        }

        blueprints.append(
            {
                "oreBot": oreBotCost,
                "clayBot": clayBotCost,
                "obsBot": obsBotCost,
                "geoBot": geoBotCost
            }
        )

    total = 1
    for i in range(3):

        # These return zero as far as I can tell
        #if (i + 1) in [1, 3, 4, 9, 11, 12, 13, 14, 15, 17, 28, 30]:
        #    continue

        blueprint = blueprints[i]
        geos = getMaxGeos(blueprint)
        print(f"{i + 1}: {geos}")
        total *= geos

    return total

def main():

    #lines = open("test_input.txt").read().strip()
    lines = open("input.txt").read().strip()

    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 106  - too low
# 2226 - too high
# 258  - wrong
# 881  - wrong
# 1354 - wrong
# 1368 - wrong
