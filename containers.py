def group(p):
	return Group(*p)
	
class  Group:
	grouptype = (int, str)
	def __init__(self, *args):
		for ele in args:
			assert isinstance (ele, self.grouptype), f"Type Error:Must be '{self.grouptype}' type"
		self.data = list(args)
		self.cur = 0
	
	@property	
	def isempty(self):
		if len(self.data) == 0:
			return True
		return False
		
	def positionfromid(self, i):
		for n,x in enumerate (self.data):
			if i == x.id:
				return n
		raise ValueError(f"{i} not found!!")
		
	def add(self, data):
		assert isinstance (data, self.grouptype), f"Type Error:Must be '{self.grouptype}' type"
		self.data.append(data)
		
	def remove (self, _id):
		for i,x in enumerate (self.data):
			if _id == x.id:
				del self.data[i]
				return
		raise ValueError(f"{_id} not found! ")

	def __getitem__(self, i):
		 for n,x in enumerate (self.data):
		 	if i == x.id:
		 		return self.data[n]
		
	def __iter__(self):
		return self
		
	def __repr__(self):
		name =str(type(self)).split(".")[-1].rstrip("'>")
		return f"{name}: << {' , '.join([str(x) for x in self.data])} >>"
		
	def __len__(self):
		return len(self.data)
		
	def __next__(self):
		if self.cur < len(self.data):
			item = self.data[self.cur]
			self.cur += 1
			return item
		else:
			raise StopIteration
	
#x = (1,23,5, "16")
#print (group(x))
#class StudentsIterator:
#		
#	def __init__(self, l):
#		self.students = l
#		self.cur= 0
#		
#	def __iter__(self):
#		return self
#		
#	def __next__(self):
#		if self.cur < len(self.students):
#			item = self.students[self.cur]
#			self.cur += 1
#			return item
#		else:
#			raise StopIteration 
#		

	

		
# = Students()
#x.add(1)
#x.add(2)
#x.add(5)
#for i in x:
#	print(i)

class NonTeachers():
	pass
	
class Subjects:
	pass
	
class PartPayments:
	pass