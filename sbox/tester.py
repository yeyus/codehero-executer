import sys
from sbox import Runner

def read_file(file):
	f = open(file);
	code = ''
	for lines in f:
		code = code + lines

	return code

def run_code(code):
	runner = Runner()
	return runner.Run(code=code)

if __name__ == "__main__":
	code = read_file('testme.py')
	print "This is the input code: "
	print(code)
	print "\n\nThis is the result of the execution of the code: "
	print run_code(code)
