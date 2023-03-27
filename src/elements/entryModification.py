from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class entryModificationWindow(QFrame):
	def pushState(self, action, index):
		self.state["action"] = action
		self.state["index"] = index

	def cancelClicked(self):
		self.mWin.changeState("dbview")

	def saveClicked(self):
		if self.state["action"] == "create":
			#TODO: cleanup, use loops, too tired atm
			self.mWin.database.createMember({
				"title": self.inputBoxes["Title"].text(),
				"username": self.inputBoxes["Username"].text(),
				"password": self.inputBoxes["Password"].text(),
				"note": self.inputBoxes["Note"].text()
			})
		elif self.state["action"] == "edit":
			self.mWin.database.editMember(self.state["index"], {
				"title": self.inputBoxes["Title"].text(),
				"username": self.inputBoxes["Username"].text(),
				"password": self.inputBoxes["Password"].text(),
				"note": self.inputBoxes["Note"].text()
			})

		self.mWin.changeState("dbview")

	def changeInputBoxes(self, data):
		for b in self.inputBoxes:
			self.inputBoxes[b].setText(data[b.lower()])

	def clearInputBoxes(self):
		for b in self.inputBoxes:
			self.inputBoxes[b].setText("")
	
	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin
		self.inputBoxes = {}
		self.state = {
			"action": "", #string, valid options: "create", "edit"
			"index": -1 #integer
		}

		layout = QVBoxLayout()
		values = ["Title", "Username", "Password", "Note"]

		#not sure if a loop makes sense since events are a thing
		for v in values:
			line = QHBoxLayout()

			label = QLabel(v)
			line.addWidget(label)

			lineEdit = QLineEdit("")
			line.addWidget(lineEdit)

			layout.addLayout(line)
			self.inputBoxes[v] = lineEdit

		buttons = QHBoxLayout()
		buttons.addStretch(1)

		cancel = QPushButton("Cancel")
		cancel.clicked.connect(self.cancelClicked)
		buttons.addWidget(cancel)

		save = QPushButton("Save")
		save.clicked.connect(self.saveClicked)
		buttons.addWidget(save)
		
		layout.addLayout(buttons)

		#TODO: remove padding?
		self.setLayout(layout)
