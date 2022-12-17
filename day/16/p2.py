level = 0
def openFrom(valveRates, valveMatrix, nonZeroValves, mTimeLeft, eTimeLeft, mNext, eNext, mValve, eValve):
    global level

    mTime = float("-inf") if mNext == float("-inf") else mTimeLeft - mNext 
    eTime = float("-inf") if eNext == float("-inf") else eTimeLeft - eNext

    if mNext == float("-inf") and eNext == float("-inf"):
        return 0

    if False:
        if mTime > eTime:
            mt = mTimeLeft - mNext
            print("    " * level + f"cv(m): {mValve}, tl: {mt}, r: {valveRates[mValve] * (mt)}")
        else:
            et = eTimeLeft - eNext
            print("    " * level + f"cv(e): {eValve}, tl: {et}, r: {valveRates[eValve] * (et)}")

    bestRate = 0
    if mTime > eTime:

        mTimeLeft -= mNext

        flag = False
        for otherValve in nonZeroValves:
        
            if mTimeLeft <= valveMatrix[mValve][otherValve] + 1:
                continue
            
            flag = True
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                list(filter(lambda x: x != otherValve, nonZeroValves)),  
                mTimeLeft, eTimeLeft, 
                valveMatrix[mValve][otherValve] + 1, eNext,
                otherValve, eValve
            )
            level -= 1

            bestRate = max(bestRate, rate)

        if len(nonZeroValves) == 0 or not flag:
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                nonZeroValves,  
                None, eTimeLeft, 
                float("-inf"), eNext,
                None, eValve
            )
            level -= 1

            bestRate = max(bestRate, rate)

        return bestRate + (valveRates[mValve] * mTimeLeft if mTimeLeft > 0 else 0)
    
    elif mTime < eTime:

        eTimeLeft -= eNext
        
        flag = False
        for otherValve in nonZeroValves:
        
            if eTimeLeft <= valveMatrix[eValve][otherValve] + 1:
                continue
            flag = True
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                list(filter(lambda x: x != otherValve, nonZeroValves)),  
                mTimeLeft, eTimeLeft, 
                mNext, valveMatrix[eValve][otherValve] + 1,
                mValve, otherValve
            )
            level -= 1

            bestRate = max(bestRate, rate)

        if len(nonZeroValves) == 0 or not flag:
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                nonZeroValves,  
                mTimeLeft, None, 
                mNext, float("-inf"),
                mValve, None
            )
            level -= 1

            bestRate = max(bestRate, rate)

        return bestRate + (valveRates[eValve] * eTimeLeft if eTimeLeft > 0 else 0)
    
    else: # mTime == eTime

        mTimeLeft -= mNext
        mRate = 0
        flag = False
        for otherValve in nonZeroValves:
        
            if mTimeLeft <= valveMatrix[mValve][otherValve] + 1:
                continue
            flag = True
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                list(filter(lambda x: x != otherValve, nonZeroValves)),  
                mTimeLeft, eTimeLeft, 
                valveMatrix[mValve][otherValve] + 1, eNext,
                otherValve, eValve
            )
            level -= 1

            mRate = max(mRate, rate)

        if len(nonZeroValves) == 0 or not flag:
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                nonZeroValves,  
                None, eTimeLeft, 
                float("-inf"), eNext,
                None, eValve
            )
            level -= 1

            mRate = max(mRate, rate)

        eTimeLeft -= eNext
        eRate = 0
        flag = False
        for otherValve in nonZeroValves:
        
            if eTimeLeft <= valveMatrix[eValve][otherValve] + 1:
                continue
            flag = True
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                list(filter(lambda x: x != otherValve, nonZeroValves)),  
                mTimeLeft, eTimeLeft, 
                mNext, valveMatrix[eValve][otherValve] + 1,
                mValve, otherValve
            )
            level -= 1

            eRate = max(eRate, rate)

        if len(nonZeroValves) == 0 or not flag:
            level += 1
            rate = openFrom(
                valveRates, valveMatrix, 
                nonZeroValves,  
                mTimeLeft, None, 
                mNext, float("-inf"),
                mValve, None
            )
            level -= 1

            eRate = max(eRate, rate)
        
        if mRate > eRate:
            return mRate + (valveRates[mValve] * mTimeLeft if mTimeLeft > 0 else 0)
        else:
            return eRate + (valveRates[eValve] * eTimeLeft if eTimeLeft > 0 else 0)

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
    for mValve in nonZeroValves:
        for eValve in nonZeroValves:
            if mValve == eValve:
                continue
            mTimeLeft, eTimeLeft = 26, 26
            mNext = valveMatrix["AA"][mValve] + 1
            eNext = valveMatrix["AA"][eValve] + 1
            bestRate = max(bestRate, openFrom(
                valveRates, 
                valveMatrix, 
                list(filter(lambda x: x != mValve and x != eValve, nonZeroValves)), 
                mTimeLeft, eTimeLeft,
                mNext, eNext,
                mValve, eValve))

    return bestRate

def main():
    
    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 2504 - too low