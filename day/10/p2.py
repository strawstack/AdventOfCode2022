def parseCmd(line):
    if " " in line:
        v = line.split(" ")
        return {
            "name": v[0],
            "value": int(v[1]),
            "cycles": 2
        }
    else:
        return {
            "name": line,
            "value": None,
            "cycles": 1
        }

def processCmd(cmd):
    if cmd["name"] == "noop":
        return 0

    elif cmd["name"] == "addx":
        return cmd["value"]

def drawPixel(screen, screen_index, x):
    if abs((screen_index % 40) - x) <= 1:
        screen[screen_index] = "#"
    else:
        screen[screen_index] = "."

def printScreen(ROWS, COLS, screen):
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(screen[COLS * r + c])
        print("".join(row))

def sol(lines):
    cmds = [parseCmd(x) for x in lines]
    
    ROWS = 6
    COLS = 40

    x = 1
    current_cycle = 1

    screen_index = 0
    screen = ['.'] * (ROWS * COLS)

    for cmd in cmds:
        for cycle in range(cmd["cycles"]):
            drawPixel(screen, screen_index, x)

            if cycle == cmd["cycles"] - 1:
                x += processCmd(cmd)

            screen_index += 1
            if screen_index == ROWS * COLS:
                screen_index = 0
            current_cycle += 1

    # Print screen
    printScreen(ROWS, COLS, screen)
    return 0

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    #lines = [x[:-1] for x in open("input_test.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)