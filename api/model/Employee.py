# -*- coding: utf-8 -*-

from model import *

class Employee:

	id = ''
	name = ''
	email = ''
	code = ''
	fingerprint = ''
	week_hours = ''

	def __init__(self, id = None, name = None, email = None, code = None, fingerprint = None, week_hours = None) :
		self.id = id
		self.name = name
		self.email = email
		self.code = code
		self.fingerprint = fingerprint
		self.week_hours = week_hours

	def create(self) :
		db = DB()
		db.query("INSERT INTO employees (name, email, findprint, week_hours) VALUES ('%s', '%s', '%s', '%s')" % (self.name, self.email, self.fingerprint, self.week_hours))

		self.id = db.cursor.lastrowid

		return True

	def update(self) :
		db = DB()
		db.query("UPDATE employees SET name = '%s', email = '%s', week_hours = '%s' WHERE id = '%s'" % (self.name, self.email, self.week_hours, self.id))

		return True

	def delete(self) :
		db = DB()
		db.query("DELETE FROM employees WHERE id = '%s'" % self.id)

		del self

		return True

	@staticmethod
	def getByID(employee_id): 
		db = DB()
		db.query("SELECT * FROM employees WHERE id = '%s'" % employee_id)
		results = db.result()
		db.close()

		return Employee(int(results[0][0]), results[0][1], results[0][2], int(results[0][3]), results[0][4], int(results[0][5]))


	@staticmethod
	def getAll(): 
		db = DB()
		db.query("SELECT * FROM employees")
		results = db.result()
		db.close()

		employees = []
		for item in results :
			employees.append(Employee(int(item[0]), item[1], item[2], int(item[3]), item[4], int(item[5])))

		return employees


