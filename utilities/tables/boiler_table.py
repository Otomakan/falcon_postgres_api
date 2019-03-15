from ..models.name import NAME
from sqlalchemy import exc


class NAME:
  def __init__(self, session):
    self.session = session

  def find(self, col_name, info):
    query_filter  = {col_name: info}
    return self.session.query(NAME).filter_by(**query_filter)

  def add(self,details):
    try:
      db_name = NAME(**details)
      self.session.add(db_name)
    except exc.SQLAlchemyError as e:
      raise e 

    return db_name
  def delete(self, col_name, info):

    return
  def update(self, col_name, info):
    return