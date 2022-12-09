def inBounds(ROWS, COLS, lines, cur):
    (c, r) = cur
    return r >= 0 and r < ROWS and c >= 0 and c < COLS

def add(cur, d):
    return (cur[0] + d[0], cur[1] + d[1])

def search(ROWS, COLS, lines, pos):
    (c, r) = pos

    start_height = int(lines[r][c])
    dirs = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]

    ans = 1
    for d in dirs:
        start = (c, r)
        
        count = 0
        cur = add(start, d)
        while inBounds(ROWS, COLS, lines, cur):
            
            nxHeight = int(lines[cur[1]][cur[0]])
            count += 1
            if not (nxHeight < start_height):
                break

            cur = add(cur, d)

        ans *= count

    return ans

def sol(lines):
    ROWS = len(lines)
    COLS = len(lines[0])

    best_amount = 0
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            amount = search(ROWS, COLS, lines, (c, r))
            best_amount = max(best_amount, amount)

    return best_amount

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)