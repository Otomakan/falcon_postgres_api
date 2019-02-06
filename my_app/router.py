import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.getcwd())

import falcon
import json



from .routes.users import UsersResource
from .models import session,User
from sqlalchemy.ext.declarative import declarative_base


app = falcon.API()

# Resources are represented by long-lived class instances
users = UsersResource()

# things will handle all requests to the '/things' URL path
app.add_route('/users', users)
