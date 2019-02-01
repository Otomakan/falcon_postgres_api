from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://username:bloblo@localhost/falcon_api_quote_generator', echo=True)
# engine.connect()

Base = declarative_base()
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
# Base.metadata.create_all(engine)
# print(User.name)
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)

our_user =session.query(User).first()
print(our_user)

session.commit()