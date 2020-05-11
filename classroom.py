from person import Person
from datetime import date
from staff import *
from student import Student, Students

class Class:
	__title=None
	__nextClass =None
	__prevClass=None
	students = None
	teacher = None
	doneExam = False
	
	def __init__(self, name, nclass=None, pclass = None):
		self.name = name
		self.__nextClass = nclass
		self.__prevClass = pclass
		self.register = Register ()
	
	def loadup(self, students, teacher, attendance=None):
		assert isinstance (students, Students) and isinstance (teacher, (Teacher, Teachers)), "Wrongly Typed parameters"
		self.students = students
		self.teacher = teacher
		self.register.loadup(students, attendance)
		
	def addStudent(self, student):
		self.students.add(student)
		self.register.addmember(student)
		
	def totalStudents(self):
		if self.students:
			return len(self.students)
		
	def withdraw (stdId):
		self.students.remove(stdId)
		
	def positions(self):
		studs = dict()
		if doneExam:
			for student in self.students:
				studs[student.report.average] = student
				
			avgs = list(studs.keys())
			avgs.sort()
			
			# Adds the suffix
			def suffix(x):
				e = x[-1]
				if e == "1":
					return "st"
				if e == "2":
					return "nd"
				if e == "3":
					return "rd"
				if e == "4" or e=="5"\
					or e =="6" or e=="7"\
				 	or e == "8" or e=="9" or e=="0":
					return "th"
					
			# removes repeated values 
			# for ranking purposes
			ranking = set(avgs)
			rankingdict = {}
			c = 1
			for d in ranking:
				use = str(c)
				rankingdict[d] = f"{use}{suffix(x)}"
				c += 1
			
			out = dict()
			for avgs in studs:
				out[rankingdict[avgs]] = studs[avgs]
				
			return out
				
	def __repr__(self):
		if self.students == None:
			return f"Class: {self.name}"
			
		out = f"Class: {self.name}\n"
		if isinstance (self.teacher, Teachers):
			out += f"Teachers: {' and '.join([x.name for x in self.teacher])}\n"
		else:
			out += f"Teacher: {self.teacher.name}\n"
		out += "Students:\n"
		for n, stud in enumerate (self.students):
			out += f"{n+1}.\t{stud.name}\n"
		return out
			
			
class Register:
	members = None
	data = {}
	def loadup(self, member, attendance = None):
		self.members = member
		if attendance:
			self.noattended = attendance
		else:
			self.noattended = [0]*len(self.members)
		self.data = zip(self.members, self.noattended)
		self.data = dict(self.data)
		print(self.data)
		
	def addmember(self, ind, attended= 0):
		self.members.add(ind)
		self.noattended.append(attended)
		
	def setAttended(self, _id, data):
		self.noattended[self.members.positionfromid(_id)] = data
		
	def __repr__(self):
		out = ""
		for i,n in enumerate (self.members):
			out += f"{i+1}.\t{n.name}\t{self.noattended[i]}\n"
			
		return out


if __name__=="__main__":
	from datetime import date
	#name = Name.setfromstring("Obisike Treasure")
#	#name.changename("firstname", "Treasure")
#	name.changeothername="Chime"
#	print(name)
#	class D(SchoolMember):
#		def __init__(self, name, dob):
#			self.setid= 1
#			self.setname = name
#			self.setdob = dob
#			self.setDOA = "2000-02-11"
			#self.m = [x for x in dir(self) if "__" not in x]
			
				
	#x = D("Treasure Obisike", "1999-01-15")
	#Class("Lvl1")
	#x.Class.loadup(Students(**[Student(id=n, name=f"test{n}") for n in range(6)]), Teacher(id=2, name= "Patrick"))
	print(x.Class)
	
	print(x)
			