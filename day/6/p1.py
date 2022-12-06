def sol(text):
    
    start = 0
    end = 4

    index = 0
    while True:
        s = text[index:index + 4]
        d = {}
        for c in s:
            d[c] = True
        if len(d) == 4:
            return index + 4
        index += 1

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)