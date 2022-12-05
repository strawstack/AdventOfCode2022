def sol(lines):
    rawStackData, lines = lines.split("\n\n")
    rows = [x for x in rawStackData.split("\n")]
    cols = list(zip(*rows))
    cols = list(filter(lambda x: x[-1] in "123456789", cols))

    stacks = {}
    for rawStack in cols:
        rawStack = list(reversed(rawStack))
        number, items = int(rawStack[0]), rawStack[1:]
        stack = []
        for item in items:
            if item == " ":
                break
            stack.append(item)
        stacks[number] = stack

    data = []
    for line in lines.split("\n"):
        lineSplit = line.split(" ")
        grab = (int(lineSplit[1]), int(lineSplit[3]), int(lineSplit[5]))
        data.append(grab)

    # move items
    for move, fromStack, toStack in data:
        
        out = []
        for m in range(move):
            out.append(stacks[fromStack].pop())
        
        for item in out:
            stacks[toStack].append(item)

    ans = [""] * 10
    for k in stacks:
        ans[int(k)] = stacks[k][-1]

    return "".join(ans)

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)