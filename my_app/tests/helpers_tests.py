import unittest
from ..helpers import validate_fields
from ..models import User
from ..models import session

class ValidateFieldsTest(unittest.TestCase):
	"""Test  for the field validation """
	def test(self):
			self.assertEqual(validate_fields(
				{"users.id":"lol",
				"users.name":"bob",
				"users.fullname":"Beltcher",
				"users.password":"BBKING",},
				User

				),True)
		