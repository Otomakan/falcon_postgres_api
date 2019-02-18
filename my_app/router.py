import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.getcwd())

import falcon
import json

from .helpers import validate_fields

from .routes.users import UsersRoute
from .models import session,User
from sqlalchemy.ext.declarative import declarative_base


app = falcon.API()

# Resources are represented by long-lived class instances
users = UsersRoute()
 
# things will handle all requests to the '/things' URL path
app.add_route('/users', users)
