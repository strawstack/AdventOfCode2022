from Queue import Queue

def copyBlizzards(blizzards):
    newBlizzards = {}
    for k in blizzards:
        newBlizzards[k] = blizzards[k][:]
    return newBlizzards

def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

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

def bfs(ROWS, COLS, blizzards, time, pos, endPos):
    q = Queue()
    q.push( (copyBlizzards(blizzards), time, pos) )

    while True:
        blizzards, time, pos = q.pop()
        blizzards = updateBlizzards(ROWS, COLS, blizzards)

        if eq(pos, endPos):
            return time

        print(pos, time)

        dirs = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        for delta in dirs:
            newPos = add(pos, delta)
            if pos not in blizzards and inBounds(ROWS, COLS, pos):
                q.push( (copyBlizzards(blizzards), time + 1, newPos) )

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
                blizzards[(r, c)] = [dirLookup[letter]]

    #
    # TODO: verify list of blizzards is accurate
    #

    # Remove walls
    ROWS -= 2
    COLS -= 2

    # [{time:, blizzards:}, ...]
    # for all times when (0, 0) cell is free
    startStates = []
    cBlizzards = copyBlizzards(blizzards)
    LIMIT = COLS
    for i in range(1, LIMIT):
        if (0, 0) not in cBlizzards:
            startStates.append({
                "time": i,
                "blizzards": cBlizzards
            })
        cBlizzards = updateBlizzards(ROWS, COLS, cBlizzards)

    endPos = (ROWS - 1, COLS - 1)

    bestTime = float("inf")
    for s in startStates:
        newTime = bfs(ROWS, COLS, s["blizzards"], s["time"], (0, 0), endPos)
        bestTime = min(bestTime, newTime + 1)

    return bestTime

def main():

    lines = [x[:-1] for x in open("test_input.txt").readlines()]
    #lines = [x[:-1] for x in open("input.txt").readlines()]

    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)
