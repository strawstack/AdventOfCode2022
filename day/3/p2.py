def same(done, dtwo):
    for k in done:
        if k in dtwo:
            return k
    raise "not found"

def pri(letter):
    if ord(letter) > ord("Z"):
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27

def find3(group):
    for x in group[0]:
        if x in group[1] and x in group[2]:
            return x
    raise "not found"

def sol(lines):

    total = 0
    for i in range(0, len(lines), 3):

        group = [
            lines[i],
            lines[i + 1],
            lines[i + 2]
        ]

        d = []
        for bag in group:
            d.append({x: True for x in bag})

        letter = find3(d)
        p = pri(letter)
        total += p

    return total

def main():
    
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 2863 no
# 3037 no