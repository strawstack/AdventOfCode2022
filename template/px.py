def sol(lines):
    print(len(lines))

def main():
    lines = [x[:-1] for x in open("input.txt").readlines()]
    ans = sol()