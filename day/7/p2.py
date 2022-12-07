def chunkResults(currentPath, resultList):
    res = []
    for i in range(0, len(resultList) - 1, 2):
        dirOrSize = resultList[i] # "dir" or size int
        itemName = resultList[i + 1]
        fullPathName = f"{currentPath}:{itemName}"
        res.append( (dirOrSize, fullPathName) )
    return res

def process_ls(dirs, size, current_dir, resultList):
    currentPath = ":".join(current_dir)
    dirs[currentPath] = chunkResults(currentPath, resultList)

def calculate_size(dirs, size, fullPathName):
    total_size = 0
    for (dirOrSize, fullPathName) in dirs[fullPathName]:
        if dirOrSize == "dir":
            total_size += calculate_size(dirs, size, fullPathName)
        
        else: # item is a file:
            total_size += int(dirOrSize)

    size[fullPathName] = total_size

    return total_size

def sol(lines):
    # {key, value} -> {dir_name, [dir_name list]}
    dirs = {}

    # {key, value} -> {dir_name, size int}
    size = {}

    lines = [x.strip().replace("\n", " ").split(" ") for x in lines.split("\n$")]
    lines[0] = lines[0][1:]

    current_dir = []

    for line in lines:
        if line[0] == "cd":
            if line[1] == "..":
                current_dir.pop()
                if len(current_dir) == 0:
                    current_dir.append("/")    

            elif line[1] == "/":
                current_dir.clear()
                current_dir.append("/")
            
            else: # dir name 
                current_dir.append(line[1])

        else: # line[0] == ls
            process_ls(dirs, size, current_dir, line[1:])

    TOTAL_SPACE = 70000000
    USED_SPACE = calculate_size(dirs, size, "/")
    FREE_SPACE = TOTAL_SPACE - USED_SPACE
    UPDATE_SPACE = 30000000
    REQUIRED_SPACE = UPDATE_SPACE - FREE_SPACE  

    lst = []
    for k in size:
        value = size[k] 
        if REQUIRED_SPACE <= value:
            lst.append((value, k))
    lst = sorted(lst)

    return lst[0][0]

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)