import sqlite3 as  db
connection = db.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE User
					(userName TEXT,
					 address TEXT,
					 place TEXT,
					 latitude REAL,
					 longitude REAL,
					 state TEXT,
					 emailId TEXT,
					 password TEXT,
					 PRIMARY KEY(emailId)
					)
				''')
connection.commit()

# cursor.execute('''CREATE TABLE Property
# 					(pid INTEGER PRIMARY KEY AUTOINCREMENT,
# 					 image TEXT,
# 					 locality TEXT,
# 					 latitude REAL,
# 					 longitude REAL,
# 					 noOfBedRooms INTEGER,
# 					 rentAmount REAL,
# 					 description TEXT,
# 					 landlordEmailId TEXT,
# 					 rating INTEGER,
# 					 numberOfPeopleRated INTEGER
# 					)
# 				''')
# connection.commit()




# cursor.execute('''CREATE TABLE PropertyAssignment
# 					(pid INTEGER PRIMARY KEY,
# 					 tenantEmailId TEXT,
# 					 rentRemainderDate DATE,
# 					 FOREIGN KEY(pid) REFERENCES Property(pid),
# 					 FOREIGN KEY(tenantEmailId) REFERENCES User(emailId)
# 					)
# 				''')
# connection.commit()

# cursor.execute('''CREATE TABLE Payment
# 					(pid INTEGER,
# 					 tenantEmailId TEXT,
# 					 paymentDate DATE,
# 					 paymentMode TEXT,
# 					 amount TEXT,
# 					 PRIMARY KEY(pid, tenantEmailId, paymentDate),
# 					 FOREIGN KEY(pid) REFERENCES Property(pid),
# 					 FOREIGN KEY(tenantEmailId) REFERENCES User(emailId)
# 					)
# 				''')
# connection.commit()


# cursor.execute('''CREATE TABLE Issue
# 					(
# 					 id INTEGER PRIMARY KEY AUTOINCREMENT,
# 					 reporterMailId TEXT,
# 					 issueDate date,
# 					 description TEXT,
# 					 category TEXT,
# 					 contactPersonMailId TEXT,
# 					 status TEXT,
# 					 customerStatus	TEXT,
# 					 contactPersonStatus TEXT,
# 					 FOREIGN KEY(reporterMailId) references User(emailId), 
# 					 FOREIGN KEY(contactPersonMailId) references ContactPerson(emailId)
# 					)
# 				''')
# connection.commit()


# connection.close()