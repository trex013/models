from person_ext import SchoolMember
from containers import Group 

class Staff(SchoolMember):
	Salary = None
	
class Teachers(Group):
	def __init__(self, *args):
		self.grouptype = Teacher
		super().__init__(*args)
	
	
class Teacher(Staff):
	pass
	
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