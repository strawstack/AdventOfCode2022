def getInputNum(mkys, targetValue, code, level):
    job = mkys[code]

    if code == "humn":
        return targetValue

    elif job["type"] == "op":
        leftJob  = mkys[job["left"]]["input_path"]
        inputCode, otherCode = ("left", "right") if leftJob else ("right", "left")

        otherValue = getNumber(mkys, job[otherCode])

        newTargetValue = None
        if job["op"] == "-":
            if leftJob:
                newTargetValue = targetValue + otherValue
            else:
                newTargetValue = otherValue - targetValue

        elif job["op"] == "/": 
            if leftJob:
                newTargetValue = targetValue * otherValue
            else:
                newTargetValue = otherValue * targetValue

        else:
            jobLookup = {
                "+": lambda tv, ov: tv - ov,
                "*": lambda tv, ov: tv // ov
            }         
            newTargetValue = jobLookup[job["op"]](targetValue, otherValue)
        
        ans = getInputNum(mkys, newTargetValue, job[inputCode], level + 1)
        return ans

def getRoot(mkys, code):
    job = mkys[code]

    if code == "humn":
        job["input_path"] = True
        return "INPUT_NUM"

    if job["type"] == "number":
        job["input_path"] = False
        return str(job["value"])
    
    else: # job["type"] == "op"
        left  = getRoot(mkys, job["left"])
        right = getRoot(mkys, job["right"])

        leftJob  = mkys[job["left"]]["input_path"]
        rightJob = mkys[job["right"]]["input_path"]

        job["input_path"] = leftJob or rightJob

        jobLookup = {
            "+": lambda left, right: f"{left} + {right}",
            "-": lambda left, right: f"{left} - {right}",
            "*": lambda left, right: f"{left} * {right}",
            "/": lambda left, right: f"{left} / {right}",
            "=": lambda left, right: f"{left} == {right}"
        }

        result = jobLookup[job["op"]](left, right)
        return result

def getNumber(mkys, code, humnVal=None):
    job = mkys[code]

    if code == "humn" and humnVal != None:
        return humnVal

    elif job["type"] == "number":
        return job["value"]
    
    else: # job["type"] == "op"
        left  = getNumber(mkys, job["left"])
        right = getNumber(mkys, job["right"])

        jobLookup = {
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "*": lambda left, right: left * right,
            "/": lambda left, right: left // right,
            "=": lambda left, right: left == right
        }

        result = jobLookup[job["op"]](left, right)
        return result

def sol(lines):

    mkys = {}

    for line in lines:
        code, jobStr = line.split(": ")
        job = jobStr.split(" ")

        if len(job) == 3:
            job = {
                "type": "op",
                "left": job[0],
                "op": job[1],
                "right": job[2],
                "input_path": False
            }
        else:
            job = {
                "type": "number",
                "value": int(job[0]),
                "input_path": False
            }
        
        mkys[code] = job

    mkys["root"]["op"] = "="
    
    targetValue = None
    subTreeCode = None

    root = getRoot(mkys, "root")
    root = root.split("==")
    LEFT, RIGHT = 0, 1
    if "INPUT_NUM" in root[LEFT]:
        subTreeCode = mkys["root"]["left"]
        targetValue = getNumber(mkys, mkys["root"]["right"])
    else:
        subTreeCode = mkys["root"]["right"]
        targetValue = getNumber(mkys, mkys["root"]["left"])

    inputNum = getInputNum(mkys, targetValue, subTreeCode, 0) 

    return inputNum

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)