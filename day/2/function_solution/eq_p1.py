from math import *

# Read input as int tuples. Ex. [[67, 88], [65, 88], ...]
games = [[ord(y) for y in x.strip().split(" ")] for x in open("input.txt").readlines()]

# Calculate score for a game
score = lambda g: 3 * round(cos(2 * pi * (g[1] - g[0] - 23) / 3 - 2) + 1) + g[1] - 87

print(sum(map(score, games)))