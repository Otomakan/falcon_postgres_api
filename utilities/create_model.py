import os
import re, sys


def check_args(args):
	print('checking arguments')
	print(args)
	# Raise error if the arguments aren't quite right
	# args[0] == tablename

def reverse_match(reg, str):
	return bool(re.search(reg,str))

def capitalize(str):
	return str.replace(str[0],str[0].upper(),1)

def first_upper_camel_caselize(str):
	splitted_underscore  = str.split('_')
	if len(str.split("_"))==1:
		return capitalize(str)
	return ''.join(list(map(lambda x: x.capitalize(), (splitted_underscore))))

def snake_caselize(str):
	# Method stolen from epost on stackoverflow thank you!
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2',str)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2',s1).lower()


def create_model(args):

	check_args(args)

	model_name = capitalize(args[0])
	valid_model_name = reverse_match(r'[^a-zA-Z]', model_name)
	if  valid_model_name:
		raise Exception("The model name can only contain lower case and uppercase letters ")
	
	lc_model_name = snake_caselize(model_name)
	# print(model_name[0]+model_name.split()[1:len(model_name)].join())
	# filename = lc_model_name+'.py'
	# with open(filename,'w') as f:

	print('from . import Base\nfrom sqlalchemy import Column, Integer, String,relationship\n\n')

	print("class %s(object):\n\t\"\"\" %s Object Table\"\"\"\n\tdef __init__(self, arg):\n\t\tsuper(%s, self).__init__()\n\t\tself.arg = arg\n" % (model_name,model_name,model_name))
	print("\tid = Column(Integer, primary_key=True)\n")

	rows =  list(map(lambda x: {"name": first_upper_camel_caselize(x.partition(":")[0]), "type": capitalize(x.partition(':')[2])},
		args[1:len(args)]))
	# print(rows)
	for row in rows:
		types = ['String', 'Integer']
		# Check if the combo has the format row_name:row_type
		# check_format
		if not row["type"] in types:
			raise Exception("%s has an invalid type the valid types are string and integer" % (row_name))

		print("\t%s = Column(%s)\n" % (snake_caselize(row['name']), row['type']))

	print("\tdef __repr__(self):\n")
	print("\t\treturn \"<%s(" % (model_name))
	
	repr_start = ''
	repr_end = ''
	first = True
	for  row in rows:
		if first:
			first = False
			repr_start = "%s='%s')>\" %s (" % (snake_caselize(row['name']),"%s","%")
			repr_end = "self.%s" % (snake_caselize(row['name'])) +")"
		else:
			repr_start = "%s='%s', " % (snake_caselize(row['name']),"%s")  + repr_start
			repr_end = "self.%s, " % (snake_caselize(row['name']))  + repr_end

	print(repr_start + repr_end)
	