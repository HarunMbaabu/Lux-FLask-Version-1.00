import os
from flask import Flask, render_template, url_for, jsonify
#import MongoClient from pymongo
#from pymongo import MongoClient


#app.config['SECRET_KEY'] = OS.environ.get('SECTRET_KEY', 'XYZ')
app = Flask(__name__)
#Provide a host url for mongo database.
#client = MongoClient('mongodb://127.0.0.1:27017')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/Course")
def Courses():
	return render_template("Course.html")

@app.route("/Blog")
def Blogs():
	return render_template("Blog.html")



@app.route("/About")
def About():
	return render_template("About.html")

"""
@app.route("/Course")
def  Tech_Talk():
	return render_template("course.html")
"""
"""
@app.route("/Course")
def Sign_Up():
	return render_template("course.html")
"""
"""
@app.route("/Course")
def Log_In():
	return render_template("course.html")	
"""
if __name__ == '__main__':
	app.run(debug= True)


