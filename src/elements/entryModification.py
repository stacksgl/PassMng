from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class entryModificationWindow(QFrame):
	def cancelClicked(self):
		self.mWin.changeState("dbview")

	def saveClicked(self):
		self.mWin.changeState("dbview")
	
	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin
		self.inputBoxes = {}

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
