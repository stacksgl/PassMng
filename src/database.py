# parse a database from a string to an object inside the class

import json

class Database():
	#data = []
	data = [{'title': 'first', 'username': 'user 1', 'password': 'pass 1', 'note': ''}, {'title': 'second', 'username': 'user 2', 'password': 'pass 2', 'note': ''}]
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

	def getTitles(self):
		product = []

		for m in self.data:
			product.append(m["title"])

		return product

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

	def getMemberAt(self, member):
		return self.data[member]

	#TODO: delete, temporary function
	def print(self):
		print(self.data)
