def same(done, dtwo):
    for k in done:
        if k in dtwo:
            return k
    raise "not found"

def pri(letter):
    if ord(letter) > ord("Z"):
        return ord(letter) - ord("A") + 27
    else:
        return ord(letter) - ord("a") + 1

def sol(lines):
    total = 0
    for line in lines:
        length = len(line)//2
        one, two = line[:length], line[length:]
        done = {x: True for x in one}
        dtwo = {x: True for x in two}
        letter = same(done, dtwo)
        p = pri(letter)
        total += p
    return total

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)