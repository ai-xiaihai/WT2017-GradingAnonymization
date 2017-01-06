# Redact a list of names in a java source code file
# Author: Xinnan Cheng (2017 WT)
# Usage: python redactjava <file with list of names> <original file> <redacted file>
#

import sys, re

# redact a single-line comment, return a string
def single(line, list):
	sline = iline.split("//",1)
	cline = sline[1] #comment part of the line
	for name in list:
		if re.search(name, line, re.IGNORECASE):
			cline = re.compile(re.escape(name), re.IGNORECASE).sub("NAME", cline)
	return sline[0] + "//" + cline

if __name__ == "__main__":

	#load name list
	name_list = (open(sys.argv[1], "r")).read().splitlines()
	
	#redact the java file
	with open(sys.argv[2], "r") as fi, open(sys.argv[3], "w+") as fo:
		#do something
		for iline in fi:
			if "//" in iline:
				#single line comment
				fo.write(single(iline,name_list))
				
			elif "/*" in iline:
				1+1
			else:
				#replicate lines that contains no comments
				fo.write(iline)
	
	#in_file = open( sys.argv[2], "r") 
	#out_file = open( sys.argv[3], "w+") 
	#in_file.close()
	#out_file.close()