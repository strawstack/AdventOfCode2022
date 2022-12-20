def copyState(state):
    newState = {}
    for k in state:
        newState[k] = state[k]
    return newState

def execMine(state):
    state = copyState(state)
    for t in ["ore", "clay", "obs", "geo"]:
        state[t] += state[f"{t}Bot"] 
    return state

def canMake(state, bot):
    blueprint = state["bp"][bot]
    
    if state[f"{bot}Limit"] <= state[bot]:
        return False
    
    for k in blueprint:
        reqNumber = blueprint[k]
        if state[k] < reqNumber:
            return False
    
    return True

def purchaseBot(state, bot):
    state = copyState(state)
    blueprint = state["bp"][bot]
    for k in blueprint:
        state[k] -= blueprint[k]
    return state

def printState(state):
    lst = [] 
    bots = ["ore", "clay", "obs", "geo"]
    for b in bots:
        lst.append(str(state[f"{b}Bot"]))

    lst.append(",")

    for b in bots:
        lst.append(str(state[b]))
    
    print(" ".join(lst))

def checkState(state, oreBot, clayBot, obsBot, geoBot,  ore, clay, obs, geo):

    one = state["oreBot"] == oreBot
    two = state["clayBot"] == clayBot
    three = state["obsBot"] == obsBot
    four = state["geoBot"] == geoBot

    five = state["ore"] == ore
    six = state["clay"] == clay
    seven = state["obs"] == obs
    eight = state["geo"] == geo

    return one and two and three and four and five and six and seven and eight

def canMine(state):
    lst = ["ore", "clay", "obs"]
    for item in lst:
        holdLess = state[item] < state[f"{item}Limit"]
        haveBots = state[f"{item}Bot"] > 0
        if holdLess and haveBots:
            return True
    return False

def tryAll(state):

    printState(state)

    if True:
        debug = False
        if checkState(state, 1, 3, 0, 0,  2, 9, 0, 0):
            debug = True
            printState(state)

    state = copyState(state)
    state["time"] -= 1 # Use one min to mine and make a bot if you can

    # Return if no time left
    if state["time"] == 0:
        state = execMine(state)
        return state["geo"]

    # Actions (what bot do you want to build with the factory?)
    bestReturn = 0
    flag = True
    for bot in ["oreBot", "clayBot", "obsBot", "geoBot"]:

        if canMake(state, bot):

            if debug:
                print(f"Make {bot}")

            flag = False
            cState = purchaseBot(state, bot)
            cState = execMine(cState)
            cState[bot] += 1
            
            bestReturn = max(
                bestReturn,
                tryAll(cState)
            )
    
    # Try not building a bot this round
    if canMine(state):

        if debug:
            print("Can mine")

        state = execMine(state)
        bestReturn = max(
            bestReturn,
            tryAll(state)
        )
    
    return bestReturn

def getMax(blueprint, mType):
    mNum = 0
    for k in blueprint:
        for kk in blueprint[k]:
            if kk == mType:
                mNum = max(mNum, blueprint[k][kk])
    return mNum + 1

def getQualityLevel(blueprint):
    state = {
        "bp": blueprint,
        "time": 24,

        "oreBot": 1,
        "clayBot": 0,
        "obsBot": 0,
        "geoBot": 0,

        "ore": 0,
        "clay": 0,
        "obs": 0,
        "geo": 0,

        "oreBotLimit": getMax(blueprint, "ore"),
        "clayBotLimit": getMax(blueprint, "clay"),
        "obsBotLimit": getMax(blueprint, "obs"),
        "geoBotLimit": float("inf"),

        "oreLimit": getMax(blueprint, "ore"),
        "clayLimit": getMax(blueprint, "clay"),
        "obsLimit": getMax(blueprint, "obs"),
        "geoLimit": float("inf")
    }
    rtn = tryAll(state)
    return rtn

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

    total = 0
    for i in range(len(blueprints)):
        blueprint = blueprints[i]
        ql = (i + 1) * getQualityLevel(blueprint)
        return ql
        total += ql

    return total

def main():
    
    #lines = open("input.txt").read().strip()
    lines = open("test_input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
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