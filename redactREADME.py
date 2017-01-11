# Redact a list of names in a README file
# names would be turn into "NAME"
# Author: Xinnan Cheng (2017 WT)
# Usage: python redactREADME.py <name list file> <original file> <redacted file>

import sys, re

# redact a string, return a string
def redact(str, list):
	for name in list:
		if re.search(name, str, re.IGNORECASE):
			str = re.compile(re.escape(name), re.IGNORECASE).sub("NAME", str)           
	return str

if __name__ == "__main__":
	# load name list
	name_list = (open(sys.argv[1], "r")).read().splitlines()

	# redact the README line by line
	with open(sys.argv[2], "r") as fi, open(sys.argv[3], "w+") as fo:
		for line in fi:
			fo.write(redact(line, name_list))
