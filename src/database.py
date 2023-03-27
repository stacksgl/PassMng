# parse a database from a string to an object inside the class

import json
from src.aes256 import *

class Database():
	#data = []
	password = ""
	'''data = [
		{'title': 'first', 'username': 'user 1', 'password': 'pass 1', 'note': ''},
		{'title': 'second', 'username': 'user 2', 'password': 'pass 2', 'note': ''}
	]'''
	data = []
	def __init__(self):
		print()

	def encrypt(self):
		aes = AESCipher(self.password)
		crypted = aes.encrypt(json.dumps(self.data))
		return crypted

	def decrypt(self, data, password):
		aes = AESCipher(password)
		decrypted = aes.decrypt(data)
		return decrypted

	def load(self, data, password):
		#TODO: possibly add self.initialized variable
		raw = self.decrypt(data, password)
		try:
			self.data = json.loads(raw)
		except:
			print("an error occured when reading the database")
			return False

		self.password = password
		#TODO: MD5 checksum
		return True

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
