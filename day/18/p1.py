def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def sol(lines):
    
    cubes = {}
    
    for line in lines:
        x, y, z = [int(x) for x in line.split(",")]
        cubes[(x, y, z)] = True
    
    dirs = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if abs(x) + abs(y) + abs(z) == 1:
                    dirs.append( (x, y, z) )

    count = 0
    for cube in cubes:
        for d in dirs:
            adjPos = add(cube, d)
            if adjPos not in cubes:
                count += 1

    return count

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    #lines = [x[:-1] for x in open("test_input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)