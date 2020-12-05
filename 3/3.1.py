#!/usr/local/bin/python

def format_input(filename):
	line_list = []
	file = open(filename, 'r')
	lines = file.readlines()
	for line in lines:
		line_list.append(line.rstrip())
	return line_list

def split_lines(line_list):
	lines = []
	for line in line_list:
		lines.append(list(line))
	return lines

def traverse_grid(lines, x, y):
	width = len(lines[0])
	length = len(lines)
	offset = width - x 
	counter = 0
	index = 0
	for i in range(0, length, y):
		if lines[i][index] == '#':
			counter += 1
		# print("".join(lines[i]))
		# print(lines[i][index])
		# print(index)
		if index < offset:
			index += x
		else:
			index -= offset
	return counter		



line_list = format_input('input.txt')
lines = split_lines(line_list)
num_of_trees = traverse_grid(lines, 1, 2)
print(num_of_trees)



