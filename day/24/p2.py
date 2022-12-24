from Queue import Queue
import math

def copyBlizzards(blizzards):
    newBlizzards = {}
    for k in blizzards:
        newBlizzards[k] = blizzards[k][:]
    return newBlizzards

def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

def eq_d(a, b):
    for k in a:
        if k not in b:
            return False
    for k in b:
        if k not in a:
            return False
    return True

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inBounds(ROWS, COLS, pos):
    (r, c) = pos
    return r >= 0 and r < ROWS and c >= 0 and c < COLS

def updateBlizzards(ROWS, COLS, blizzards):
    dirLookup = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    newBlizzards = {}
    for (r, c) in blizzards:
        for dir in blizzards[(r, c)]:
            nr, nc = add((r, c), dirLookup[dir])

            if not inBounds(ROWS, COLS, (nr, nc)):
                if dir == 0 or dir == 2:
                    nr = (ROWS - 1) - r

                else: # dir == 1 or dir == 3
                    nc = (COLS - 1) - c

            if (nr, nc) not in newBlizzards:
                newBlizzards[(nr, nc)] = []
            newBlizzards[(nr, nc)].append(dir)

    return newBlizzards

def bfs(ROWS, COLS, openCells, time, pos, endPos):
    seen = {}
    q = Queue()
    q.push( (time, pos) )

    seen[(time % len(openCells), pos)] = True

    while q.queue_size() > 0:
        time, pos = q.pop()

        if eq(pos, endPos):
            return time

        time += 1
        openCell = openCells[time % len(openCells)]

        dirs = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
            (0, 0) # wait
        ]

        for delta in dirs:
            newPos = add(pos, delta)
            if newPos in openCell:
                h = (time % len(openCells), newPos)
                if h in seen:
                    continue
                seen[h] = True
                q.push( (time, newPos) )

    return float("inf")

def renderBliz(ROWS, COLS, bliz):
    lookup = ["^", ">", "v", "<"]
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in bliz:
                if len(bliz[(r, c)]) == 1:
                    print(lookup[bliz[(r, c)][0]], end="")
                else:
                    print(len(bliz[(r, c)]), end="")
            else:
                print(".", end="")
        print("")

def renderOpenCells(ROWS, COLS, cells, pos):
    lookup = ["^", ">", "v", "<"]
    for r in range(ROWS):
        for c in range(COLS):
            if eq((r, c), pos):
                print("E", end="")
            elif (r, c) in cells:
                print("O", end="")
            else:
                print(".", end="")
        print("")

def sol(lines):

    dirLookup = {
        "^": 0,
        ">": 1,
        "v": 2,
        "<": 3
    }

    # Build list of blizzards
    # {key: value} -> {(r, c): [list of facing directions]}
    blizzards = {}
    ROWS = len(lines)
    COLS = len(lines[0])
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            letter = lines[r][c]
            if letter != ".":
                blizzards[(r - 1, c - 1)] = [dirLookup[letter]]

    # Remove walls
    ROWS -= 2
    COLS -= 2

    allBizzards = []
    LIMIT = math.lcm(ROWS, COLS)
    cBliz = copyBlizzards(blizzards)
    for i in range(0, LIMIT):
        allBizzards.append(cBliz)
        cBliz = updateBlizzards(ROWS, COLS, cBliz)

    startPos = (-1, 0)
    endPos = (ROWS, COLS - 1)

    openCells = []
    for b in allBizzards:
        openCell = {}
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in b:
                    openCell[(r, c)] = True

        openCell[startPos] = True
        openCell[endPos] = True

        openCells.append(openCell)

    t1 = bfs(ROWS, COLS, openCells, 0, startPos, endPos)

    t2 = bfs(ROWS, COLS, openCells, t1, endPos, startPos)

    totalTime = bfs(ROWS, COLS, openCells, t2, startPos, endPos)

    return totalTime

def main():

    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    lines = [x[:-1] for x in open("input.txt").readlines()]

    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)
