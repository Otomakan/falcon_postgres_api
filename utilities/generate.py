import sys, os
from create_model import create_model
from create_table import create_table
argv = sys.argv
if sys.argv[1]=="help":
	print("To use this module simply enter the name of the type you are trying to generate."
					"accepted types are: model, middleware, models, route, table, helper")

def switch(type, arguments):
	if type=="model" :
		create_model(arguments),
	elif type=="table" :
		create_table(arguments[0])
	else:
		raise Exception("%s is not a valid argument please enter model or table" %(type))


def call_model(arg):
	print('Your arg is a model we think')
	print('look')
	print(arg)

def generate():
	''' 
		Reads the arguments in the command line and calls the function of the first argument
		The first argument should be one of : model, table

	 '''
	switch(argv[1], argv[2:len(argv)])


if __name__ =='__main__':
	generate()