lines = open("out.txt").readlines()

START_LINE = 5
DISTANCE = 10

START_LINE -= 1

collect = []
for i in range(len(lines)):
    if i >= START_LINE and i < START_LINE + DISTANCE:
        collect.append(lines[i])

print("".join([x.strip() + "\\n" for x in collect]))