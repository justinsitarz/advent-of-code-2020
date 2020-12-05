#!/usr/local/bin/python

import re

def format_input(filename):
	passports = []
	file = open(filename, 'r')
	content = file.read()
	lines = content.split("\n\n")
	for line in lines:
		line = line.replace('\n', ' ')
		line = line.split(' ')
		passport = {}
		for l in line:
			entry_list = l.split(":")
			key = entry_list[0]
			value = entry_list[1]
			passport[key] = value
		passports.append(passport)
	return passports

def passport_checker(passports):
	valid = 0
	valid_passports = []
	for p in passports:
		if (len(p) == 8) or (len(p) == 7 and 'cid' not in p.keys()):
			valid_passports.append(p)

	return valid_passports

def field_checker(valid_passports):
	valid = 0
	verified_passports = []
	for p in valid_passports:
		if  birth_year_checker(p['byr']) and issue_year_checker(p['iyr']) and expiration_year_checker(p['eyr']) and \
			height_checker(p['hgt']) and hair_color_checker(p['hcl']) and eye_color_checker(p['ecl']) and pid_checker(p['pid']):
			
			verified_passports.append(p)

	return verified_passports

def birth_year_checker(byr):
	if 2003 > int(byr) > 1919:
		return True

def issue_year_checker(iyr):
	if 2021 > int(iyr) > 2009:
		return True

def expiration_year_checker(eyr):
	if 2031 > int(eyr) > 2019:
		return True

def height_checker(hgt):
	pattern = re.compile('^(\d*)([a-zA-Z]*)$')
	m = pattern.search(hgt)
	val = int(m.group(1))
	if (m.group(2) == "in" and (59 <= val <= 76)) or (m.group(2) == "cm" and (150 <= val <= 193)):
		return True

def hair_color_checker(hcl):
	pattern = re.compile('^#[a-fA-F0-9]{6}$')
	if pattern.match(hcl):
		return True

def eye_color_checker(ecl):
	if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return True

def pid_checker(pid):
	pattern = re.compile('^\d{9}$')
	if pattern.match(pid):
		return True

def result_checker(verified_passports):
	for p in verified_passports:
		if 'cid' in p.keys():
			p.pop('cid') 
		print(dict(sorted(p.items())))






passports = format_input('input.txt')
valid_passports = passport_checker(passports)
verified_passports = field_checker(valid_passports)
result_checker(verified_passports)

print(len(verified_passports))
# lower than 149


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# 	If cm, the number must be at least 150 and at most 193.
# 	If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.