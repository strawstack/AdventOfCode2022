def sol(text):
    
    index = 0
    while True:
        s = text[index:index + 14]
        d = {}
        for c in s:
            d[c] = True
        if len(d) == 14:
            return index + 14
        index += 1

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)