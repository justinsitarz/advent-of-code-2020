#!/usr/bin/python
import re


index = 0
count = 0
index_list = []

def format_input(filename):
        file = open(filename, 'r')
        content = file.read()
        step_list = content.split('\n')
        steps = []
        pattern = re.compile('(\S+)\s(\S+)')
        for s in step_list:
        	m = pattern.search(s)
        	step_tuple = (m.group(1), m.group(2))
        	steps.append(step_tuple)
        	print(steps)
        return steps

def traverse_steps():
	global steps
	global index
	global count
	while index not in index_list:
		action = steps[index][0]
		value = int(steps[index][1])
		print('Index List: {}'.format(index_list))
		print('Action: {}'.format(action))
		print('Value: {}'.format(value))
		print('Index: {}'.format(index))
		print('Count: {}'.format(count))
		if action == 'acc':
			index_list.append(index)
			count += value
			index += 1
			continue
		if action == 'jmp':
			index_list.append(index)
			index += value
			continue
		if action == 'nop':
			index_list.append(index)
			index += 1
			continue
		else:
			return count




steps = format_input('input.txt')
count = traverse_steps()