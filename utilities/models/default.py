from . import Base
from sqlalchemy import Column, Integer, String


class TableName(Base):
	__tablename__ = TableName.lowerCase()
	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)
	def __repr__(self):
		 return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
