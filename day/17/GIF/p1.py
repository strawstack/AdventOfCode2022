from gridsToGIF import gridsToGIF

# Note:
# grid is grid[x][y]
    # positive x is right
    # positive y is down

gridList = []

def getRocks():
    rocks = [
        [
            "####"
        ],
        [
            ".#.",
            "###",
            ".#."
        ],
        [
            "..#",
            "..#",
            "###"
        ],
        [
            "#",
            "#",
            "#",
            "#"
        ],
        [
            "##",
            "##"
        ]
    ]
    return rocks

def copyGrid(grid):
    newRock = {}
    for k in grid:
        newRock[k] = grid[k]
    return newRock

def copyRock(rock):
    newRock = {}
    for k in rock:
        newRock[k] = rock[k]
    return newRock

def makeRockDict(rockData, rIndex):
    
    yHeight = len(rockData)
    xWidth = len(rockData[0])

    points = {}

    for y in range(yHeight - 1, -1, -1):
        for x in range(xWidth):
            if rockData[y][x] == "#":
                points[(x, yHeight - y - 1)] = rIndex + 2

    return points

def inBounds(grid, rock):
    
    # Check walls and floor
    for k in rock:
        x, y = k
        if x <= 0:
            return False
        if x >= 8:
            return False
        if y <= 0:
            return False
    
    # Check other rocks
    for k in rock:
        if k in grid:
            return False
    
    return True

def moveRock(rock, delta):
    newRock = {}
    for k in rock:
        newRock[add(k, delta)] = rock[k]
    return newRock

def jetPush(grid, rock, jetDir):
    jetDirs = { ">": (1, 0), "<": (-1, 0) }
    delta = jetDirs[jetDir]
    newRock = moveRock(rock, delta)

    if inBounds(grid, newRock):
        return newRock
    else:
        return copyRock(rock)

def rockFall(grid, rock):
    delta = (0, -1) # down
    newRock = moveRock(rock, delta)

    if inBounds(grid, newRock):
        return newRock
    else:
        return copyRock(rock)

def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def setRockLocation(rock, botLeft):
    newRock = {}
    for k in rock:
        newRock[add(k, botLeft)] = rock[k]
    return newRock

def rockEqual(rock, oldRock):
    for k in oldRock:
        if k not in rock:
            return False
    return True

def getHighest(highestPoint, rock):
    for k in rock:
        x, y = k
        highestPoint = max(highestPoint, y)
    return highestPoint

def addRockToGrid(grid, rock):
    for k in rock:
        grid[k] = rock[k]

def flipY(height, grid):
    newGrid = {}
    for k in grid:
        x, y = k
        newGrid[(x, height - y)] = grid[k]
    return newGrid

def filterGrid(height, grid):
    newGrid = {}
    for k in grid:
        x, y = k
        if y < height:
            newGrid[k] = grid[k]
    return newGrid

def addWalls(height, width, grid):
    newGrid = {}
    for k in grid:
        newGrid[k] = grid[k]
    
    for h in range(height):
        newGrid[(0, h)] = 1
        newGrid[(8, h)] = 1

    #for w in range(width):
    #    newGrid[(w, height - 1)] = 1
    
    return newGrid

def captureGrid(grid, rock):
    global gridList
    newGrid = copyGrid(grid)
    for k in rock:
        newGrid[k] = rock[k]
    
    newGrid = filterGrid(50, newGrid)
    newGrid = flipY(50, newGrid)
    newGrid = addWalls(50, 9, newGrid)
    gridList.append(newGrid)

def dropRock(grid, highestPoint, jetData, rock):
    (jet, jIndex) = jetData
    
    botLeft = (3, highestPoint + 4)
    rock = setRockLocation(rock, botLeft)

    while True:
        # push
        rock = jetPush(grid, rock, jet[jIndex])
        jIndex = (jIndex + 1) % len(jet)

        captureGrid(grid, rock)

        # fall
        oldRock = copyRock(rock)
        rock = rockFall(grid, rock)

        captureGrid(grid, rock)
        
        # exit if rock has landed
        if rockEqual(rock, oldRock):
            addRockToGrid(grid, rock)
            highestPoint = getHighest(highestPoint, rock)
            return jIndex, highestPoint

# grid
# Positive y is up
# Positive x is right
# Floor is x = 0 (x axis)

def sol(jet):
    global gridList
    
    grid = {}
    jIndex = 0
    rIndex = 0
    rocks = getRocks()

    rockCount = 0
    highestPoint = 0
    while rockCount < 31:
        
        rd = makeRockDict(rocks[rIndex], rIndex)
        jIndex, highPoint = dropRock(grid, highestPoint, (jet, jIndex), rd)
        
        highestPoint = max(highestPoint, highPoint)
        rIndex = (rIndex + 1) % len(rocks)
        rockCount += 1
    
    options = {
        "COLORS": [
            (22, 22, 22),
            (255, 255, 255),
            (163, 217, 255),
            (126, 107, 143),
            (150, 230, 179),
            (218, 62, 82),
            (242, 233, 78),
            (0, 0, 0)
        ],
        "DELAY": 5
    }

    gridsToGIF("AOC_DAY_17_P1", 50, 9, 16, gridList, options)

    return highestPoint

def main():
    
    lines = open("../input.txt").read().strip()
    #lines = open("test_input.txt").read().strip()
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)