import re
inputFile = open("./input.txt", "r")
pattern = re.compile(r'(\S+):(\S+)')

validCount = 0
hash = {}


def valid_hgt(val):
    mg = re.search(r'^(\d+)(cm|in)$', val)
    if mg:
    	if mg.group(2) == "in":
	    return int(mg.group(1)) <= 76 and int(mg.group(1)) >= 59
    	if mg.group(2) == "cm":
	    return int(mg.group(1)) <= 193 and int(mg.group(1)) >= 150
    return False

def valid_hcl(val):
    return re.match(r'^#[a-f0-9]{6}$', val)

def valid_ecl(val):
    return re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', val)

def valid_pid(val):
    return re.match(r'^\d{9}$', val)


def check_valid_fields(hash):
	return (int(hash['byr']) >= 1920 and int(hash['byr']) <= 2002) and (int(hash['iyr']) >= 2010 and int(hash['iyr']) <= 2020) and (int(hash['eyr']) >= 2020 and int(hash['iyr']) <= 2030) and valid_hgt(hash['hgt']) and valid_hcl(hash['hcl']) and valid_ecl(hash['ecl']) and valid_pid(hash['pid']) 


for line in inputFile:

    if line.isspace():
	print(hash)
	#checkValidFields (either 8 entries or (7 entries and cid not in hash))
	if len(hash) == 8 or (len(hash) == 7 and "cid" not in hash):
	    if check_valid_fields(hash):
	    	#increment if valid
		print("valid")
	    	validCount += 1
	    	

	#reset hash for next passport
        hash = {}

    else:
	#re to get groups, add key,value pairs to hash
	for (key, value) in re.findall(pattern, line):
            hash[key] = value


print(validCount)