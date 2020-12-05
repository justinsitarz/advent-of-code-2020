#!/usr/local/bin/python
import math

def format_input(filename):
	tickets = []
	file = open(filename, 'r')
	lines = file.readlines() 
	for line in lines:
		tickets.append(line)


	return tickets


def binary_search(tickets):
	highest = 0
	ids = []
	for ticket in tickets:
		row = ticket[0:7]
		column = ticket[7:10]
		row = row.replace('F', '0').replace('B', '1')
		row = int(row, 2)
		column = column.replace('L', '0').replace('R','1')
		column = int(column, 2)
		id = row * 8 + column
		ids.append(id)
		if id > highest:
			highest = id
	return ids

def print_ids(ids):
	ids.sort()
	for id in ids:
		print(id)

def find_missing(ids):
	ids.sort()
	start = ids[0]
	for i in range(len(ids)):
		if i+40 !=  ids[i]:
			return ids[i] - 1



tickets = format_input('input.txt')

ids = binary_search(tickets)
#print_ids(ids)
missing = find_missing(ids)
print(missing)