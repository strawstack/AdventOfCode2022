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

def copyRock(rock):
    newRock = {}
    for k in rock:
        newRock[k] = True
    return newRock

def makeRockDict(rockData):
    
    yHeight = len(rockData)
    xWidth = len(rockData[0])

    points = {}

    for y in range(yHeight - 1, -1, -1):
        for x in range(xWidth):
            if rockData[y][x] == "#":
                points[(x, yHeight - y - 1)] = True

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
        newRock[add(k, delta)] = True
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
        newRock[add(k, botLeft)] = True
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
        grid[k] = True

def dropRock(grid, highestPoint, jetData, rock):
    (jet, jIndex) = jetData
    
    botLeft = (3, highestPoint + 4)
    rock = setRockLocation(rock, botLeft)

    while True:
        # push
        rock = jetPush(grid, rock, jet[jIndex])
        jIndex = (jIndex + 1) % len(jet)

        # fall
        oldRock = copyRock(rock)
        rock = rockFall(grid, rock)
        
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
    
    grid = {}
    jIndex = 0
    rIndex = 0
    rocks = getRocks()

    rockCount = 0
    highestPoint = 0
    while rockCount < 2022:
        
        rd = makeRockDict(rocks[rIndex])
        jIndex, highPoint = dropRock(grid, highestPoint, (jet, jIndex), rd)
        
        highestPoint = max(highestPoint, highPoint)
        rIndex = (rIndex + 1) % len(rocks)
        rockCount += 1
        
    return highestPoint

def main():
    
    lines = open("input.txt").read().strip()
    #lines = open("test_input.txt").read().strip()
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)