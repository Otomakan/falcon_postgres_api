import sys, os
from create_model import create_model

argv = sys.argv
if sys.argv[1]=="help":
	print("To use this module simply enter the name of the type you are trying to generate."
					"accepted types are: model, middleware, models, route, table, helper")

# sys.argv.shift()

def switch(type, arguments):
	return {
		'model':create_model(arguments),
		'b':2
	}[type]

def call_model(arg):
	print('Your arg is a model we think')
	print('look')
	print(arg)

def generate():
	switch(argv[1], argv[2:len(argv)])
# for arg in sys.argv:
# 	print (arg)

# if __name__ =='__main__':
# 	generate()
# 	create_model()
generate()