import random
import sys
from copy import copy,deepcopy
from tester import run_test,load_code

def generate_shuffled_int_array(size):
	gen_array = [random.randint(0,size) for r in xrange(size)]
	return gen_array

def run_average_for_size(code,runs,size):
	sys.stdout.write("[")
	runtimes = []
	for r in xrange(runs):
		shuffled = generate_shuffled_int_array(size)
		sortd = sorted(shuffled)
		# BUG if you remove the following line this doesn't work
		sys.stdout.write(".")
		sys.stdout.flush()
		#print "%s # %s" % (id(shuffled), id(sortd))
		(eq, time) = run_test(code, shuffled, sortd)
		if (eq != True):
			return False;
		runtimes.append(time)

	sys.stdout.write("]")
	sys.stdout.flush()
	return reduce(lambda x, y: x + y, runtimes) / len(runtimes)

def main():

	tests = ['quicksort.py', 'mergesort.py', 'insertionsort.py', 'bubblesort.py']

	for file in tests:
		code = load_code(file)
		print "--- %s ---" % file
		base = run_average_for_size(code, 25, 1)
		print ""
		#print "base: %s" % run_average_for_size(code, 25, 1)
 		print " 100: %s" % (run_average_for_size(code, 25, 100) - base)
		print " 500: %s" % (run_average_for_size(code, 25, 500) - base)
		print " 1000: %s" % (run_average_for_size(code, 25, 1000) - base)
		print " 5000: %s" % (run_average_for_size(code, 25, 5000) - base)
		print " 10000: %s" % (run_average_for_size(code, 25, 10000) - base)

if __name__ == "__main__":
	main()