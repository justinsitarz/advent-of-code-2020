#!/usr/local/bin/python


def format_input(filename):
	file = open(filename, 'r') 
	lines = file.readlines() 
	passlist = []
	for line in lines: 
		obj = {}
		l = line.split(' ')
		range = l[0].split('-')
		obj['min'] = range[0]
		obj['max'] = range[1]
		obj['letter'] = l[1].strip(':')
		obj['password'] = l[2].strip('\n')


		passlist.append(obj)

	return(passlist)

def count_valid_passwords(passlist):
	pass


passlist = format_input('input.txt')
print(passlist)

