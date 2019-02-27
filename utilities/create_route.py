
import os
import re, sys, formatter,pathlib
from formatter import snake_caselize, first_upper_camel_caselize, reverse_match

def check_route_name(route_name):
	print('checking arguments')
	print(route_name)
	# Raise error if the arguments aren't quite right



def create_route(route_name):
	'''
	Creates a route file with route_name
	'''

	check_route_name(route_name)

	valid_route_name = formatter.reverse_match(r'[^a-zA-Z]', route_name)
	if  valid_route_name:
		raise Exception("The model name can only contain lower case and uppercase letters ")
	
	lc_route_name = snake_caselize(route_name)
	# print(model_name[0]+model_name.split()[1:len(model_name)].join())
	# filename = lc_model_name+'.py'
	# with open(filename,'w') as f:
	f = open(os.path.dirname(os.path.realpath(__file__)) +'/routes/boiler_route.py')
	for x in f:
		x = x.replace('NAME', route_name)
		x =  x.replace('name', route_name.lower())
		print(x)