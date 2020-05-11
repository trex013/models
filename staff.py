from schoolmember import SchoolMember
from containers import Group 

class Staff(SchoolMember):
	Salary = None
	PaymentD = None

	
class Teachers(Group):
	def __init__(self, *args):
		self.grouptype = Teacher
		super().__init__(*args)
		
	def findby(property, value):
		if property =="class":
			for t in self.data:
				if value==t.Class:
					return t
			raise IndexError("No Match found!!")
	
	
class Teacher(Staff):
	def __init__(self, **d):
		super().__init__(**d)
	
class NTeachers(Group):
	def __init__(self, *args):
		self.grouptype = NTeacher
		super().__init__(*args)
	
	
	
class NTeacher(Staff):
	#setClass = None
	def __init__(self, **k):
		super().__init__(**k)
		
	def setClass(self):
		raise ValueError ("Cannot Set A class of Nteacher")
		return None
	

	
if __name__=="__main__":
	x = NTeacher(id=5, name="Treasure O")
	x.setDOA = "2014-01-01"
	x.setClass = 55
	print(x)
	print(x. _m())