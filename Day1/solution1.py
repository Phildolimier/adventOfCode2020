inputFile = open("./input.txt", "r")

hash = {}

for element in inputFile:
    el = int(element)
    if 2020 - el in hash:
	print(el, 2020- el)
    	break;
    if el not in hash:
	hash[el] = el