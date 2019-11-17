import sqlite3 as  db
connection = db.connect("CrimeDataBase.db")
cursor = connection.cursor()



# cursor.execute('''CREATE TABLE Admin
# 					(
# 					 userName TEXT PRIMARY KEY,
# 					 password TEXT 
# 					)
# 				''')
# connection.commit()


cursor.execute('''CREATE TABLE Complaint
					(
					 complaintId INTEGER PRIMARY KEY AUTOINCREMENT, 
					 userName TEXT ,
					 password TEXT,
					 crimeType TEXT,
					 description TEXT,
					 latitude REAL,
					 longitude REAL
					)
				''')
connection.commit()


connection.close()