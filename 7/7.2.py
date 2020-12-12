#!/usr/bin/python

import re

bags = set()
bag_list = [['shiny gold', 2]]
count = 0
global_bags = []
bag_total = 0


def format_input(filename):
        file = open(filename, 'r')
        content = file.read()
        bag_rules = content.split('\n')
        return bag_rules

def build_graph(bag_rules):
	bag_dict = {}
	for rule in bag_rules:
		rule = rule.split(' bags contain ')
		outer = rule[0]
		bag_dict[outer] = []
		inner_tmp = rule[1].split(',')
		inner_list = []
		for inner in inner_tmp:
			inner_bag = get_inner_bags(inner)
			if inner_bag is not None:
				bag_dict[outer].append([inner_bag[0], inner_bag[1]])
	return bag_dict

def get_inner_bags(bag):
	if bag != 'no other bags.':
		pattern = re.compile('(\d)\s(.*)\sbag')
		m = pattern.search(bag)
		if m.group(1) is not None:
			inner_bag_num = m.group(1)
		else:
			inner_bag_num = '0'
		inner_bag = m.group(2)
		return inner_bag, int(inner_bag_num)

def check_for_gold(bag_dict, bag_list): 
	global count
	new_bag_list = []
	for b in bag_list:
		for key, value in bag_dict.items():
			if b in value:
				bags.add(key)
				new_bag_list.append(key)
	if new_bag_list:
		count += 1
		check_for_gold(bag_dict, new_bag_list)
	return bags

# def check_contents_of_shiny_gold(bag_dict, bag_list):
# 	global global_bags
# 	global bag_total
# 	new_bag_list = []
# 	for b in bag_list:
# 		print(b)
# 		if b is not None:
# 			new_bags = bag_dict.get(b[0])
# 			print('New bags {}'.format(new_bags))
# 			for n in new_bags:
# 				n[1] *= b[1]
# 				print(n)
# 				bag_total += n[1]
# 			global_bags.append(new_bags)
# 			check_contents_of_shiny_gold(bag_dict, new_bags)

def check_bags(bag_list):
	global bag_dict
	global bag_total
	for bag in bag_list:
		multiplier = bag[1]
		print('Multiplier: {}'.format(multiplier))
		print('Bag: {}'.format(bag))
		check_bags(bag_dict[bag[0]])





bag_rules = format_input('test-input.txt')
bag_dict = build_graph(bag_rules)
# print(bag_dict)
all_bags = check_for_gold(bag_dict, bag_list)
# print("Number of bag colors that can contain 'shiny gold': " + str(len(all_bags)))
# check_contents_of_shiny_gold(bag_dict, bag_list)
# print('Bag total: {tot}'.format(tot=bag_total))

check_bags(bag_list)