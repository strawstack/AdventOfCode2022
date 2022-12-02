def sol(lines):
    valueLookup = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    outcomeLookup = {
        "lose": 0,
        "draw": 3,
        "win": 6
    }
    myLookup = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    otherLookup = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    matchLookup = {
        "Rock": {
            "Rock": outcomeLookup["draw"],
            "Paper": outcomeLookup["lose"],
            "Scissors": outcomeLookup["win"]
        },
        "Paper": {
            "Rock": outcomeLookup["win"],
            "Paper": outcomeLookup["draw"],
            "Scissors": outcomeLookup["lose"]
        },
        "Scissors": {
            "Rock": outcomeLookup["lose"],
            "Paper": outcomeLookup["win"],
            "Scissors": outcomeLookup["draw"]
        }
    }

    lines = [x.split(" ") for x in lines]

    grandTotal = 0
    for line in lines:
        my, other = line[1], line[0]
        matchResult = matchLookup[myLookup[my]][otherLookup[other]]
        value = valueLookup[myLookup[my]]
        total = matchResult + value
        grandTotal += total
        
    return grandTotal

def main():
    
    #lines = open("input.txt").read().strip()
    lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)