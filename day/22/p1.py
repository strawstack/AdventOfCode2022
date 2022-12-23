def getTopLeft(grid):
    minCol = float("inf")
    for row, col in grid:
        if row == 0:
            minCol = min(minCol, col)
    return 0, minCol

def add(curPos, delta):
    return (curPos[0] + delta[0], curPos[1] + delta[1])

def getOppositeTile(grid, newPos, facing):
    otherFacing = (facing + 2) % 4
    deltaLookup = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nextPos = None
    while True:
        nextPos = add(newPos, deltaLookup[otherFacing])

        if nextPos not in grid:
            return newPos
        
        newPos = nextPos
    
    raise Exception("Failed to find opposite cell.") 

# One step in direction facing
# Unless you hit a wall
def move(grid, curPos, facing):

    deltaLookup = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    newPos = add(curPos, deltaLookup[facing])

    if newPos not in grid:
        oRow, oCol = getOppositeTile(grid, newPos, facing)

        if grid[(oRow, oCol)] == "#":
            return curPos
        
        else: # grid[(oRow, oCol)] == "."
            return (oRow, oCol)

    elif grid[newPos] == "#":
        return curPos
    
    elif grid[newPos] == ".":
        return newPos
    
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
            curPos = move(grid, prevPos, facing)

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