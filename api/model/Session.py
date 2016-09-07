# -*- coding: utf-8 -*-

import time
from model import *
from model.Employee import Employee

class Session:

	id = ''
	day = ''
	start = time.strftime("%H:%M")
	end = ''
	employee = ''

	def __init__(self, id = None, day = None, start = None, end = None, employee = None) :
		self.id = id
		self.day = day
		self.start = start
		self.end = end
		self.employee = employee

	def create(self) :
		db = DB()

		self.end = None if self.end is None else str(self.end)

		db.query("INSERT INTO sessions (day, start, end, employee) VALUES ('%s', '%s', '%s', '%s')" % (str(self.day), str(self.start), self.end, int(self.employee)))

		self.id = db.cursor.lastrowid

		return True

	def update(self) :
		db = DB()
		db.query("UPDATE sessions SET day = '%s', start = '%s', end  = '%s', employee = '%s' WHERE id = '%s'" % (str(self.day), str(self.start), str(self.end), self.employee, self.id))

		return True

	def delete(self) :
		db = DB()
		db.query("DELETE FROM sessions WHERE id = '%s'" % self.id)

		del self

		return True

	@staticmethod
	def getByID(session_id): 
		db = DB()
		db.query("SELECT * FROM sessions WHERE id = %s" % session_id)
		results = db.result()
		db.close()

		employee = Employee.getByID(int(results[0][4]))
		start = time.strftime("%H:%M", time.strptime(str(results[0][2]), "%H:%M:%S"))
		end = time.strftime("%H:%M", time.strptime(str(results[0][3]), "%H:%M:%S"))
		
		return Session(int(results[0][0]), str(results[0][1]), start, end, employee.__dict__)

	@staticmethod
	def getByDate(date_from, date_to): 

		db = DB()
		db.query("SELECT * FROM sessions WHERE (day BETWEEN '%s' AND '%s')" % (str(date_from), str(date_to)))
		results = db.result()

		db.close()

		sessions = []
		for item in results:
			employee = Employee.getByID(int(item[4]))
			start = time.strftime("%H:%M", time.strptime(str(item[2]), "%H:%M:%S"))
			end = time.strftime("%H:%M", time.strptime(str(item[3]), "%H:%M:%S"))

			sessions.append(Session(int(item[0]), str(item[1]), start, end, employee.__dict__))

		return sessions

	@staticmethod
	def getByEmployee(employee): 
		db = DB()
		db.query("SELECT * FROM sessions WHERE employee = '%s'" % employee)
		results = db.result()
		db.close()

		sessions = []
		for item in results:
			employee = Employee.getByID(int(item[4]))
			start = time.strftime("%H:%M", time.strptime(str(item[2]), "%H:%M:%S"))
			end = time.strftime("%H:%M", time.strptime(str(item[3]), "%H:%M:%S"))

			sessions.append(Session(int(item[0]), str(item[1]), start, end, employee.__dict__))

		return sessions

	@staticmethod
	def getByDateEmployee(date_from, date_to, employee): 

		db = DB()
		db.query("SELECT * FROM sessions WHERE (day BETWEEN '%s' AND '%s') AND employee = '%s'" % (str(date_from), str(date_to), employee))
		results = db.result()

		db.close()

		sessions = []
		for item in results:
			employee = Employee.getByID(int(item[4]))
			start = time.strftime("%H:%M", time.strptime(str(item[2]), "%H:%M:%S"))
			end = time.strftime("%H:%M", time.strptime(str(item[3]), "%H:%M:%S"))

			sessions.append(Session(int(item[0]), str(item[1]), start, end, employee.__dict__))

		return sessions

	@staticmethod
	def getAll(): 
		db = DB()
		db.query("SELECT * FROM sessions")
		results = db.result()
		db.close()

		sessions = []
		for item in results:
			employee = Employee.getByID(int(item[4]))
			start = time.strftime("%H:%M", time.strptime(str(item[2]), "%H:%M:%S"))
			end = time.strftime("%H:%M", time.strptime(str(item[3]), "%H:%M:%S"))

			sessions.append(Session(int(item[0]), str(item[1]), start, end, employee.__dict__))

		return sessions



		