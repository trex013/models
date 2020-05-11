from datetime import datetime
from containers import Group
#import time

class Payment:
	def __init__(self, time, amt, purpose=None):
		print(time)
		self.__time=datetime.fromtimestamp(time)
		self.__amt = amt
		self.purpose = purpose
	
	@property	
	def amt(self):
		return self.__amt
		
	@property
	def time(self):
		return self.__time
		
	def __repr__(self):
		return f"Time: {self.__time}, Amt: {self.__amt}"
		
class Paid(Group):
	def __init__(self, *args):
		self.grouptype = Payment
		super().__init__(*args)
	
class PaymentDetail:
	paid = Paid()
	payAPI = True
	def __init__(self, salary = None, lesson=None, schoolfee= None, transport=None, incentive=None):
		self.salary = salary
		self.lesson = lesson
		self.schoolfee = schoolfee
		self.transport = transport
		self.incentives = incentive
		self.total = self.totaldeptamt()
	
	def totaldeptamt(self):
		total = None
		if self.salary:
			total = self.salary
			if self.incentives:
				total+=self.incentives
		else:
			total = self.schoolfee
			if self.transport:
				total+=self.transport
			if self.lesson:
				total+=self.lesson
			
		return total
	
	@property
	def totalpaid(self):
		return sum([paid.amt for paid in self.paid])
		
	@property
	def dept(self):
		return self.total - self.totalpaid
		
		
	def pay(self, amt):
		if self.payAPI:
			time = datetime.now(). timestamp ()
			self.paid.add(Payment (time, amt))
		
	def __repr__(self):
		out = ""
		for x in self.paid:
			out += f"{x}\n"
			
		return out
		
if __name__=="__main__":
	x = PaymentDetail(schoolfee=15000, lesson=500)
	x.pay(15000)
#	time.sleep(10)
	x.pay(50000)
	
	print(x.dept)