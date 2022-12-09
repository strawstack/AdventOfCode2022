def hash_tree(col, row):
    return f"{col}:{row}"

def sol(lines):
    ROWS = len(lines)
    COLS = len(lines[0])
    
    visible = {}

    for r in range(ROWS):
        tallest_so_far = -1
        for c in range(COLS):
            
            outer_row = r == 0 or r == ROWS - 1
            outer_col = c == 0 or c == COLS - 1

            height = int(lines[r][c])
            if height > tallest_so_far or outer_row or outer_col:
                visible[hash_tree(c, r)] = True
            tallest_so_far = max(tallest_so_far, height)

    for r in range(ROWS):
        tallest_so_far = -1
        for c in range(COLS - 1, -1, -1):
            
            outer_row = r == 0 or r == ROWS - 1
            outer_col = c == 0 or c == COLS - 1

            height = int(lines[r][c])
            if height > tallest_so_far or outer_row or outer_col:
                visible[hash_tree(c, r)] = True
            tallest_so_far = max(tallest_so_far, height)

    for c in range(COLS):
        tallest_so_far = -1
        for r in range(ROWS):
            outer_row = r == 0 or r == ROWS - 1
            outer_col = c == 0 or c == COLS - 1

            height = int(lines[r][c])
            if height > tallest_so_far or outer_row or outer_col:
                visible[hash_tree(c, r)] = True
            tallest_so_far = max(tallest_so_far, height)

    for c in range(COLS):
        tallest_so_far = -1
        for r in range(ROWS - 1, -1, -1):
            outer_row = r == 0 or r == ROWS - 1
            outer_col = c == 0 or c == COLS - 1

            height = int(lines[r][c])
            if height > tallest_so_far or outer_row or outer_col:
                visible[hash_tree(c, r)] = True
            tallest_so_far = max(tallest_so_far, height)

    return len(visible)

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)