
import os
import re, sys, formatter,pathlib
from formatter import snake_caselize, first_upper_camel_caselize, reverse_match

def check_table_name(table_name):
	print('checking arguments')
	print(table_name)
	# Raise error if the arguments aren't quite right



def create_table(table_name):
	'''
	Creates a table file with table_name
	'''


	check_table_name(table_name)


	valid_table_name = formatter.reverse_match(r'[^a-zA-Z]', table_name)
	if  valid_table_name:
		raise Exception("The model name can only contain lower case and uppercase letters ")
	
	lc_table_name = snake_caselize(table_name)
	# print(model_name[0]+model_name.split()[1:len(model_name)].join())
	# filename = lc_model_name+'.py'
	# with open(filename,'w') as f:
	f = open(os.path.dirname(os.path.realpath(__file__)) +'/tables/boiler_table.py')
	for x in f:
		x = x.replace('NAME', table_name)
		x =  x.replace('name', table_name.lower())
		print(x)
	