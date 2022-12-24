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
    q = Queue()
    q.push( (time, pos) )

    while q.queue_size() > 0:
        time, pos = q.pop()
        time += 1
        openCell = openCells[time % len(openCells)]

        if eq(pos, endPos):
            return time + 1

        dirs = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        for delta in dirs:
            newPos = add(pos, delta)
            if newPos in openCell:
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

def renderOpenCells(ROWS, COLS, cells):
    lookup = ["^", ">", "v", "<"]
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in cells:
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

    openCells = []
    for b in allBizzards:
        openCell = {}
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in b:
                    openCell[(r, c)] = True
        openCells.append(openCell)

    bestTime = float("inf")

    endPos = (ROWS - 1, COLS - 1)
    for i in range(len(openCells)):
        if (0, 0) in openCells[i]:
            t = bfs(ROWS, COLS, openCells, i, (0, 0), endPos)
            bestTime = min(bestTime, t)

    return bestTime

def main():

    lines = [x[:-1] for x in open("test_input.txt").readlines()]
    #lines = [x[:-1] for x in open("input.txt").readlines()]

    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)
