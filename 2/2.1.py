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
	count = 0
	for p in passlist:
		char_count = p['password'].count(p['letter'])
		if int(p['max']) >= char_count >= int(p['min']):
			count += 1
	return count

def new_count_valid_passwords(passlist):
	count = 0
	for p in passlist:
		occurrences = 0
		password = p['password']
		letter = p['letter']
		first = int(p['min']) - 1
		second = int(p['max']) -1
		if password[first] == letter:
			occurrences += 1
		if password[second] == letter:
			occurrences += 1
		if occurrences == 1:
			count += 1
	return count



passlist = format_input('input.txt')
total_valid_passwords = count_valid_passwords(passlist)
print("Total passwords: " + str(total_valid_passwords))
new_total = new_count_valid_passwords(passlist)
print("New total: " + str(new_total))