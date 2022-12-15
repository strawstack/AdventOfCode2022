# Note:
# grid is grid[x][y]
    # positive x is right
    # positive y is down

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def placeRock(grid, pos):
    grid[pos] = "#"

def addRock(grid, line):
    
    curPos = line[0]
    for i in range(1, len(line)):
        nx = line[i]

        delta = (
            nx[0] - curPos[0],
            nx[1] - curPos[1]
        )

        mag = max([abs(x) for x in delta])
        norm = (delta[0] / max(1, abs(delta[0])), delta[1] / max(1, abs(delta[1])))
        
        placeRock(grid, curPos)
        for j in range(mag):
            curPos = add(curPos, norm)
            placeRock(grid, curPos)

        curPos = nx

def getAbyssLevel(grid):
    lowest = 0
    for x, y in grid:
        lowest = max(lowest, y)
    return lowest

def getMaxx(grid):
    minx, maxx = float("inf"), 0
    for x, y in grid:
        minx = min(minx, x)
        maxx = max(maxx, x)
    return (minx, maxx)

def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

def shouldFall(grid, abyssLevel, floorLevel, curPos):
    
    down  = (0, 1)
    left  = (-1, 0)
    right = (1, 0) 

    downPos = add(curPos, down)
    if downPos[1] < floorLevel:
        if downPos not in grid:
            return downPos
        
        leftPos = add(downPos, left)
        if leftPos not in grid:
            return leftPos
        
        rightPos = add(downPos, right)
        if rightPos not in grid:
            return rightPos
    
    return False

def dropGrain(grid, abyssLevel, floorLevel, startPos):
    curPos = startPos
    while shouldFall(grid, abyssLevel, floorLevel, curPos) != False:
        nx = shouldFall(grid, abyssLevel, floorLevel, curPos)
        curPos = nx
    
    grid[curPos] = "O"
    if eq(curPos, (500, 0)):
        return False
    else:
        return True

def simulateSand(grid, abyssLevel, floorLevel, startPos):
    count = 0
    while dropGrain(grid, abyssLevel, floorLevel, startPos):
        count += 1
    return count + 1

def sol(lines):    
    lines = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in lines]

    for i in range(len(lines)):
        lines[i] = list(map(lambda x: (x[0], x[1]), lines[i]))

    grid = {}

    for line in lines:
        addRock(grid, line)
    
    abyssLevel = getAbyssLevel(grid)
    maxx = getMaxx(grid)
    floorLevel = 2 + abyssLevel

    #print(f"abyssLevel: {abyssLevel}")
    #print(f"maxx: {maxx}")

    grains = simulateSand(grid, abyssLevel, floorLevel, (500, 0))

    return grains

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)