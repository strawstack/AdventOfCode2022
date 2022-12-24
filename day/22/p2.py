def getTopLeft(grid):
    minCol = float("inf")
    for row, col in grid:
        if row == 0:
            minCol = min(minCol, col)
    return 0, minCol

def add(curPos, delta):
    return (curPos[0] + delta[0], curPos[1] + delta[1])

def getBaseCoord(faceNumb):
    faceLookup = {
        1: (0, 1),
        2: (0, 2),
        3: (1, 1),
        4: (2, 0),
        5: (2, 1),
        6: (3, 0)
    }
    return faceLookup[faceNumb]

def getFace(curPos):
    r, c = curPos
    faceLookup = {
        (0, 1): 1,
        (0, 2): 2,
        (1, 1): 3,
        (2, 0): 4,
        (2, 1): 5,
        (3, 0): 6
    }
    return faceLookup[(r // 50, c // 50)]

def getNextFace(curFace, facing):
    faceLookup = {
        (1, 0): 6,
        (1, 1): 2,
        (1, 2): 3,
        (1, 3): 4,

        (2, 0): 6,
        (2, 1): 5,
        (2, 2): 3,
        (2, 3): 1,

        (3, 0): 1,
        (3, 1): 2,
        (3, 2): 5,
        (3, 3): 4,

        (4, 0): 3,
        (4, 1): 5,
        (4, 2): 6,
        (4, 3): 1,

        (5, 0): 3,
        (5, 1): 2,
        (5, 2): 6,
        (5, 3): 4,

        (6, 0): 4,
        (6, 1): 5,
        (6, 2): 2,
        (6, 3): 1
    }
    return faceLookup[(curFace, facing)]

#  12 
#  3
# 45
# 6
def transformCoord(curFace, nextFace, curPos):
    lookup = {
        (1, 6): lambda cp: ((cp[1], 0), 1),
        (1, 2): lambda cp: ((cp[0], 0), 1),
        (1, 3): lambda cp: ((0, cp[1]), 2),
        (1, 4): lambda cp: ((49 - cp[0], 0), 1),

        (2, 6): lambda cp: ((49, cp[1]), 0),
        (2, 5): lambda cp: ((49 - cp[0], 49), 3),
        (2, 3): lambda cp: ((cp[1], 49), 3),
        (2, 1): lambda cp: ((cp[0], 49), 3),
        
        (3, 1): lambda cp: ((49, cp[1]), 0),
        (3, 2): lambda cp: ((49, cp[0]), 0),
        (3, 5): lambda cp: ((0, cp[1]), 2),
        (3, 4): lambda cp: ((0, cp[0]), 2),

        (4, 3): lambda cp: ((cp[1], 0), 1),
        (4, 5): lambda cp: ((cp[0], 0), 1),
        (4, 6): lambda cp: ((0, cp[1]), 2),
        (4, 1): lambda cp: ((49 - cp[0], 0), 1),
        
        (5, 3): lambda cp: ((49, cp[1]), 0),
        (5, 2): lambda cp: ((49 - cp[0], 49), 3),
        (5, 6): lambda cp: ((cp[1], 49), 3),
        (5, 4): lambda cp: ((cp[0], 49), 3),
        
        (6, 4): lambda cp: ((49, cp[1]), 0),
        (6, 5): lambda cp: ((49, cp[0]), 0),
        (6, 2): lambda cp: ((0, cp[1]), 2),
        (6, 1): lambda cp: ((0, cp[0]), 2)
    }

    baseRow, baseCol = ((curPos[0] // 50) * 50, (curPos[1] // 50) * 50)
    relativePos = (curPos[0] - baseRow, curPos[1] - baseCol)

    newRelativePos, newFacing = lookup[(curFace, nextFace)](relativePos)

    bc = getBaseCoord(nextFace)
    newPos = add(
        newRelativePos,
        (bc[0] * 50, bc[1] * 50)
    )

    if False: # debug
        print(f"{curFace} to {nextFace}")
        print(f"curPos: {curPos}")
        print(f"baseRow, baseCol: {baseRow}, {baseCol}")
        print(f"relativePos: {relativePos}")
        print(f"newRelativePos: {newRelativePos}")
        print(f"newPos: {newPos}")
        print("")

    return newPos, newFacing

def getOppositeTile(grid, curPos, facing):
    curFace  = getFace(curPos)
    nextFace = getNextFace(curFace, facing)
    newPos, facing = transformCoord(curFace, nextFace, curPos)
    return newPos, facing

# One step in direction facing
# Unless you hit a wall
def move(grid, curPos, facing, debug=False):

    deltaLookup = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    newPos = add(curPos, deltaLookup[facing])

    if newPos not in grid:
        oPos, newFacing = getOppositeTile(grid, curPos, facing)

        if grid[oPos] == "#" and not debug:
            return curPos, facing
        
        else: # grid[(oRow, oCol)] == "."
            return oPos, newFacing

    elif grid[newPos] == "#" and not debug:
        return curPos, facing
    
    elif grid[newPos] == "." or debug:
        return newPos, facing
    
    else:
        raise Exception("Unknown grid tile.")

def turn(facing, direction):
    if direction == "R":
        facing = (facing + 1) % 4

    elif direction == "L":
        facing = (facing - 1) % 4
    
    else:
        raise Exception("Unknown turn direction.")
    
    return facing

def doCommand(grid, cmd, curPos, facing):
    
    if cmd["type"] == "number":
        for i in range(cmd["value"]):

            prevPos = curPos
            curPos, facing = move(grid, prevPos, facing)

            # We hit a wall
            if prevPos == curPos:
                break

    elif cmd["type"] == "turn":
        facing = turn(facing, cmd["value"])
    
    else:
        raise Exception("Unknown command.")
    
    return curPos, facing

def followPath(grid, path):
    curPos = getTopLeft(grid)
    facing = 1
    
    for cmd in path:
        curPos, facing = doCommand(grid, cmd, curPos, facing)

    return curPos[0], curPos[1], facing

def sol(lines):
    
    gridStr, pathStr = lines.split("\n\n")
    gridRows = gridStr.split("\n") 

    grid = {}
    for r in range(len(gridRows)):
        for c in range(len(gridRows[r])):
            letter = gridRows[r][c]
            if letter == " ":
                pass

            elif letter == "." or letter == "#":
                grid[(r, c)] = letter

            else:
                raise Exception("Unknown letter.") 

    if False: # debug
        curPos, facing = (0, 75), 2
        for i in range(4 * 50):
            curPos, facing = move(grid, curPos, facing, True)
        print(curPos)

        curPos, facing = (25, 50), 1
        for i in range(4 * 50):
            curPos, facing = move(grid, curPos, facing, True)
        print(curPos)

        curPos, facing = (0, 125), 2
        for i in range(4 * 50):
            curPos, facing = move(grid, curPos, facing, True)
        print(curPos)

    else:
        path = []
        index = 0
        while index < len(pathStr):
            
            number = []
            while index < len(pathStr) and pathStr[index] in "0123456789":
                number.append(pathStr[index])
                index += 1
            
            path.append({
                "type": "number",
                "value": int("".join([str(x) for x in number])) 
            })

            if index < len(pathStr):
                path.append({
                    "type": "turn",
                    "value": pathStr[index]
                })

            index += 1

        row, col, facing = followPath(grid, path)

        return (1000 * (row + 1)) + (4 * (col + 1)) + ((facing - 1) % 4)

def main():
    
    #lines = open("test_input.txt").read()[:-1]
    lines = open("input.txt").read()[:-1]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 16362 - wrong
# 17366 - wrong
# 75284 - too low