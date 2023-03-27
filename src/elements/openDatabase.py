from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pathlib import Path

class openDatabaseWindow(QFrame):
	dbPath = None
	def selectDatabase(self):
		fileName = QFileDialog.getOpenFileName(self, str("Open File"),
			"",
			str("PassMng Database (*.pmdb)"))[0]

		if fileName:
			self.dbPath = Path(fileName)

			#MOVE

	def unlockDatabase(self):
		if self.dbPath and len(self.passwordInput.text()) != 0:
			with open(self.dbPath) as f:
				d = f.read()
				res = self.mWin.database.load(d, self.passwordInput.text())
				if res:
					self.mWin.dbViewFrame.updateList()
					self.mWin.changeState("dbview")
				else:
					print("show errors here")
				#TODO: show error to user

	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		self.selectButton = QPushButton("Select a database file")
		self.selectButton.clicked.connect(self.selectDatabase)
		layout.addWidget(self.selectButton)

		line = QHBoxLayout()

		label = QLabel("Password")
		line.addWidget(label)

		self.passwordInput = QLineEdit("")
		line.addWidget(self.passwordInput)

		layout.addLayout(line)

		self.unlockButton = QPushButton("Unlock")
		self.unlockButton.clicked.connect(self.unlockDatabase)
		layout.addWidget(self.unlockButton)

		#TODO: remove padding?
		self.setLayout(layout)
