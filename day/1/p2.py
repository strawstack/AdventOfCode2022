def sol(lines):
    lines = [
        [int(y) 
        for y in x.split("\n")] 
        for x in lines.split("\n\n")]
    totals = [sum(x) for x in lines]
    return sum(sorted(totals)[-3:]) # Greatest three

def main():
    lines = open("input.txt").read().strip()
    ans = sol(lines)
    return ans

ans = main()
print(ans)