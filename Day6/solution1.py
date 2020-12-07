inputFile = open("./input.txt", "r")

hash = {}
sum = 0
party_count = 0

for line in inputFile:

    if line.isspace():
	print(hash)
        for char in hash.keys():
	    if hash[char] == party_count:
		sum += 1 
	    	

	#reset hash for next group
        hash = {}
        party_count = 0

    else:
	party_count += 1
	for char in line:
	    if char != "\n" and char not in hash:
            	hash[char] = 1
	    elif char in hash:
		hash[char] += 1


print(sum)