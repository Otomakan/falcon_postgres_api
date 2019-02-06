from ..models.installation_specific import User
from sqlalchemy import exc

class UserTable:
  def __init__(self, session):
    self.session = session
  def create(self,details):
    try:
      db_users = InstallationSpecific(**details)
      self.session.add(db_users)
    except exc.SQLAlchemyError as e:
      raise e 
    return db_users
   def delete(self, details):


   def see_all(self)
    	final = {}
	  	for name, fullname in session.query(User.name, User.fullname):
	    	final[name] = fullname
	  	return final

