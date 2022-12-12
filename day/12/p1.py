from Queue import Queue

def inBounds(ROWS, COLS, pos):
    r, c = pos
    return r >= 0 and r < ROWS and c >= 0 and c < COLS

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def letterToHeight(letter):
    if letter == "S":
        return ord("a")
    if letter == "E":
        return ord("z")
    return ord(letter)

def canStepGivenHeight(grid, a, b):
    
    aRow, aCol = a
    bRow, bCol = b
    
    aHeight = letterToHeight(grid[aRow][aCol])
    bHeight = letterToHeight(grid[bRow][bCol])

    return aHeight + 1 >= bHeight

def bfs(ROWS, COLS, grid, initPos, endLetter): 
    adj = [
        (-1, 0), # up
        (0, 1), # right 
        (1, 0), # down
        (0, -1)  # left
    ]

    q = Queue()
    q.push({
        "curPos": initPos,
        "steps": 0
    })

    visited = {}
    visited[initPos] = True

    while q.queue_size() > 0:
        
        cell = q.pop()
        cRow, cCol = cell["curPos"]
        steps = cell["steps"]

        #print(" " * steps + f"({cRow}, {cCol})")

        # End condition
        letter = grid[cRow][cCol]
        if letter == endLetter:
            return steps

        # For each neighbour 
        for adjDir in adj:
            tRow, tCol = add((cRow, cCol), adjDir)

            if inBounds(ROWS, COLS, (tRow, tCol)): 
                visitedCheck = (tRow, tCol) not in visited
                heightCheck = canStepGivenHeight(grid, (cRow, cCol), (tRow, tCol))

                if visitedCheck and heightCheck:
                    q.push({
                        "curPos": (tRow, tCol),
                        "steps": steps + 1
                    })
                    visited[(tRow, tCol)] = True

def getPos(ROWS, COLS, grid, letter):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == letter:
                return (r, c)

def sol(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    startPos = getPos(ROWS, COLS, grid, "S")
    steps = bfs(ROWS, COLS, grid, startPos, "E")

    return steps

def main():
    
    lines = [x[:-1] for x in open("input.txt").readlines()]
    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)