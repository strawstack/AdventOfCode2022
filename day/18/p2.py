def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def inBounds(xMin, xMax, yMin, yMax, zMin, zMax, tPos):
    x, y, z = tPos
    xx1 = xMin <= x 
    xx2 = x <= xMax
    yy1 = yMin <= y
    yy2 = y <= yMax
    zz1 = zMin <= z
    zz2 = z <= zMax
    return xx1 and yy1 and zz1 and xx2 and yy2 and zz2 

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

    # Determine a containing box
    # Pick vacant cell on outside
    # Run DFS to find all reachable
    # Calc surface area that touches steam
    
    xMin, xMax = float("inf"), float("-inf")
    yMin, yMax = float("inf"), float("-inf")
    zMin, zMax = float("inf"), float("-inf")

    for cube in cubes:
        x, y, z = cube
        xMin, xMax = min(xMin, x), max(xMax, x)
        yMin, yMax = min(yMin, y), max(yMax, y)
        zMin, zMax = min(zMin, z), max(zMax, z)
    
    xMin -= 1
    xMax += 1
    yMin -= 1
    yMax += 1
    zMin -= 1
    zMax += 1

    steamPos = (xMin, yMin, zMin)
    q = [steamPos]
    visited = {}
    visited[steamPos] = True

    while len(q) > 0:
        pos = q.pop()
        for d in dirs:
            tPos = add(pos, d)
            
            nv = tPos not in visited
            ib = inBounds(xMin, xMax, yMin, yMax, zMin, zMax, tPos)
            ntc = tPos not in cubes
            if nv and ib and ntc:
                visited[tPos] = True
                q.append(tPos)

    count = 0
    for cube in cubes:
        for d in dirs:
            adjPos = add(cube, d)
            if adjPos in visited:
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