def over(a, b):
    return a[0] <= b[0] and b[1] <= a[1]

def sol(lines):
    ranges = [[[
        int(z) 
        for z in y.split("-")] 
        for y in x.split(",")] 
        for x in lines]
    
    total = 0
    for pair in ranges:
        if over(pair[0], pair[1]) or over(pair[1], pair[0]):
            total += 1

    return total

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)