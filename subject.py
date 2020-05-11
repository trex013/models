from containers import Group

class Subject:
	def __init__(self, _id=None, name=None, score=None):
		self.name = name
		self.__id = _id
		self.__score = None
		
	@property
	def id(self):
		return self.__id
	
	@id.setter	
	def setId(self, s):
		self.__id = s
		
	@property
	def score(self):
		return self.__score
	
	@score.setter	
	def setScore(self, s):
		self.__score = s
		
	@property
	def average (self):
		if isinstance (self.__score, (list, tuple)):
			pass
			
	@property
	def isexamtaken(self):
		if self.__score:
			return True		
			
	@property
	def grade(self):
		x=self.score
		if x>=70:
			return "A"
		if 60 <=x<=69:
			return "B"
		if 50<=x<=59:
			return "C"
		if 40<=x<=49:
			return "D"
		if 30<=x<=39:
			return "E"
		if x<=29:
			return "F"
			
	
class Subjects(Group):
	def __init__(self, *a):
		self.grouptype=Subject
		super().__init__(*a)
		
	@property
	def average (self):
		avgs = [x. average for x in self. data]
		return sum(avgs)/len(self.data)
		
	def find(self, name):
		for sub in self.data:
			if name.lower() == sub.name.lower():
				return sub
		
	def hasexamfinished(self):
		for sub in self.data:
			if not sub.isexamtaken:
				return False
		return True
				
	
if __name__=="__main__":
	print("Ok!")
	math = Subject(_id = 2,name="maths")
	math.setScore = 100
	print(math.grade)