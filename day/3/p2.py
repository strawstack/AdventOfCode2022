def pri(letter):
    if ord(letter) > ord("Z"):
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27

def sol(lines):

    return sum(
        [
            pri(
                set(
                    lines.pop()
                )
                .intersection(
                    set(
                        lines.pop()
                    )
                ).intersection(
                    set(
                        lines.pop()
                    )
                ).pop()
            )
            for x in range(len(lines)//3)
        ]
    )

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)