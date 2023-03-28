from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pathlib import Path

class createDatabaseWindow(QFrame):
	def createDatabase(self):
		self.mWin.database.new(self.passwordInput.text())
		#TODO: fix security
		self.mWin.dbPath = Path(self.nameInput.text())
		self.mWin.openDbFrame.dbPath = self.mWin.dbPath

		self.mWin.changeState("dbview")

	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		line = QHBoxLayout()

		label = QLabel("File name")
		line.addWidget(label)

		self.nameInput = QLineEdit("")
		line.addWidget(self.nameInput)

		layout.addLayout(line)

		line = QHBoxLayout()

		label = QLabel("Password")
		line.addWidget(label)

		self.passwordInput = QLineEdit("")
		line.addWidget(self.passwordInput)

		layout.addLayout(line)

		line = QHBoxLayout()

		line.addStretch(1)

		self.cancelButton = QPushButton("Cancel")
		line.addWidget(self.cancelButton)

		self.okButton = QPushButton("Create")
		self.okButton.clicked.connect(self.createDatabase)
		line.addWidget(self.okButton)

		layout.addLayout(line)

		self.setLayout(layout)

