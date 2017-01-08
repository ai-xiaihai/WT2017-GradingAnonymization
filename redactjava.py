# Redact a list of names in a java source code file
# names would be turn into "NAME"
# Author: Xinnan Cheng (2017 WT)
# Usage: python redactjava <file with list of names> <original file> <redacted file>
#

import sys, re

# redact a string, return a string
def redact(str, list):
	#sline = iline.split("//",1)
	#cline = sline[1] #comment part of the line
	for name in list:
		if re.search(name, str, re.IGNORECASE):
			str = re.compile(re.escape(name), re.IGNORECASE).sub("NAME", str)
	return str

if __name__ == "__main__":

	# load name list
	name_list = (open(sys.argv[1], "r")).read().splitlines()
	
	# 0 means not comments, 1 means single line comments, 2 means multi-line comments
	flag = 0
	
	# redact the java file
	with open(sys.argv[2], "r") as fi, open(sys.argv[3], "w+") as fo:
		#do something
		
		while True:
			c = fi.read(1)
    		if not c:
    			# EOF
      			break
      		elif c == '/':
      			c2 = fi.read(1)
      			if c2 == "/":
      				# single line comment
      				fo.write( "//" + redact(fi.readline(), name_list) )
      				
      			elif c2 == "*":
      				# multi-line comment
      				
      			else:
      				fo.write(c+c2)
      		else:
      			fo.write(c)
      				
    	print "Read a character:", c
    	
# 		for iline in fi:
# 			if "//" in iline:
# 				#single line comment
# 				fo.write(single(iline,name_list))
# 				
# 			elif "/*" in iline:
# 				if "*/" in iline:
# 					
# 			else:
# 				#replicate lines that contains no comments
# 				fo.write(iline)
# 	