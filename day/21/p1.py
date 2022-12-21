def getNumber(mkys, code):
    job = mkys[code]

    if job["type"] == "number":
        return job["value"]
    
    else: # job["type"] == "op"
        left  = getNumber(mkys, job["left"])
        right = getNumber(mkys, job["right"])

        jobLookup = {
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "*": lambda left, right: left * right,
            "/": lambda left, right: left // right
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
                "right": job[2]
            }
        else:
            job = {
                "type": "number",
                "value": int(job[0])
            }
        
        mkys[code] = job

    return getNumber(mkys, "root")

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)