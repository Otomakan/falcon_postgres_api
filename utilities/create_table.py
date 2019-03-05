
import os
import re, sys, formatter,pathlib
from formatter import snake_caselize, first_upper_camel_caselize, reverse_match

def check_table_name(table_name):
	print('checking arguments')
	print(table_name)
	# Raise error if the arguments aren't quite right
	# args[0] == tablename


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
	# print('from ..models.%s import %s\n'
	# 	'from sqlalchemy import exc' % (table_name.lower(), table_name))
	
	# print("class %s:\n"
	# 	"\t\"\"\" %s Object Table\"\"\"\n"
	# 	"\tdef __init__(self, session):\n"
	# 	"\t\tself.session = session" % (model_name,model_name))
	
	# # Find function
	# print("\tfind(self, col_name, info):\n")

	# # Add Function
	# rows =  list(map(lambda x: {"name": snake_caselize(x.partition(":")[0]), "type": x.partition(':')[2].capitalize()},
	# 	args[1:len(args)]))
	# # print(rows)
	# for row in rows:
	# 	types = ['String', 'Integer']
	# 	# Check if the combo has the format row_name:row_type
	# 	# check_format
	# 	if not row["type"] in types:
	# 		raise Exception("%s has an invalid type the valid types are string and integer" % (row_name))

	# 	print("\t%s = Column(%s)\n" % (row['name'], row['type']))

	# print("\tdef __repr__(self):\n")
	# print("\t\treturn \"<%s(" % (model_name))
	
	# repr_start = ''
	# repr_end = ''
	# first = True
	# for  row in rows:
	# 	if first:
	# 		first = False
	# 		repr_start = "%s='%s')>\" %s (" % (row['name'],"%s","%")
	# 		repr_end = "self.%s" % (row['name']) +")"
	# 	else:
	# 		repr_start = "%s='%s', " % (snake_caselize(row['name']),"%s")  + repr_start
	# 		repr_end = "self.%s, " % (snake_caselize(row['name']))  + repr_end

	# print(repr_start + repr_end)
	# 