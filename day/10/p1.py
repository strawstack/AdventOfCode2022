def parseCmd(line):
    if " " in line:
        v = line.split(" ")
        return {
            "name": v[0],
            "value": int(v[1]),
            "cycles": 2
        }
    else:
        return {
            "name": line,
            "value": None,
            "cycles": 1
        }

def processCmd(cmd):
    if cmd["name"] == "noop":
        return 0

    elif cmd["name"] == "addx":
        return cmd["value"]

def checkCycle(current_cycle):
    return current_cycle in [20, 60, 100, 140, 180, 220]

def sol(lines):
    cmds = [parseCmd(x) for x in lines]
    
    x = 1
    current_cycle = 1
    total_strength = 0

    for cmd in cmds:
        
        for cycle in range(cmd["cycles"]):
            current_cycle += 1

            if cycle == cmd["cycles"] - 1:
                x += processCmd(cmd)

            if checkCycle(current_cycle):
                strength = current_cycle * x
                total_strength += strength

        if current_cycle > 220:
            return total_strength

    return total_strength

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    #lines = [x[:-1] for x in open("input_test.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)