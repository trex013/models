from main import *
import sqlite3 as sq
class ArrayDT:
	@staticmethod
	def toArray(data):
		data = data.strip("[").strip("]").split(",")
		return data
		
	def __init__(self):
		self.element = list()
		
	def __conform__(self, protocol):
		if protocol is sq.PrepareProtocol:
			return str(self.element)
			
class Morel(ArrayDT):
	def __init__(self,**kwargs):
		super().__init__()
		self.element.append(kwargs)
		
class Column:
	def __init__(self, name, datatype=None, nullable=False, PK=False, **others):
		self.name = name
		self.datatype = datatype
		self.nullable = "NULL" if nullable else ""
		self.PK = "primary key" if PK else ""
		self.others = others
		
	def __str__(self):
		return f"{self.name} {self.datatype} {self.nullable} {self.PK}"
		
		
		
class Table:
	
	@staticmethod
	def create(tablename, cur, *cols):
		t = Table(tablename, cur, new = True)
		t.query.createtable(*cols)
		return t
		
	def __init__(self, name, cur, new = False):
	#	print(name, "exists:", Query.isTableExisting (name, cur))
		if not new:
			assert Query.isTableExisting (name, cur), f"The table '{name}' does not exist"
		self. query = Query(name, cur)
		
		

class Dbm:
	def __init__(self, db):
		self. conn = sq. connect (db+".db")
		self. table = None
		
	def openTable(self, tablename):
		self.table = Table(tablename, self.conn)
		return self.table
		
	def createTable (self, name, *cols):
		self.table = Table.create(name, self.conn, *cols)
		return self.table
		
	def test(self):
		print ("1....2")
		
	def __enter__(self, *args):
		return self
		
	def __exit__(self, *args):
		self. conn. commit()
		self. conn. close()
		self.conn = None
		
def string2list(strng):
	strng = strng.strip("[").strip("]")
	string2dict(strng)
	return strng.split(",")
	
def string2dict(s):
	s = s.strip("{").strip("}")
	s = s.split(',')
	s = { k.strip("'"):v for k,v in [ m.strip("'").split(":") for m in s ]}
	print(s)
	
#with Dbm("school") as dbm:
#	sn = Column("sn", datatype="int")
#	dbm.createTable("net", sn, Column ("scores", datatype="morel"))
#	_Table = {}
#	_Table["net"] = dbm.openTable("net")
#	_Table["Rex"] = dbm.openTable("Rex")
#	_Table["net"].query.insert([1, Morel(x = 5, y = 10)])
#	for table in _Table.values():
#		print(table.query.select.all())
#		
#	x = _Table["net"]
#	x.query.setRowFactory(True)
#	y = x.query.limit(1). select.all().fetchall()
#	print(tuple(y[0]))
#	
#	print(ArrayDT.toArray("[3,4,5,6]"))
	#x[0].query.insert((1,),(2,))
#	x[1].query.insert([1, "frank"])
#	for n in x:
#		print(n.query.select.all())
#	dbm.createTable("Rex", sn, Column("name", datatype="varchar"))
#	#dbm.table.query.insert([3, "TEzi"], [4, "TObi"])
#	dbm.table.query.where("sn=3").delete
#	print(dbm.table.query.select.all())
#	dbm.table.query.where("sn=4").update (name="Ada")

#	dbm.table.query.where("sn=4").delete
#	print(dict(x))
#	print(dbm.table.query.select.all())
#print((dbm.conn))