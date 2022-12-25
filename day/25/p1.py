def s(sn):
    TARGET = 30223327868980
    d = TARGET - snToDec(sn)
    if d > 0:
        print(f"UNDER: {d}")
    else:
        print(f"OVER : {d}")

def snToDec(snNumber):
    lookup = {
        "0": 0,
        "1": 1,
        "2": 2,
        "-": -1,
        "=": -2
    }
    BASE = 5
    numberValue = 0
    power = 0
    for i in range(len(snNumber) - 1, -1, -1):
        d = snNumber[i]
        numberValue += lookup[d] * (BASE ** power)
        power += 1
    return numberValue

def maxValueWithDigit(number, index):
    cNumber = number[:]
    for i in range(index, len(cNumber)):
        cNumber[i] = "2"
    return snToDec("".join(cNumber))

def minValueWithDigit(number, index):
    cNumber = number[:]
    for i in range(index, len(cNumber)):
        cNumber[i] = "="
    return snToDec("".join(cNumber))

def findNumber(TARGET, number, index):
    if index < len(number):
        digits = "=-012"
        for d in digits:
            #print(f"With: {d}")
            cNumber = number[:]
            cNumber[index] = d
            maxValue = TARGET - maxValueWithDigit(cNumber, index + 1)
            minValue = TARGET - minValueWithDigit(cNumber, index + 1)
            #print(f"  maxValue: {TARGET - maxValue}")
            #print(f"  minValue: {TARGET - minValue}")
            if minValue >= 0 and maxValue <= 0:
                number[index] = d
                findNumber(TARGET, number, index + 1)

def sol(lines):

    numbers = []

    for snNumber in lines:
        numbers.append(snToDec(snNumber))

    # 30223327868980
    TARGET = sum(numbers)

    digitsRequired = ["2"]
    while snToDec("".join(digitsRequired)) < TARGET:
        digitsRequired.append("2")

    # Required digits
    digitsReq = len(digitsRequired)

    number = ["0"] * digitsReq
    index = 0
    findNumber(TARGET, number, index)

    res = "".join(number)

    if snToDec(res) == TARGET:
        return res
    else:
        return "Incorrect."

def main():

    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]

    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)
