from datetime import date

# Name Class
class Name:
	__firstname = None
	__othername = None
	__surname = None
	
	@staticmethod
	def setfromstring(string):
		name = string.split(" ")
		while len(name)< 3:
			name.append(None)
		return Name.set(
			surname=name[0], 
			firstname=name[1], 
			othername=name[2]
		)
	

	def set(firstname=None, surname=None, othername=None):
		name = Name()
		name.changefirstname=firstname
		name.changeothername=othername
		name.changesurname=surname
		return name
		
	@property
	def firstname(self):
		return self.__firstname
		
	@firstname.setter
	def changefirstname(self, x):
		self.__firstname = x
		
	@property
	def othername(self):
		return self.__othername
		
	@othername.setter
	def changeothername(self, x):
		self.__othername = x
		
	@property
	def surname(self):
		return self.__othername
		
	@surname.setter
	def changesurname(self, x):
		self.__surname = x
	
	def changename(self, ntype, newname):
		ntype = "change"+ntype
		setattr(self, ntype, newname)
		
	@staticmethod
	def emp(name):
		if name:
			return name.capitalize()
		return " "
	
	@property	
	def getfullname (self):
		return str(self)
		
	def __repr__(self):
		name = (
			self.__surname, 
			self.__firstname, 
			self.__othername
		)
		name = list(map(Name.emp, name ))
		return f"{name[0]} {name[1]} {name[2]}"
	
# Person Class
class Person:
	__id = None
	height=None
	weight=None
	certification=None
	__country = None
	__state = None
	__name = None
	__dob = None
	__lga = None
	parent = None
	disability = None
	address = None
	
	@property
	def dob(self):
		return self.__dob
		
	@dob.setter
	def setdob(self, d ):
		self.__dob = date.fromisoformat(d)
		
	@property
	def lga(self):
		return self.__lga
		
	@lga.setter
	def setlga(self, lga):
		self.__lga = lga
		
	@property
	def country(self):
		return self.__country
		
	@country.setter
	def setcountry(self, name):
		self.__country = name
		
	@property
	def state(self):
		return self.__state
		
	@state.setter
	def setstate(self, state):
		self.__state = state
		
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def setname(self, name):
		self.__name = Name.setfromstring(name)
		
	@property
	def id(self):
		return self.__id
		
	@id.setter
	def setid(self, id):
		self.__id = id
		
		
		
	def __init__(self, **k):
	#	assert self.__id, "No id"
		assert ("name" in k or "surname" in k) and \
		"id" in k, "No name or id passed"
		if k:
			if "id" in k:
				self.__id = k["id"]
				
			if "name" in k:
				self.__name = Name.setfromstring(
					k["name"]
				)
			if "surname" in k and "firstname" in k:
				self.__name = Name.set(
					surname=k["surname"],
					firstname=k["firstname"]
				)
				if "othername" in k:
					self.__name.changeothername = k[" othername" ]
					
			if "dateofbirth" in k:
				self.dob = date.fromisoformat(k["dateofbirth"])
				
			if "dob" in k:
				self.__dob = date.fromisoformat(k["dob"])
				
			if "country" in k:
				self.__country = k["country"]
				
			if "state" in k:
				self.__state = k["state"]
				
			if "lga" in k:
				self.__lga = k["lga"]
	
	@property
	def age(self):
		if self.dob:
			currentyear = date.today().year
			birthyear = self.dob.year
			return currentyear - birthyear
	
	@property
	def isbirthday(self):
		if self.dob:
			currentmonth = date.today().month
			currentday = date.today().day
			birthmonth = self.dob.month
			birthday = self.dob.day
			if currentmonth == birthmonth:
				if currentday == birthday:
					return True
					
		return False
		
	@property	
	def fullname(self):
		if self.name:
			return self.name.getfullname
		return None
		
	def __repr__(self):
		out = f""" Title: {str(self.__class__).split('.')[-1].rstrip("'>" )}\n""" 
		out +="-"*20
		for x in [x for x in dir(self) if "__" not in x and "set" not in x and "full" not in x and "_" not in x]:
			out+= " \n{}: {}".format(
				x.capitalize(), getattr(self,x)
			)
		return out
	#	if not self.age:
#			self.age = None
#		return f"Name: {self.name}\
#		\nDate of Birth: {self.dob}\
#		\nAge: {self.age}\
#		\nHeight: {self.height}\
#		\nWeight: {self.weight}\
#		\nCountry of Origin: {self.country}\
#		\nState of Origin: {self.state}\
#		\nLGA: {self.lga}\
#		"
	