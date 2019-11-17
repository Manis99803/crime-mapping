from datetime import date
import requests
import sqlite3


# import hashlib
# hashlib.sha1((user['password']).encode()).hexdigest()


# Function for adding the user name to database
# Parameters : user_dictionary
def add_user_to_db(user_data):
	connection_state = sqlite3.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection_state.cursor()
	cursor.execute('''INSERT INTO User (userName, address, place, latitude, longitude, state, emailId, password) 
		VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
		[user_data["userName"], user_data["address"], user_data["place"], 
		user_data["latitude"], user_data["longitude"],user_data["state"], user_data["emailId"], user_data["password"]])
	connection_state.commit()
	connection_state.close()
	

# Function for checking if the user name exist in the db or no:
# Parameter : 
#	user: user_data
# 	key : a list of parameters which can be used for checking if the user exist in the database.
# returns True : If user exist in the db
# returns False : If the user does not exist in the db.
def check_user_name_in_db(user_data, key):
	connection_state = sqlite3.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection_state.cursor()
	
	query_parameter = [user_data[parameter] for parameter in key]
	
	parameter_length = len(key)
	query_clause = str()
	
	for i in range(parameter_length):
		if i != parameter_length - 1:
			query_clause += key[i] + " = ? and "
		else:
			query_clause += key[i] + " = ? "
	
	query = "SELECT * from User where " + query_clause
	cursor.execute(query, query_parameter)
	user_data = cursor.fetchall()
	connection_state.commit()
	connection_state.close()
	
	if user_data != None:
		return True
	if len(user_data) != 0:
		return True
	return False


def add_complaint_to_db(complaint_object):
	
	requests.post("http://127.0.0.1:5001/api/v1/increment_complaint_counter")
	connection = sqlite3.connect("/home/manish/manish/Manish/Documents/7th_Sem/Web-Tech/project/crime-mapping/CrimeDataBase.db")
	cursor = connection.cursor()

	query = "INSERT INTO Complaint (userName, crimeType, description, latitude, longitude, location, crimeDate) VALUES (?, ?, ?, ?, ?, ?, ?)"
	cursor.execute(query, [complaint_object["name"], complaint_object["crimeType"], complaint_object["description"], 
				complaint_object["latitude"], complaint_object["longitude"], complaint_object["location"], complaint_object["crimeDate"]])

	connection.commit()
	connection.close()
	
	return True