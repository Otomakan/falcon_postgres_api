import json
import falcon

from ..models.user import User
from ..models import session


def see_all():
  final = {}
  for name, fullname in session.query(User.name, User.fullname):
    final[name] = fullname
  return final

  # def create_user(self, name, fullname,password) :
  #   session.add(User(name=name,fullname=fullname,password=password))   

class UsersResource(object):
    # def __init__(self,session):
    #   self.users_table = PostGresUsersTable(session=session)
      
    def on_get(self, req, resp):
        """Handles GET requests"""
        users = see_all()
        print(users)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = (json.dumps(users))
    def on_post(self, req, resp,dr):
        posted_data = json.loads(req.stream.read())
       	for key in posted_data:
       		print(key)
       		print(posted_data[key])
       	# with open('out.pdf', 'r') as file:
       	resp.stream = open('out.pdf', 'r')
       	resp.downloadable_as = 'out.pdf'        
       	resp.status = falcon.HTTP_200
  