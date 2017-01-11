# Redact a list of names in a java source code file
# names would be turn into "NAME"
# Author: Xinnan Cheng (2017 WT)
# Usage: python redactjava.py <name list file> <original file> <redacted file>

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
	
	# redact the java file
	with open(sys.argv[2], "r") as fi, open(sys.argv[3], "w+") as fo:
		c = fi.read(1)
		while c:
			if c == "/":
				c2 = fi.read(1)
				if c2 == "/": # single line comment
					fo.write( "//" + redact(fi.readline(), name_list) )
					
				elif c2 == "*": # multi-line comment
					comm = ""
					while True:
						cm = fi.read(1)
						comm += cm
						if not cm: # file end without "*/" (unlikely outcome)
							fo.write("/*" + redact(comm, name_list))
							break
						elif cm == "*":
							cm2 = fi.read(1)
							comm += cm2
							if cm2 == "/": # end of multi-line comment
								fo.write("/*" + redact(comm, name_list))
								break
				else:
					fo.write(c+c2)
			else:
				fo.write(c)
			c = fi.read(1)
			
