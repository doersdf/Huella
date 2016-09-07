# -*- coding: utf-8 -*-

import json, datetime, time
from model.Session import Session


class SessionController:

	@staticmethod
	def GetAll(data = '') :
		
		json_data = []
		if data != '':
			data = data.to_dict()

			if 'from' in data and 'to' in data: #Filter by date
				format = "%Y-%m-%d"
				try:
					results = Session.getByDate(datetime.datetime.strptime(data['from'], format).strftime(format), datetime.datetime.strptime(data['to'], format).strftime(format))
				except ValueError:
					print ValueError
					return "Internal server error.", 500

				for item in results:
					json_data.append(item.__dict__)

			else: #Get all by default
				try:
					results = Session.getAll()
				except ValueError:
					print ValueError
					return "Internal server error.", 500

				for item in results:
					json_data.append(item.__dict__)

		else: #Get all
			try:
				results = Session.getAll()
			except ValueError:
				print ValueError
				return "Internal server error.", 500

			for item in results:
				json_data.append(item.__dict__)
			
		return json.dumps(json_data)

	@staticmethod
	def GetByID (id):
		json_data = []
		if type(id) is int and id > 0: #Get by session id
			try:
				json_data = Session.getByID(id).__dict__
			except ValueError:
				print ValueError
				return "Internal server error.", 500
		

		return json.dumps(json_data)

	@staticmethod
	def GetByEmployee (id, data = ''):

		json_data = []
		data = data.to_dict()
		format = "%Y-%m-%d"

		if type(id) is int and id > 0 and 'from' in data :

			try:
				f = datetime.datetime.strptime(data['from'], format).strftime(format)
				t = datetime.datetime.strptime(data['to'], format).strftime(format) if 'to' in data else f

				for session in Session.getByDate(f,t):
					if session.employee['id'] == id :
						json_data.append(session.__dict__)

			except ValueError:
				print ValueError
				return "Internal server error.", 500

		elif type(id) is int and id > 0: #Get by session id
			try:
				for session in Session.getAll():
					if session.employee['id'] == id :
						json_data.append(session.__dict__)

			except ValueError:
				print ValueError
				return "Internal server error.", 500
		

		return json.dumps(json_data)

	@staticmethod
	def GetEmployeeHours (id, data = ''):

		data = data.to_dict()
		dayFormat = "%Y-%m-%d"
		hourFormat = "%H:%M"

		if type(id) is int and id > 0 and 'from' in data :

			try:
				f = datetime.datetime.strptime(data['from'], dayFormat).strftime(dayFormat)
				t = datetime.datetime.strptime(data['to'], dayFormat).strftime(dayFormat) if 'to' in data else f

				hours = 0
				minutes = 0

				for session in Session.getByDate(f,t):
					if session.employee['id'] == id :
						startTime = time.strptime(session.start, hourFormat)
						start = datetime.timedelta(hours=startTime.tm_hour,minutes=startTime.tm_min,seconds=startTime.tm_sec).total_seconds()
						endTime = time.strptime(session.end, hourFormat)
						end = datetime.timedelta(hours=endTime.tm_hour,minutes=endTime.tm_min,seconds=endTime.tm_sec).total_seconds()
						m, s = divmod(end-start, 60)
						h, m = divmod(m, 60)
						hours += h
						minutes += m
				
				h, minutes = divmod(minutes, 60)
				hours += h

				json_data = {
					"from": str(f),
					"to": str(t),
					"hours": int(hours),
					"minutes": int(minutes),
					"employee_id": int(id)
				}						

				return json.dumps(json_data)

			except ValueError:
				print ValueError
				return "Internal server error.", 500

		elif type(id) is int and id > 0: #Get by session id
			try:
				for session in Session.getAll():
					if session.employee['id'] == id :
						json_data.append(session.__dict__)

			except ValueError:
				print ValueError
				return "Internal server error.", 500
		

		return json.dumps(json_data)

	@staticmethod
	def Post (data = ''):
		
		data = data.to_dict()
		dayFormat = "%Y-%m-%d"
		hourFormat = "%H:%M"

		if 'day' in data and 'start' in data and 'employee' in data :

			end = datetime.datetime.strptime(data['end'], hourFormat).strftime(hourFormat) if 'end' in data else None 

			session = Session(None, datetime.datetime.strptime(data['day'], dayFormat).strftime(dayFormat), datetime.datetime.strptime(data['start'], hourFormat).strftime(hourFormat), end, int(data['employee']))

			try:
				session.create()
				return "", 200
			except ValueError:
				print ValueError
				return "Internal server error.", 500

		else:
			return "Missing required parameters.", 400

	@staticmethod
	def Put (id = -1, data = ''):
		data = data.to_dict()
		dayFormat = "%Y-%m-%d"
		hourFormat = "%H:%M"

		if 'day' in data and 'start' in data and type(id) is int and id > 0:

			session = Session.getByID(id)

			end = data['end'] if 'end' in data else session.end
			employee = data['employee'] if 'employee' in data else session.employee.id

			
			session.day = datetime.datetime.strptime(data['day'], dayFormat).strftime(dayFormat)
			session.start = datetime.datetime.strptime(data['start'], hourFormat).strftime(hourFormat)
			session.end = end
			session.employee = employee

			try:
			 	session.update()
				return "", 200
			except ValueError:
				print ValueError
				return "Internal server error.", 500

		else:
			return "Missing required parameters.", 400

	@staticmethod
	def Delete (id = -1):
		if type(id) is int and id > 0:
			try:
				session = Session.getByID(id)
			 	session.delete()
				return "", 200
			except ValueError:
				print ValueError
				return "Internal server error.", 500
		else:
			return "Missing required parameters in url: [id].", 404