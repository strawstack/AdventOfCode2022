level = 0
def openFrom(valveRates, valveMatrix, nonZeroValves, timeLeft, curValve):
    global level
    #print("    " * level + f"cv: {curValve}, tl: {timeLeft}, r: {valveRates[curValve] * timeLeft}")

    if timeLeft == 0:
        return 0

    if len(nonZeroValves) == 0:
        return valveRates[curValve] * timeLeft

    bestRate = 0
    for otherValve in nonZeroValves:
        
        # Ensure there is enough time to visit valve
        if timeLeft - valveMatrix[curValve][otherValve] - 1 < 0:
            continue

        level += 1
        withOpen = openFrom(
            valveRates, valveMatrix, 
            list(filter(lambda x: x != otherValve, nonZeroValves)),  
            timeLeft - valveMatrix[curValve][otherValve] - 1, otherValve
        )
        level -= 1

        bestRate = max(bestRate, withOpen)
    
    return bestRate + valveRates[curValve] * timeLeft

def sol(lines):

    nodes = []
    for line in lines:
        valveFlowStr, tunnelsStr = line.split("; ")
        valveFlowList = valveFlowStr.split(" ")
        valveName = valveFlowList[1]
        valveRate = int(valveFlowStr.split(" ")[4].split("=")[1])
        tunnelsList = tunnelsStr.split(" ")[4:]
        tunnelsList = [x[:2] if len(x) == 3 else x for x in tunnelsList]

        nodes.append({
            "valveName": valveName,
            "valveRate": valveRate,
            "tunnels": tunnelsList  
        })

    valveMatrix = {x["valveName"]: {} for x in nodes}

    valveRates = {x["valveName"]: x["valveRate"] for x in nodes}

    # Every value points to every other valve
    for k in valveMatrix:
        for k1 in valveMatrix:
            if k != k1:
                valveMatrix[k][k1] = float("inf")

    # Edges of lenght 1
    for node in nodes:
        for otherNode in node["tunnels"]:
            valveMatrix[node["valveName"]][otherNode] = 1

    # F-W algo
    for k in valveMatrix:
        for k1 in valveMatrix:
            for k2 in valveMatrix:
                if k != k1 and k != k2 and k1 != k2:
                    dist = valveMatrix
                    newD = dist[k1][k] + dist[k][k2]
                    if newD < dist[k1][k2]:
                        dist[k1][k2] = newD

    nonZeroValves = [x["valveName"] if x["valveRate"] > 0 else None for x in nodes]
    nonZeroValves = list(filter(lambda x: x != None, nonZeroValves))

    # Try every route
    # Use culling to avoid timeout

    bestRate = 0
    for startValve in nonZeroValves:
        timeLeft = 30
        curRate = 0
        bestRate = max(bestRate, openFrom(
            valveRates, 
            valveMatrix, 
            list(filter(lambda x: x != startValve, nonZeroValves)), 
            timeLeft - valveMatrix["AA"][startValve] - 1,
            startValve))

    return bestRate

def main():
    
    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)