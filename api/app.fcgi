#!/usr/bin/python

# -*- coding: utf-8 -*-

from flup.server.fcgi import WSGIServer

from flask import Flask, request
from controller.AuthController import AuthController
from controller.SessionController import SessionController
from controller.EmployeeController import EmployeeController
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

###########################
# AUTH ROUTING METHODS #
###########################

# GET
@app.route('/auth', methods=['GET'])
def check_token():
	if AuthController.CheckToken():
		return "", 200
	else:
		return "Forbidden", 403

# POST
@app.route('/auth', methods=['POST'])
def login():
	return AuthController.Post()

# DELETE
@app.route('/auth/', methods=['DELETE'])
def logout():
	return AuthController.Delete()



###########################
# SESSION ROUTING METHODS #
###########################

# GET
@app.route('/session', methods=['GET'])
def get_all_sessions():
	if AuthController.CheckToken():
		return SessionController.GetAll(request.args)
	else:
		return "Forbidden", 403

@app.route('/session/<int:session_id>', methods=['GET'])
def get_session(session_id):
	if AuthController.CheckToken():
		return SessionController.GetByID(session_id,)
	else:
		return "Forbidden", 403

@app.route('/session/employee/<int:employee_id>', methods=['GET'])
def get_session_by_employee(employee_id):
	if AuthController.CheckToken():
		return SessionController.GetByEmployee(employee_id, request.args)
	else:
		return "Forbidden", 403

@app.route('/session/employee/<int:employee_id>/hours', methods=['GET'])
def get_session_employee_hours(employee_id):
	if AuthController.CheckToken():
		return SessionController.GetEmployeeHours(employee_id, request.args)
	else:
		return "Forbidden", 403

# POST
@app.route('/session', methods=['POST'])
def create_session():
	if AuthController.CheckToken():
		return SessionController.Post(request.form)
	else:
		return "Forbidden", 403

# PUT
@app.route('/session/<int:session_id>', methods=['PUT'])
def update_session(session_id):
	if AuthController.CheckToken():
		return SessionController.Put(session_id, request.form)
	else:
		return "Forbidden", 403

# DELETE
@app.route('/session/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
	if AuthController.CheckToken():
		return SessionController.Delete(session_id)
	else:
		return "Forbidden", 403



############################
# EMPLOYEE ROUTING METHODS #
############################

# GET
@app.route('/employee', methods=['GET'])
def get_all_employees():
	if AuthController.CheckToken():
		return EmployeeController.Get()
	else:
		return "Forbidden", 403

@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
	if AuthController.CheckToken():
		return EmployeeController.Get(employee_id)
	else:
		return "Forbidden", 403

# POST
@app.route('/employee', methods=['POST'])
def create_employee():
	if AuthController.CheckToken():
		return EmployeeController.Post(request.form)
	else:
		return "Forbidden", 403

# PUT
@app.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
	if AuthController.CheckToken():
		return EmployeeController.Put(employee_id, request.form)
	else:
		return "Forbidden", 403

# DELETE
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
	if AuthController.CheckToken():
		return EmployeeController.Delete(employee_id)
	else:
		return "Forbidden", 403


if __name__ == '__main__':
	WSGIServer(app).run()
