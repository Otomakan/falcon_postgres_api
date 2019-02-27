import json, falcon

from ..models import NAME
from ..tables import NAMETable
from ..models import session


class NAMEsRoute(object):
    def __init__(self):
      """Create an interface to interact with the User Table  """
      self.names_table = NAMETable(session=session)
      
    def on_get(self, req, resp):
      """Handles NAME GET requests"""
      names = self.names_table.see_all()
      resp.body = json.dumps(names)
      resp.status = falcon.HTTP_200  # This is the default status
        
    def on_post(self, req, resp):
      """Handles NAME POST requests"""
      body = req.stream.read()
      if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                      'A valid JSON document is required.')

      posted_data = json.loads(body)	  
      resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
      resp.body = "Delete route"
      resp.status = falcon.HTTP_200

