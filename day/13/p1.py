def inOrder(left, right):
    li, ri = 0, 0

    while li < len(left) and ri < len(right):
        
        lv = left[li]
        rv = right[ri]

        if type(lv) == int and type(rv) == int:
            if lv == rv:
                pass
            else:
                return lv < rv
        
        elif type(lv) == list and type(rv) == list:
            res = inOrder(lv, rv)
            if res == None:
                pass
            else:
                return res

        else: # one is list and one int
            if type(lv) == int:
                left[li] = [left[li]]
            else:
                right[ri] = [right[ri]]
            continue # skip increment index
        
        li += 1
        ri += 1
    
    if li == len(left) and ri == len(right):
        return None
    else:
        return li == len(left)
    
def sol(lines):
    lines = lines.split("\n\n")
    lines = [[eval(y) for y in x.split("\n")] for x in lines]

    ans = []
    for i in range(len(lines)):
        line = lines[i]
        a, b = line
        if inOrder(a, b):
            ans.append(i + 1)
        
    return sum(ans)

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)