def findIndex(lst, index):
    # Find the tuple with that original index
    for i in range(len(lst)):
        origIndex, n = lst[i]
        if index == origIndex:
            return i

def getZero(lst):
    for i in range(len(lst)):
        origIndex, n = lst[i]
        if n == 0:
            return i 

def sol(lines):
    
    lst = [int(x) for x in lines.split("\n")]
    SIZE = len(lst)
    
    lst = list(enumerate(lst))

    # In order of original index
    origIndex = 0
    while origIndex < SIZE:

        newIndex = findIndex(lst, origIndex)
        _, n = lst[newIndex]
        targetIndex = (newIndex + n) % (SIZE - 1)

        # Remove original element
        if newIndex == SIZE - 1:
            lst.pop()
        else:
            lst = lst[:newIndex] + lst[newIndex + 1:]
        
        if n < 0 and targetIndex == 0:
            targetIndex = SIZE

        elif n > 0 and targetIndex == SIZE - 1:
            targetIndex = 0

        # Add element back
        lst = lst[:targetIndex] + [(origIndex, n)] + lst[targetIndex:]

        origIndex += 1

    zeroIndex = getZero(lst)
    one   = (zeroIndex + 1000) % SIZE
    two   = (zeroIndex + 2000) % SIZE
    three = (zeroIndex + 3000) % SIZE

    return lst[one][1] + lst[two][1] + lst[three][1]

def main():
    
    #lines = open("test_input.txt").read().strip()
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 1072 - wrong