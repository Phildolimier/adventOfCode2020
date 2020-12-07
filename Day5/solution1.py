import re

inputFile = open("input.txt", "r")

currmax = 0

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
    print("row ", F, B,  " seat ", L)
    print(F*8)+L
    print(currmax)
    if (F * 8) + L > currmax:
        currmax = F * 8 + L
    

print(currmax)