import glob, os, sys


if __name__ == "__main__":
	lines = 0
	if len(sys.argv) < 2:
		print "use path as input"	
		exit
	path = sys.argv[1]
	print "chaging dir to " + path
	for root, dirs, files in os.walk(path):
		for file in files:
			if (file.endswith(".cpp") or file.endswith(".c") or file.endswith(".h") or file.endswith(".hpp")) and not ("CMake" in file):
				print "reading file " , file
				with open(os.path.join(root, file)) as f:
                                	tot = sum(1 for line_ in f.readlines() if not line_.isspace())
					#print "file ", file , " contains " , tot , " lines"
					lines = lines + tot
	print "total lines " , lines
