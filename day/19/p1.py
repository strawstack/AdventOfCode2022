def getQualityLevel(blueprint):

    allOre = getAllOre(blueprint)

    

    return 0

def sol(lines):

    lines = [
        [y.split(" ")
        for y in x.split(": ")[1].split(". ")] 
        for x in lines.split("\n")]

    blueprints = []
    for line in lines:
        oreBotCost  = {line[0][-1]: int(line[0][-2])}
        clayBotCost = {line[1][-1]: int(line[1][-2])}
        obsBotCost  = {
            line[2][-4]: int(line[2][-5]),
            line[2][-1]: int(line[2][-2]),
        }
        geoBotCost  = {
            line[3][-4]: int(line[3][-5]),
            line[3][-1][:-6]: int(line[3][-2]) 
        }

        blueprints.append(
            {
                "oreBot": oreBotCost,
                "clayBot": clayBotCost,
                "obsBot": obsBotCost,
                "geoBot": geoBotCost
            }
        )

    total = 0
    for i in range(len(blueprints)):
        blueprint = blueprints[i]
        ql = (i + 1) * getQualityLevel(blueprint)
        return ql
        total += ql

    return total

def main():
    
    #lines = open("input.txt").read().strip()
    lines = open("test_input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)

# 106  - too low
# 2226 - too high
# 258  - wrong 
# 881  - wrong 
# 1354 - wrong