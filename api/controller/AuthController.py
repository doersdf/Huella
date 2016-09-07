# -*- coding: utf-8 -*-

import json, base64, hashlib, datetime
from flask import request
from model.User import User

class AuthController:

	@staticmethod
	def CheckToken():
		try:
			user = User.getByToken(request.headers.get("token"))
		except: 
			return False

		expire = datetime.datetime.strptime(user.expire, "%Y-%m-%d %H:%M:%S")

		return expire > datetime.datetime.now()


	@staticmethod
	def Post():
		http_basic_auth = request.headers.get("Authorization").split(" ")[1].decode("base64")

		username = http_basic_auth.split(":")[0]
		password = base64.b64encode(hashlib.sha512(http_basic_auth.split(":")[1]).hexdigest())

		try:
			user = User.getByUsername(username)
		except:
			return "User not found.", 403

		logged = False
		
		if user.expire != "None":
		
			expire = datetime.datetime.strptime(user.expire, "%Y-%m-%d %H:%M:%S")
			logged = True


		if logged and expire > datetime.datetime.now():
			
			delattr(user, 'password')
			return json.dumps(user.__dict__)

		elif password == user.password:
			
			user.expire = (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
			user.token = base64.b64encode(hashlib.sha512(username + password + user.expire).hexdigest())

			try:
				user.update()
			except:
				return "Internal server error.[]", 500

			delattr(user, 'password')

			return json.dumps(user.__dict__)

		else:
			
			return "Incorrect password.", 403
 

	@staticmethod
	def Delete():
		try:
			user = User.getByToken(request.headers.get("token"))
		except:
			return "User not found.", 403

		user.token = ''
		user.expire = "0000-00-00 00:00:00"

		try:
			user.update()
		except:
			return "Internal server error.", 500

		return "", 200


