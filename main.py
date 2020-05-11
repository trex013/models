
from staff import *
from student import *
from classroom import *
from subject import *
from payment import *
from database_tables import *
from datetime import date, datetime


class LoadStaff:
	def loadteachers(self):
		teachers = TeachersDB. query. all()
		for teach in teachers:
		#	p = [dict(time= 123444, amt=5000)]
			p = Paid.query.where(f"id  = {teach.id}").all()
			self.loadoneteacher(teach, p)
		
	def loadoneteacher(self, staffdet, payments):
		t = Teacher(**staffdet)
		paydet = PaymentDetail(salary=staffdet["salary"])
		for x in payments:
			paydet.paid.add(Payment(**x))
		t.paymentD = paydet
		self.staffs[0].add(t)
		
	def loadNteachers(self):
		Nteachers = NTeachersDB. query. all()
		for nteach in Nteachers:
		#	p = [dict(time= 123444, amt=5000)]
			p = Paid.query.where(f"id  = {nteach.id}").all()
			self.loadoneNteacher(nteach, p)
		
	def loadoneNteacher(self, staffdet, payments):
		t = NTeacher(**staffdet)
		paydet = PaymentDetail(salary=staffdet["salary"])
		for x in payments:
			paydet.paid.add(Payment(**x))
		
		t.paymentD = paydet
		self.staffs[1].add(t)
		
class LoadClasses:
	def findClass(self, clsname):
		x = self.clsnames.index(clsname)
		return self.clsdb[x]
		
	def loadClasses(self):
		# List of all the tables to access
		self.clsdb = [
			Class1, Class2, 
			Class3, Class4,
			Class5, Class6
		]
		
		clsSubjects = [
			SubjectC1, SubjectC2,
			SubjectC3, SubjectC4, 
			SubjectC5, SubjectC6
		]
		
		clsAttendance = [
			AttendanceC1, AttendanceC2,
			AttendanceC3, AttendanceC4,
			AttendanceC5, AttendanceC6
		]
		
		clspaymentD = [
			PDC1, PDC2,
			PDC3, PDC4,
			PDC5, PDC6
		]
		
		# Gets all the students data from the 
		# DB Tables listed above
		clsdatas = ( (cls.query.all(), subjs.query.all()) for cls, subjs in (self.clsdb, clsSubjects) )
		
		attenddata = ( att.query.all() for att in clsAttendance )
		
		paymentdata = ( att.query.all() for att in clspaymentD )
		
		# Gets the string clsname from the sqlachemy model
		self.clsnames = [clsname.name for clsname in self.clsdb]
		cnt = 0
		
		for clsdata, clsSub in clsdatas:
			self.loadClass(self.clsnames[cnt], clsdata, clsSub, next(attenddata), next(paymentdata))
			cnt += 1
		
	def loadClass(
		self,name, clsdata, listsub, 
		attendance, payD
	):
		
		# Adds the students from the self.clsdb
		s = Students()
		cnt = 0
		for data in clsdata:
			st = Student (**data)
			
			# Creates the payment details
			l,t = None,None
			if payD[cnt]["lesson" ]:
				l = payD[cnt]["lesson"]
			if payD[cnt]["transport"]:
				t = payD[cnt]["transport"]
			
			paydet = paymentD(schoolfee=self.schoolfee, lesson=l, transport=t)
			
			# Adds the paid transactions
			payments = Paid.query.where(f"id  = {payD[cnt].id}").all()
			for x in payments:
				paydet.paid.add(Payment(*x))
			
			# Adds the subjects to the list of subjects
			subj = Subjects()
			for sub in listsub:
				subj.add(**sub)
			
			
			# Adds Payments Details, Report Book
			# to the student and then adds the 
			# student to the list of students
			st.paymentD = paydet
			st.reportBook.loadup(subj)
			s.add(st)
			
		# creates the class and stores it
		self.classes[name] = Class(name=name)
		self.classes[name].loadup(
			students=s, 
			teacher=staffs[0].findby("class", name),
			attendance=attendance
		)
		
class School(LoadStaff, LoadClasses):
	name = None
	classes = {}
	staffs = (Teachers(), NTeachers())
	
	
	def __init__(self):
		# Load up the staffs
		self.loadStaffs()
		
		# load up the classes
		self.loadClasses()
		
	# loading up staffs
	def loadStaffs(self):
		self.loadteachers()
		self.loadNteachers()
		
	def registerpupil(self, _class, **pupildetail):
		self.classes[_class].addStudent(Student(**pupildetails))
		self.findClassDB(_class)(**pupildetails)
		#Commit it to db later
		
	def withdrawStudent(self, _class, studentId):
		self.classes[_class].withdraw(studentId)
		self.findClassDB(_class).delete().where("id = {studentId}")
		
	def payfee(self, _class, studid, amt):
		self.classes[_class].students[studid].p
		