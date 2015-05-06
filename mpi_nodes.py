#!/usr/bin/env python

def main():

	from optparse import OptionParser
	import sys

	usage = """
	mpi_nodes.py 2 10  all nodes between 2 and 10 including 2 and 10
	mpi_nodes.py o 2 4  all nodes between 2 and 2 + 4 - 1 including 5
	mpi_nodes.py n 2 4  only nodes 2 and 4
	Currently there are 12 nodes, node 11 is the master
	"""
	
	parser = OptionParser(usage = usage)
	(options, args) = parser.parse_args(sys.argv[1:])

	if args[0].isdigit():
		my_start = int(args[0])
		my_end = int(args[1]) + 1

		for i in range(my_start, my_end):
			if i!=11:
				sys.stdout.write("n%d"%i)
			else:
				sys.stdout.write("bmbpccl1")
			if i != (my_end - 1):
				sys.stdout.write(",")
	if args[0]=="o":
		my_start = int(args[1])
		my_end = int(args[1]) + int(args[2]) 

		for i in range(my_start, my_end):
			if i!=11:
				sys.stdout.write("n%d"%i)
			else:
				sys.stdout.write("bmbpccl1")
			if i != (my_end - 1):
				sys.stdout.write(",")
	elif args[0]=="n":
		for i in range(1,len(args)):
			if args[i]!="11":
				sys.stdout.write("n" + args[i])
			else:
				sys.stdout.write("bmbpccl1")
			if i != (len(args) - 1):
				# print ",",
				sys.stdout.write(",")

	sys.stdout.flush()

if __name__ == '__main__':
	main()

