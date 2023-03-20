# parse a database from a string to an object inside the class

import json

class Database():
	def __init__(self):
		print()

	def load(data):
		self.data = json.loads(data)
		#TODO: MD5 checksum
		return true

	def deleteMember(member):
		#deletes a member
		self.data.pop(member, NULL)

	def setMember(member, value):
		#creates or changes a member
		self.data.member = value
