import sqlite3 as sql

number_of_complaints = 0
notification_sent_for_complaints = 0

def increment_complaints_count():
	global number_of_complaints
	number_of_complaints += 1
	print(number_of_complaints)

def push_data():
    global number_of_complaints
    global notification_sent_for_complaints
    print(number_of_complaints, notification_sent_for_complaints)
    
    if number_of_complaints != notification_sent_for_complaints:
        notification_sent_for_complaints += 1
        yield 'data: %s\n\n' % 'Number Of Complaints Posted: {0}'.format(notification_sent_for_complaints)


def check_user_in_db(user_object):
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection.cursor()
	
	query = "SELECT userName FROM Admin where userName = ? and password = ?"
	cursor.execute(query, [user_object["name"], user_object["password"]])

	db_user = cursor.fetchone()
	if db_user == None:
		return False
	return True

def get_data_for_crime_type(table_name):
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	connection.row_factory = sql.Row
	cursor = connection.cursor()
	
	query = ('SELECT crimeHeading,Latitude,Longitude,articleLink,crimeDate,crimeLocation,TableName FROM ' + table_name)
	cursor.execute(query)
	crime_data = cursor.fetchall()
	
	return crime_data


def get_crime_wise_frequency_distribution(table_name):
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	connection.row_factory=sql.Row
	cursor = connection.cursor()
	
	query = "SELECT * FROM " + table_name
	cursor.execute(query)
	frequency_data = cursor.fetchall()

	return frequency_data


def get_graph_data_for_crime_type(table_name):
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	connection.row_factory = sql.Row
	cursor = connection.cursor()
	
	query = "SELECT Location,Frequency,crimeType FROM " + table_name
	cursor.execute(query)
	graph_data = cursor.fetchall()

	return graph_data

def add_complaint_to_db(complaint_object):
	global number_of_complaints

	print(complaint_object)
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection.cursor()

	query = "INSERT INTO Complaint (userName, crimeType, description, latitude, longitude, location, crimeDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
	cursor.execute(query, [complaint_object["name"], complaint_object["crimeType"], complaint_object["description"], 
				complaint_object["latitude"], complaint_object["longitude"], complaint_object["location"], complaint_object["crimeDate"]])

	number_of_complaints += 1
	connection.commit()
	connection.close()
	
	return True

def get_complaints_data_from_db():
	connection = sql.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection.cursor()

	query = "SELECT * FROM Complaint"
	cursor.execute(query)

	db_complaint_data = cursor.fetchall()	
	complaint_data_board = []

	for complaint_details in db_complaint_data:
		complaint_data = dict()
		complaint_data["name"] = complaint_details[1]
		complaint_data["crimeType"] = complaint_details[2]
		complaint_data["description"] = complaint_details[3]
		complaint_data["latitude"] = complaint_details[4]
		complaint_data["longitude"] = complaint_details[5]
		complaint_data["location"] = complaint_details[6]
		complaint_data["crimeDate"] = complaint_details[7]
		complaint_data_board.append(complaint_data)

	print(complaint_data_board)
	return complaint_data_board

