#!/usr/bin/python

def format_input(filename):
	group_answers = []
	file = open(filename, 'r')
	content = file.read()
	groups = content.split('\n\n')
	for group in groups:
		group_data = []
		group_count = len(group.split('\n'))
		all_answers = ''.join(group.split('\n'))
		uniques = set()
		for a in all_answers:
			uniques.add(a)
		group_data.append(group_count)
		group_data.append(uniques)
		group_data.append(all_answers)
		group_answers.append(group_data)
	return group_answers

def sum_of_answers(group_answers):
	total = 0
	for answers in group_answers:
		total += len(answers)
	return total

def check_user_answers(group_answers):
	total = 0
	for answers in group_answers:
		count = answers[0]
		uniques = answers[1]
		all_answers = answers[2]
		for u in uniques:
			if all_answers.count(u) == count:
				total += 1
	return total



group_answers = format_input("input.txt")
# print(sum_of_answers(group_answers))
total = check_user_answers(group_answers)
print(total)