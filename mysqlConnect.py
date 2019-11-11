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
		return "Record has been created"
		
	def deleteRecord(self,table,attribute):	
		sql = "delete from "+table+" where "+attribute
		self.dbcursor.execute(sql)
		self.db.commit()
		return "Waypoints has been deleted"
		
		
		
	def checkIfRecordExists(self,table,attribute):
		sql = "select * from "+table+" where "+attribute
		self.dbcursor.execute(sql)
		result = self.dbcursor.fetchall()
		if result:
			return True
		else:
			return False
			
# ~ sql = mySql("robot","Pass4you","robot")
# ~ attributes =  [["latitude","47.22133"],["longitude", "8.222311"],["homebase", False]]
# ~ value = sql.createRecord("waypoints", attributes)
# ~ value = sql.selectRecord("waypoints", "homebase=true")

# ~ attributes = "wp_number"
# ~ value = sql.deleteRecord("waypoints", attributes)


# ~ print (value)

