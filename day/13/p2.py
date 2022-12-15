def inOrder(leftPacket, rightPacket):
    li, ri = 0, 0
    left = leftPacket
    if type(leftPacket) == dict:
        left = leftPacket["value"]
    
    right = rightPacket
    if type(rightPacket) == dict:
        right = rightPacket["value"]

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

def merge(a, b):
    ia = 0
    ib = 0
    lst = []
    while ia < len(a) and ib < len(b):
        if inOrder(a[ia], b[ib]):
            lst.append(a[ia])
            ia += 1
        else:
            lst.append(b[ib])
            ib += 1
    
    while ia < len(a):
        lst.append(a[ia])
        ia += 1

    while ib < len(b):
        lst.append(b[ib])
        ib += 1
    
    return lst

def merge_sort(lines):
    if len(lines) <= 1:
        return lines
    half = len(lines)//2
    return merge(
        merge_sort(lines[half:]),
        merge_sort(lines[:half])
    )
    
def sol(lines):
    lines = lines.split("\n")
    lines = list(filter(lambda x: x != "", lines))
    lines = [{
        "code": False,
        "value": eval(x)
        } for x in lines]
    lines.append({
        "code": True,
        "value": [[2]]
    })
    lines.append({
        "code": True,
        "value": [[6]]
    })

    lines = merge_sort(lines)

    for line in lines:
        pass
        #print(line)

    total = 1
    for i in range(len(lines)):
        line = lines[i]
        if line["code"]:
            total *= i + 1

    return total

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)