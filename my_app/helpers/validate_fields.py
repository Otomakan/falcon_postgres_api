from ..models import User
from ..models import session


def validate_fields():
	data = {"usersid":"lol",
			"users.name":"bob",
			"users.fullname":"Beltcher",
			"users.password":"BBKING",}
	for c in User.__table__.columns:
		if str(c) not in data:
			raise Exception("There is a Missing key")
	
	print(type(User))