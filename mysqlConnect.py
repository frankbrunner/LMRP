import mysql.connector

class mySql():
	def __init__(self,User,Passwd,Database):
		
		self.db = mysql.connector.connect(
			host="localhost",
			user=str(User),
			passwd=str(Passwd),
			database=str(Database)
		)
		self.dbcursor = self.db.cursor()		

	def createTable(self,tablename,rows):
		sql = "create table "
		sql = sql + str(tablename)
		"""definitino of rows"""
		sql = sql + "(id int auto_increment primary key,"
		if type(rows) == str:
			sql = sql + str(rows)+","
		else:
			for item in rows:
				sql = sql + str(item)+","
		sql = sql + 'create_at timestamp default current_timestamp)'
		self.dbcursor.execute(sql)

	def createRecord(self,table,attributes):
		sql= "insert into " + table+" ("
		sqlTail = ") values ("
		values = []
		for item in attributes:
			sql = sql + str(item[0])+","
			values.append(item[1])
			sqlTail = sqlTail + "%s,"
		sql = sql[0:-1]
		sqlTail = sqlTail[0:-1] +")"
		values = (values)
		sql= sql + sqlTail
		print (sql)
		self.dbcursor.execute(sql, values)
		self.db.commit()
	
	def selectRecord(self,table,attribute):
		sql = "select * from "+table+" where "+attribute
		print (sql)
		self.dbcursor.execute(sql)
		myresult = self.dbcursor.fetchall()
		print (myresult)
		if myresult:
			return True
		else:
			return False
			
sql = mySql("robot","Pass4you","robot")
attributes =  [["latitude","47.22133"],["longitude", "8.222311"],["homebase", True]]
sql.createRecord("waypoints", attributes)
value = sql.selectRecord("waypoints", "homebase=true")
print (value)

