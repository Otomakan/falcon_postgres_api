from ..models import User
from ..models import session


def validate_fields(model, data):
	table_name_l =  len(str(model.__table__))
	data = {"users.id":"lol",
			"users.name":"bob",
			"users.fullname":"Beltcher",
			"users.password":"BBKING",}

	for c in model.__table__.columns:
		str.subs
		if str(c) not in data and True:
			print("Hmmmm data not in table ")
			return False
			# raise Exception("There is a Missing key")
	return True
