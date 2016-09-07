import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'arteria123' 
DB_NAME = 'fichaje'

class DB:
	
	def __init__(self) :
		self.conn = MySQLdb.connect(user=DB_USER, passwd=DB_PASS, db=DB_NAME, host=DB_HOST, use_unicode=True, charset="utf8")
		self.cursor = self.conn.cursor()

	def query (self, query = ''):
		self.cursor.execute(query)

		if not query.upper().startswith('SELECT') :
			self.conn.commit()

	def result(self):
		return self.cursor.fetchall()

	def close (self):
		self.cursor.close()
		self.conn.close()
 