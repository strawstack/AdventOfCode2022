def eq(a, b):
    return a[0] == b[0] and a[1] == b[1]

def mul(a, s):
    return (a[0] * s, a[1] * s)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def distance(sPos, bPos):
    return abs(sPos[0] - bPos[0]) + abs(sPos[1] - bPos[1])

def checkCell(cannotDict, hasBeacon, point):
    if point not in hasBeacon:
        cannotDict[point] = True

def checkPoint(index, sensors, sensorRadius, curPoint):
    x, y = curPoint
    if x < 0 or x > 4000000 or y < 0 or y > 4000000:
        return False

    for i in range(len(sensors)):
        sPos, bPos = sensors[i]
        sRadius = sensorRadius[i]

        if i == index:
            continue
        
        if distance(sPos, curPoint) <= sRadius:
            return False
    return True

def sol(lines):
    
    sensors = []
    for line in lines:
        one, two = line.split(": closest beacon is at ")
        sensorPosText = one.split(" at ")[1].split(", ")
        beaconPosText = two.split(", ")

        sensorPosText = [int(x[2:]) for x in sensorPosText]
        beaconPosText = [int(x[2:]) for x in beaconPosText]
        
        sensors.append((
            (sensorPosText[0], sensorPosText[1]),
            (beaconPosText[0], beaconPosText[1])
        ))

    hasBeacon = {}
    for (sPos, bPos) in sensors:
        hasBeacon[bPos] = True

    # Each beacon has a radius
    sensorRadius = []
    for (sPos, bPos) in sensors:
        sensorRadius.append( distance(sPos, bPos) )
    
    # From a sensor, we can look at the closest point to that
    # sensor that sits on 'yLine' find the distance to that point

    for i in range(len(sensors)):
        sPos, bPos = sensors[i]
        sRadius = sensorRadius[i]
        
        dirs = [
            ((0, -1), (1, 1)),
            ((1, 0), (-1, 1)),
            ((0, 1), (-1, -1)),
            ((-1, 0), (1, -1))
        ]

        points = []
        for d, nextDir in dirs:
            points.append(
                add(
                    add(sPos, mul(d, sRadius)),
                    d
                )
            )
        
        index = 0
        curPoint = points[index]
        while True:
            if index == 3:
                break

            elif eq(curPoint, points[index + 1]):
                index += 1
            
            else:

                if checkPoint(i, sensors, sensorRadius, curPoint):
                    return curPoint[0] * 4000000 + curPoint[1]

                curPoint = add(curPoint, dirs[index][1])
                
    return None

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)