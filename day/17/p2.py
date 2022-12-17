import math

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

def trimGrid(grid, highestPoint):
    delete = []
    count = 0
    for k in grid:
        x, y = k
        if y < highestPoint - 100:
            delete.append((x, y))
            count += 1
        if count > 1700:
            break
    
    for d in delete:
        del grid[d]

def dropRock(grid, jetData, rock):
    (jet, jIndex) = jetData
    highestPoint = 0
    
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
            if len(grid) > 2000:
                trimGrid(grid, highestPoint)
            return jIndex, highestPoint

def rockHeight(index):
    lst = [1, 3, 3, 4, 2]
    return lst[index]

# grid
# Positive y is up
# Positive x is right
# Floor is x = 0 (x axis)

DROP_COUNT = 2022

def sol(jet):
    
    jSize = len(jet)

    grid = {}
    jIndex = 0
    rIndex = 0
    rocks = getRocks()

    rockCount = 0
    highestPoint = 0

    pattern = [] # debug

    heightsAfterRoll = []
    rockCountRoll = []
    heightLookup = {}
    while rockCount < 3 * jSize:
    
        if len(heightsAfterRoll) == 3 and len(rockCountRoll) == 3:
            rocksPerHeight = rockCountRoll[-1] - rockCountRoll[-2]
            numberRocks = rockCount - rockCountRoll[2]
            heightLookup[numberRocks] = highestPoint - heightsAfterRoll[2]

        rd = makeRockDict(rocks[rIndex])
        botLeft = (3, highestPoint + 4)
        rock = setRockLocation(rd, botLeft)

        old_jIndex = jIndex
        jIndex, highPoint = dropRock(grid, (jet, jIndex), rock)
        
        highestPoint = max(highestPoint, highPoint)
        
        if jIndex < old_jIndex:
            rockCountRoll.append(rockCount)
            heightsAfterRoll.append(highestPoint)

        rIndex = (rIndex + 1) % len(rocks)
        rockCount += 1

    BIG_NUM = 1000000000000

    heightIncrease = heightsAfterRoll[-1] - heightsAfterRoll[-2]
    rocksPerHeight = rockCountRoll[-1] - rockCountRoll[-2]

    totalRocks = rockCountRoll[0]
    totalHeight = heightsAfterRoll[0]

    totalHeight += heightIncrease * ((BIG_NUM - totalRocks) // rocksPerHeight) 

    rocksLeft = (BIG_NUM - totalRocks) % rocksPerHeight

    return totalHeight + heightLookup[rocksLeft]

def main():
    
    lines = open("input.txt").read().strip()
    #lines = open("test_input.txt").read().strip()
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)