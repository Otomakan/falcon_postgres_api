from . import Base
from sqlalchemy import Column, Integer, String,relationship

class QuoteField(object):
	""" MyTable Object Table"""
	def __init__(self, arg):
		super(MyTable, self).__init__()
		self.arg = arg
	phases = Column(String)
	switchBoardUpgradeIncluded = Column(Integer)
	switchBoardUpgradePrice = Column(Integer)
	numberOfCircuits = Column(String)
	numberOfSplitArrays = Column(Integer)
	panelOrientation = Column(String)
	numberOfStoreys = Column(String)
	raisedFrames = Column(String)
	raisedFramesPrice = Column(Integer)
	storeys = Column(String)
	roofType = Column(String)
	roofPitch = Column(String)
	inverterLocation = Column(String)
	adequateSiteAccess = Column(String)
	def __repr__(self):		return "<InstalationSpecefic(phases='%s', switchBoardUpgradeIncluded='%s', switchBoardUpgradePrice='%s', numberOfCircuits='%s', numberOfSplitArrays='%s', panelOrientation='%s', numberOfStoreys='%s', raisedFrames='%s', raisedFramesPrice='%s', storeys='%s', roofType='%s', roofPitch='%s', inverterLocation='%s', adequateSiteAccess='%s', "