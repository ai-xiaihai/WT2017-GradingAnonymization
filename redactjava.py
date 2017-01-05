# Redact a list of names in a java source code file
# Author: Xinnan Cheng (2017 WT)
# Usage: python redactjava <file with list of names> <original file> <redacted file>
#

import sys

if __name__ == "__main__":
	in_file = open( sys.argv[1], "r") 
	out_file = open( sys.argv[2], "w+") 
	in_file.close()
	out_file.close()
