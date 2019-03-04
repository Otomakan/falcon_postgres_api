import re
	

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
	final = re.sub('(.)([A-Z][a-z]+)', r'\1_\2',str)
	final = re.sub('([a-z0-9])([A-Z])', r'\1_\2',final).lower()
	# Added this to avid double underscores
	return re.sub(r'__', '_', final)