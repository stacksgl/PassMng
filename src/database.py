# parse a database from a string to an object inside the class

import json

class Database():
	data = []
	def __init__(self):
		print()

	def load(self, data):
		#TODO: possibly add self.initialized variable
		try:
			self.data = json.loads(data)
			#array of data
		except:
			print("an error occured when reading the database")
			return false

		#TODO: MD5 checksum
		return true

	#TODO: error handling
	def deleteMember(self, member):
		#member = integer

		#deletes a member
		self.data.pop(member)

	def createMember(self, value):
		#member = integer
		#value = dictionary?
		#creates or changes a member
		self.data.append(value)

	def editMember(self, member, value):
		#member = integer
		#value = dictionary?
		#creates or changes a member
		self.data[member] = value

	#TODO: delete, temporary function
	def print(self):
		print(self.data)
