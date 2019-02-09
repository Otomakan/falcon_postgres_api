import json
import falcon

from ..models import User
from ..tables import UserTable
from ..models import session


class UsersRoute(object):
    def __init__(self):
      """Create an interface to interact with the User Table  """
      self.users_table = UserTable(session=session)
      
    def on_get(self, req, resp):
      """Handles User GET requests"""
      users = self.users_table.see_all()
      resp.body = json.dumps(users)
      resp.status = falcon.HTTP_200  # This is the default status
        
    def on_post(self, req, resp):
      """Handles User POST requests"""
      body = req.stream.read()
      if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                      'A valid JSON document is required.')

      posted_data = json.loads(body)	  
      resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
      resp.body = "Delete route"
      resp.status = falcon.HTTP_200

