def sol(lines):
    lines = lines.split("\n\n")
    lines = map(lambda x: x.split("\n"), lines)
    lines = map(lambda x: [int(y) for y in x], lines)
    totals = map(lambda x: sum(x), lines)
    return max(totals)

def main():
    lines = open("input.txt").read().strip()
    ans = sol(lines)
    print(ans)

main()