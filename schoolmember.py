from datetime import date, datetime
from person import Person
from containers import Group



class SchoolMember(Person):
	__doa = None
	__class = None
	paymentD = None
	__department = None
	
	def __init__(self, **k):
		if "class_" in k:
			self.setClass = k["class_"]
		super ().__init__(**k)
	
	@property
	def pushout(self):
		new = dict(
			class_ = self.__class,
			doa = self.__doa
		)
		new.update(super().pushout)
		return new
		
	@classmethod
	def _m(cls):
		musthave= [x for x in dir(cls) if "__" not in x and "set" not in x and "full" not in x and "_m" not in x]
		musthave.append("class_")
		return musthave
		
	@property
	def doa(self):
		return self.__doa
		
	@doa.setter
	def setDOA(self, c):
		self.__doa = date.fromisoformat(c)
		
	@property
	def Class(self):
		return self.__class
		
	@Class.setter
	def setClass(self, c):
		self.__class = c
	
	@property
	def getPaymentRecord(self):
		if self.paymentD:
			pass
		return None
	
	@property	
	def yearsOfMembership(self):
		if self.__doa:
			currentyear = date.today().year
			acceptedyear = self.__doa.year
			return currentyear - acceptedyear
