def test1():
	args = {"email":'lol',"password":'bloblo', "extra":'hello'}
	test2(args)


def test2(email, *args, **kwargs):
	print(email)

test1()