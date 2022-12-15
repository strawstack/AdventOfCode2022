def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def distance(sPos, bPos):
    return abs(sPos[0] - bPos[0]) + abs(sPos[1] - bPos[1])

def checkCell(cannotDict, hasBeacon, point):
    if point not in hasBeacon:
        cannotDict[point] = True

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

    yLine = 2000000

    cannotDict = {}

    for i in range(len(sensors)):
        sPos, bPos = sensors[i]
        sRadius = sensorRadius[i]
        
        closePoint = (sPos[0], yLine)
        moveLeft  = (-1, 0)
        moveRight = (1, 0)

        sRange = sRadius - distance(sPos, closePoint)

        if sRange >= 0:

            checkCell(cannotDict, hasBeacon, closePoint)

            leftPoint = closePoint
            for j in range(sRange):
                leftPoint = add(leftPoint, moveLeft)
                checkCell(cannotDict, hasBeacon, leftPoint)

            rightPoint = closePoint
            for j in range(sRange):
                rightPoint = add(rightPoint, moveRight)
                checkCell(cannotDict, hasBeacon, rightPoint)

    return len(cannotDict)

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)