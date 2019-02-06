import json
import falcon

from ..models import User
from ..tables import UserTable
from ..models import session



class UsersResource(object):
    def __init__(self,session):
        self.users_table = UserTable(session=session)
      
    def on_get(self, req, resp):
        """Handles GET requests"""
        users = self.users_table.see_all()
        print(users)
        resp.body = (json.dumps(users))
        resp.status = falcon.HTTP_200  # This is the default status
        
    def on_post(self, req, resp,dr):
        posted_data = json.loads(req.stream.read())
       	for key in posted_data:
       		print(key)
       		print(posted_data[key])
       	# with open('out.pdf', 'r') as file:
       	resp.stream = open('out.pdf', 'r')
       	resp.downloadable_as = 'out.pdf'        
       	resp.status = falcon.HTTP_200
  