import os
import re

table_name = "MyTable"

def convert(string):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2',string)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2',s1).lower()

filename = convert(table_name)+'.py'
with open(filename,'w') as f:

	quote= {"phases":" ", 
			"switchBoardUpgradeIncluded":False,
			"switchBoardUpgradePrice":0,
			"numberOfCircuits":" ",
			"numberOfSplitArrays":0,
			"panelOrientation":"portrait",
			"numberOfStoreys": " ",
			"raisedFrames": " ",
			"raisedFramesPrice": 0,
			"storeys": " ",
			"roofType": " ",
			"roofPitch": " ",
			"inverterLocation": " ",
			"adequateSiteAccess":" ",}

	f.write('from . import Base\nfrom sqlalchemy import Column, Integer, String,relationship\n\n')

	f.write("class %s(object):\n\t\"\"\" %s Object Table\"\"\"\n\tdef __init__(self, arg):\n\t\tsuper(%s, self).__init__()\n\t\tself.arg = arg\n" % (table_name,table_name,table_name))
	f.write("\tid = Column(Integer, primary_key=True)\n")

	for key in quote:
		typeof = type(quote[key])
		key_type = ""
		if(typeof==type(2)):
			key_type = "Integer"
		elif (typeof==type("a")):
			key_type = "String"
		elif (typeof==type(True)):
			key_type = "Integer"
		f.write("\t%s = Column(%s)\n" % (key, key_type))

	# f.close()
	f.write("\tdef __repr__(self):\n")
	f.write("\t\treturn \"<%s(" % (table_name))
	for  key in quote:
		 f.write("%s='%s', " % (key,"%s"))

	# f.seek(2,os.SEEK_END)
	# f.truncate()
	f.write("\"")
	f.close()

# final+=')\"'
# final+=' % ('
# for(let key in quote){
# 	 final += `self.${key}, `
# }
# final+=')'
# console.log(final)
# // "<Hardware(maker='%s', price='%s', model='%s')>" % (self.name, self.fullname, self.password)
