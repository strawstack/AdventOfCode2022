import sys
import os

# Read command line arg
year = 2022

try:
    day_number = sys.argv[1]
except:
    print("Missing command line arg: python3 make.py [day_number]")

# Create day folder
try:
    os.mkdir(f"day/{day_number}")
except:
    print(f"Dir 'day/{day_number}' already exists.")

# Copy template file
template = open("template/px.py", "r").read()
p1 = open(f"day/{day_number}/p1.py", "w")
p1.write(template)
#p2 = open(f"day/{day_number}/p2.py", "w")
#p2.write(template)

# Get input file
session = open("secret.txt").read().strip()
cmd = f"curl -b 'session={session}' https://adventofcode.com/{year}/day/{day_number}/input > day/{day_number}/input.txt"

os.system(cmd)

# Example command
# Gets input, create files, cd into given day, run p1 code 
# python3 make.py 16 && cd day/16 && python3 p1.py