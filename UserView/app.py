from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, Response
import requests
import dbdata as db
from datetime import date
import os
from ServerSideEvents import push_data

app = Flask(__name__)

@app.route('/api/v1/user_signup', methods = ["POST", "GET", "DELETE", "PUT"])
def user_signup():
	if request.method == "POST":
		user_object = request.get_json()
		user_object["latitude"] = 12
		user_object["longitude"] = 72

		parameters = list()
		parameters.extend(["emailId"])
		
		print(user_object)
		if db.check_user_name_in_db(user_object, parameters):
			db.add_user_to_db(user_object)
			return jsonify({}), 201
		else:
			return jsonify({}), 400
	else:
		return jsonify({}), 405
	

@app.route('/api/v1/user_login', methods = ["POST", "GET", "DELETE", "PUT"])
def user_login():
	if request.method == "POST":
		user_object = request.get_json()
		parameters = list()
		parameters.extend(["emailId", "password"])
		
		if db.check_user_name_in_db(user_object, parameters):
			session["logged_in"] = True
			session["name"] = user_object["emailId"]
			return jsonify({}), 200
		else:
			return jsonify({}), 404
	
	else:
		return 405


@app.route("/api/v1/post_complaint", methods = ["GET", "POST", "DELETE", "PUT"])
def post_complaint():
	if request.method == "POST":
		complaint_object = request.get_json()
		
		today_date = date.today()
		today_date = today_date.strftime("%d-%m-%y")
		latiude = 12
		longitude = 72
		
		complaint_object["crimeDate"] = today_date
		complaint_object["latitude"] = latiude
		complaint_object["longitude"] = longitude
		
		if db.add_complaint_to_db(complaint_object):
			return jsonify({}), 200
		else:
			return jsonify(), 404
	else:
		return jsonify(), 405


@app.route("/homepage")
def homepage():
	return render_template("Index.html")

@app.route("/login_page")
def login_page():
	if not session.get('logged_in'):
		return render_template("Login.html")
	else:
		return render_template("Index.html")

@app.route("/signup_page")
def signup_page():
	return render_template("Signup.html")


@app.route("/user_logout")
def user_logout():
	session["logged_in"] = False
	return render_template("Login.html")

@app.route("/PostComplaint")
def PostComplaint():
	if not session.get('logged_in'):
		return render_template("Login.html")
	else:
		return render_template("PostComplaints.html")


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True, port = 5000)