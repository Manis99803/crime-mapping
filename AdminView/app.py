from flask import Flask, render_template, request, jsonify, session, Response
from datetime import date
import dbdata as db
import os

app=Flask('__name__')

# API codes
@app.route("/api/v1/admin_login", methods = ["GET", "POST", "DELETE", "PUT"])
def admin_login():
	if request.method == "POST":
		user_object = request.get_json()
		if db.check_user_in_db(user_object):
			session["logged_in"] = True
			session["name"] = user_object["name"]
			return jsonify({}), 200
		else:
			return jsonify(), 404
	else:
		return jsonify(), 405


@app.route("/api/v1/increment_complaint_counter", methods = ["POST", "GET", "DELETE", "PUT"])
def increment_complaint_counter():
	if request.method == "POST":
		db.increment_complaints_count()
		return jsonify({}), 200
	else:
		return jsonify(), 405

# Function which returns the crimeheading, latiude , longitude , article link, When a particular crime type is choosen(It gets all the entries 
# for a particular crime type)
@app.route("/DataView",methods=["POST","GET"])
def DataView():
	if request.method == 'POST':
		table_name=request.form['select']
	
	crime_data = db.get_data_for_crime_type(table_name)
	return render_template("HomePage.html", rows = crime_data)


# Returns the crime count area wise when a particular crime is selected
@app.route("/FrequencyDistribution",methods=["POST","GET"])
def FrequencyDistribution():
	if request.method == 'POST':
		table_name = request.form['select']
	
	frequency_data = db.get_crime_wise_frequency_distribution(table_name)
	return render_template("Frequency.html", rows = frequency_data)


# Gets bar graph for the selected crime type [ X axis : Area Y axix : Count]
@app.route("/GraphVisualization",methods=["POST","GET"])
def GraphVisualization():
	if request.method == 'POST':
		table_name = request.form['select']
	
	graph_data = db.get_graph_data_for_crime_type(table_name)
	return render_template("Graph.html",rows = graph_data)


#provide SSE stream to the web browser
@app.route('/listensForPushes')
def stream():
	if session.get("logged_in"):
		return Response(db.push_data(), mimetype="text/event-stream")

@app.route("/getData")
def getData():
	return render_template("HomePage.html")

@app.route("/login_page")
def login_page():
	return render_template("Login.html")


@app.route("/Graph")
def Graph():
	if not session.get("logged_in"):
		return render_template("Login.html")
	else:
		return render_template("Graph.html")


@app.route("/Frequency")
def Frequency():
	if not session.get("logged_in"):
		return render_template("Login.html")
	else:
		return render_template("Frequency.html")

@app.route("/ViewComplaints")
def ViewComplaints():
	if not session.get("logged_in"):
		return render_template("Login.html")
	else:
		complaints_data = db.get_complaints_data_from_db()
		return render_template("ViewComplaints.html", complaints_data = complaints_data)


if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True, port = 5001)



