import sys
from datetime import datetime
from sbox import Runner

# Reads a file
def load_code(file):
	f = open(file);
	code = ''
	for lines in f:
		code = code + lines

	return code

# Runs the compiled code by generating a new sandbox environment
# params:
#	code: compiled python code to run
#	locals: a python object containing the names and values of the
#			local variables to run the code against
# return:
#	returns the produced stdout for the code and specified locals
def run_code(code, locals):
	runner = Runner()
	return runner.Run(code=code, locals=locals)

# Runs a test over a code with an input and an expected output as parameters
#
# return:
#	if expected_output and code output are equal return (True, [runtime])
#	else (False, -1)
def run_test(code, inpt, expected_output):
	runner = Runner()
	exp_out_str = str(expected_output)
	#print "input: %s exp_out: %s" % (inpt, expected_output)

	# Run the core
	tstart = datetime.now()
	out_str = run_code(code, {'inpt': inpt})
	tend = datetime.now()

	out_str = out_str.rstrip()
	if exp_out_str != out_str:
		#print "expected: %s,%s \nreturned: %s,%s" % (exp_out_str,len(exp_out_str),out_str,len(out_str))
		return (False, -1)
	time = tend - tstart

	return (True, time)

def main():
	code = load_code('testme.py')
	print "This is the input code: "
	print(code)
	print "\n\nThis is the result of the execution of the code: "
	#print run_code(code, {'inpt': [9,8,7,6,5,4,3,2,0,1]})
	print run_test(code, [9,8,7,6,5,4,3,2,0,1], [0,1,2,3,4,5,6,7,8,9])

if __name__ == "__main__":
	main()
