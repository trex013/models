from schoolmember import SchoolMember
from containers import Group
from subject import *

class ReportBook:
	def __init__(self, subjects=Subjects()):
		self.__subjects = subjects
		self.robocomment
		
	def loadup(self, subjects=None, score=None):
		self.__subjects = subjects
		
		
	def fill_in(self, subject, score=None):
		subject.setScore = score
		self.__subjects.add(subject)
		
	def enterScores(self, **scores):
		for sub, score in iter(scores.items()):
			self.enterScore(sub, score)
			
	def enterScore(self, subject, score):
		self.__subjects.find(subject).setScore = score
		
	def comment(self, clsavg):
		self.comment = clsavg
		
	def robocomment(self):
		if self.__subjects.hasexamfinished:
			self.comment = "Well"
		else:
			self.comment = None
		
	
class Student(SchoolMember):
	reportBook = None
	def __init__(self, **kwargs ):
		for key in kwargs:
			assert key in SchoolMember._m(),f"Incorrect keyword--{key}"
		super().__init__(**kwargs)
		self.siblings = Students()
		
	def addSiblings(*args):
		for s in args:
			self.siblings.add(s)
			
	def __repr__(self):
		return f"Student id: {self.id} Student Name: {self.name}"
		
		
class Students (Group):
	def __init__(self, *args):
		self.grouptype = Student	
		super().__init__(*args)	
		
		
if __name__=="__main__":
	bag = Students()
	for n in range(6):
		bag.add(Student (id=n, name = f"stud{n}"))

	bag.remove(2)	
	for x in bag:
		print(x.name)
	
#print(Student(id = 3, name= "Trex Obisike Chimeziri", per= 5))
	