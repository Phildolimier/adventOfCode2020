import re

inputFile = open("input.txt", "r")

hash = {}

for line in inputFile:
    F = 0
    B = 127
    for char in line[0:7]:
	if char == "F":
	    B = (F+B-1)/2
	if char == "B":
	    F = (F+B+1)/2

    L = 0
    R = 7
    for char in line[7:10]:
	if char == "L":
	    R = (R+L-1)/2
	if char == "R":
	    L = (R+L+1)/2

    hash[(F * 8) + L] = True
 
    

for x in range(999):
    if x not in hash and (x-1 in hash) and (x+1 in hash):
	print(x)