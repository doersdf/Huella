# -*- coding: utf-8 -*-

from model import *

class User:
	username = ''
	password = ''
	email = ''
	token = ''
	expire = ''

	def __init__(self, username = None, password = None, email = None, token = None, expire = None) :
		self.username = username
		self.password = password
		self.email = email
		self.token = token
		self.expire = expire

	def update(self) :
		db = DB()
		db.query("UPDATE users SET password = '%s', email = '%s', token = '%s', expire = '%s' WHERE username = '%s'" % (self.password, self.email, self.token, self.expire, self.username))

		return True
		

	@staticmethod
	def getByUsername(username): 
		db = DB()
		db.query("SELECT * FROM users WHERE username = '%s'" % username)
		results = db.result()
		db.close()

		return User(results[0][0], results[0][1], results[0][2], results[0][3], str(results[0][4]))


	@staticmethod
	def getByToken(token): 
		db = DB()
		db.query("SELECT * FROM users WHERE token = '%s'" % token)
		results = db.result()
		db.close()

		return User(results[0][0], results[0][1], results[0][2], results[0][3], str(results[0][4]))


