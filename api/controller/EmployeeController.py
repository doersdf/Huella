# -*- coding: utf-8 -*-

import json, datetime
from model.Employee import Employee


class EmployeeController:

	@staticmethod
	def Get(id = -1) :
		json_data = []
		if id == -1: #Get All
			try:
				results = Employee.getAll()
			except:
				return "Internal server error.", 500

			for item in results:
				json_data.append(item.__dict__)

		elif type(id) is int and id > 0: #Get by employee id
			try:
				json_data = Employee.getByID(id).__dict__
			except:
				return "Internal server error.", 500
		
		return json.dumps(json_data)

	@staticmethod
	def Post (data = ''):
		data = data.to_dict()

		if 'name' in data and 'email' in data and 'hours' in data:
			employee = Employee(None, data['name'], data['email'], data['hours'])

			try:	
				employee.create()
				return "", 200
			except:
				return "Internal server error.", 500

		else :
			return "Missing required parameters.", 400

	@staticmethod
	def Put (id = -1, data = ''):
		data = data.to_dict()
		format = "%Y-%m-%d %H:%M:%S"

		if 'name' in data or 'email' in data or 'hours' in data:
			try:
				employee = Employee.getByID(id)
			except:
				return "Internal server error.", 500

			if 'name' in data and data['name'] != employee.name:
				employee.name = data['name']

			if 'email' in data and data['email'] != employee.email:
				employee.email = data['email']

			if 'hours' in data and data['hours'] != employee.hours:
				employee.hours = data['hours']

			try:
				employee.update()
				return "", 200
			except:
				return "Internal server error.", 500

		else:
			return "Missing required parameters.", 400

	@staticmethod
	def Delete (id = -1):
		if type(id) is int and id > 0:
			try:
				employee = Employee.getByID(id)
				employee.delete()
				return "", 200
			except:
				return "Internal server error.", 500
		else:
			return "Missing required parameters in url: [id].", 404