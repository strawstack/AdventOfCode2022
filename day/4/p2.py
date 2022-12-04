def over_at_all(a, b):
    return not(
        a[1] < b[0] or b[1] < a[0]
    )

def sol(lines):
    ranges = [[[
        int(z) 
        for z in y.split("-")] 
        for y in x.split(",")] 
        for x in lines]
    
    total = 0
    for pair in ranges:
        if over_at_all(pair[0], pair[1]):
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