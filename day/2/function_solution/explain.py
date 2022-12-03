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
outcomeToName = {
    0: "Lose",
    3: "Draw",
    6: "Win"
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

for abc in "ABC":
    for xyz in "XYZ":
        mine = myLookup[xyz]
        other = otherLookup[abc]
        print(f"{xyz} ({mine}) vs {abc} ({other})")
        print(f"Result: {outcomeToName[matchLookup[mine][other]]}")
        print(f"{ord(xyz)} - {ord(abc)} = {ord(xyz) - ord(abc)}")
        
        print("")

# For Day 2 P1, converting the letters to ASCII numbers and subtracting them results in the following set of values: 21, 22, 23, 24, 25. Where the outcome of a match can be mapped to values as follows: 

# Win -> 24 or 21
# Lose -> 22 or 25
# Draw -> 23

# Subtracting 23 from all these values gives us the following:

# Win -> 1 or -2
# Lose -> -1 or 2
# Draw -> 0

# If we lay these values out as x-coordinates, we can find a rounded function that maps the loss values to 0, draw value to 1, and win value to 2. Multiplying the output of this function by 2 gives use either 0, 3, or 6 which is the score for the match.

# We can convert our choice to a score by subtracting the ASCII value of W from X, Y, Z to get a score of 1, 2, or 3.

# A 3D function that accepts two ASCII values and returns a score looks like this!

z=3 cos(((2 π (y-x-32))/(3))-2)+1+y-87