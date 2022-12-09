import math

def moveTail(head, tail):
    moveRow, moveCol = 0, 0
    if head[0] - tail[0] != 0:
        moveRow = (head[0] - tail[0]) / abs(head[0] - tail[0])
    
    if head[1] - tail[1] != 0:
        moveCol = (head[1] - tail[1]) / abs(head[1] - tail[1])
    
    return (math.floor(tail[0] + moveRow), math.floor(tail[1] + moveCol))

def tooFar(head, tail):
    one = abs(head[0] - tail[0])
    two = abs(head[1] - tail[1])
    return one == 2 or two == 2

def add(head, d):
    return (head[0] + d[0], head[1] + d[1])

def sol(lines):
    lines = [x.split(" ") for x in lines]
    lines = [(x[0], int(x[1])) for x in lines]
    
    dirs = {
        "U": (-1, 0),
        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1)
    }

    track = {}

    rope = [
        (0, 0),

        (0, 0),
        (0, 0),
        (0, 0),

        (0, 0),
        (0, 0),
        (0, 0),

        (0, 0),
        (0, 0),
        (0, 0)
    ]

    for (direction, number) in lines:
        d = dirs[direction]

        # Move head of rope
        for i in range(number):
            rope[0] = add(rope[0], d)
        
            # Check all other knots
            for i in range(1, len(rope)):
                if tooFar(rope[i - 1], rope[i]):
                    rope[i] = moveTail(rope[i - 1], rope[i])
                    
                    
            track[rope[len(rope) - 1]] = True

            #print(f"head: {head}")
            #print(f"tail: {tail}")
            #print("")
    
    return len(track)

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)