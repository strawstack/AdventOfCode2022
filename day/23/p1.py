def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def copyElves(elves):
    newElves = {}
    for k in elves:
        newElves[k] = elves[k]
    return newElves

def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

def nothingAround(elves, elf):
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            targetPos = add(elf, (dr, dc))
            if eq(elf, targetPos):
                continue
            if targetPos in elves:
                return False
    return True

def moveElves(elves, startIndex):
    
    dirs = [
        {
            "dirCheck": [(-1, -1), (-1, 0), (-1, 1)], # North
            "move": (-1, 0)
        },
        {
            "dirCheck": [(1, -1), (1, 0), (1, 1)], # South
            "move": (1, 0)
        },
        {
            "dirCheck": [(-1, -1), (0, -1), (1, -1)], # West
            "move": (0, -1)
        },
        {
            "dirCheck": [(-1, 1), (0, 1), (1, 1)], # East
            "move": (0, 1)
        }
    ]

    # {key: value} -> {elfPos: targetPos}
    considerMoving = {}
    
    # {targetPos: count}
    targetTrack = {}

    elves = copyElves(elves)

    # For every elf...
    for elf in elves:

        if nothingAround(elves, elf):
            continue

        #print(f"Elf: {elf}")

        # For each dir to consider... 
        dIndex = startIndex
        for d in range(len(dirs)):

            d = dirs[dIndex]
            dIndex = (dIndex + 1) % 4

            #print(f"  Consider: {dIndex}")

            # For each of the three check cells...
            elfFound = False
            for delta in d["dirCheck"]:

                # Track if an elf is found
                checkCell = add(elf, delta)
                if checkCell in elves:
                    elfFound = True
            
            #print(f"  Found: {elfFound}")

            # If all three are free, target the cell and track the decision
            if not elfFound:
                targetCell = add(elf, d["move"])
                considerMoving[elf] = targetCell
                if targetCell not in targetTrack: 
                    targetTrack[targetCell] = 0
                targetTrack[targetCell] += 1
                break
    
    newElves = {}
    for elf in elves:

        #print(f"  Elf moving: {elf}")

        # Elf decide to move
        if elf in considerMoving:
            
            targetCell = considerMoving[elf]

            # Elf movement success
            if targetTrack[targetCell] <= 1:
                #print(f"  Elf moves: {targetCell}")
                newElves[targetCell] = True

            # Elf decide to move but there is a conflict
            else:
                #print(f"  Elf stays: {elf}")
                newElves[elf] = True
        
        # Elf decide not to move
        else:
            #print(f"  Elf stays: {elf}")
            newElves[elf] = True
    
    return newElves

def renderElves(ROWS, COLS, elves):
    #for r in range(-1 * ROWS//2, ROWS):
    #    for c in range(-1 * COLS//2, COLS):
    for r in range(ROWS):
        for c in range(COLS):    
            if (r, c) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

def sol(grid):
    
    elves = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            value = grid[r][c]
            if value == "#":
                elves[(r, c)] = True
    
    roundCount = 0
    startIndex = 0
    while roundCount < 10:

        elves = moveElves(elves, startIndex)

        #renderElves(6, 5, elves)

        startIndex = (startIndex + 1) % 4
        roundCount += 1

    minRow = float("inf")
    maxRow = 0
    minCol = float("inf")
    maxCol = 0
    for (r, c) in elves:
        minRow = min(minRow, r)
        maxRow = max(maxRow, r)
        minCol = min(minCol, c)
        maxCol = max(maxCol, c)

    colWidth = maxCol - minCol + 1
    rowHeight = maxRow - minRow + 1

    ans = colWidth * rowHeight - len(elves)

    return ans

def main():
    
    #lines = [x[:-1] for x in open("small_test_input.txt").readlines()]
    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 4033 - wrong