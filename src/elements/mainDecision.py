from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pathlib import Path

class mainDecisionWindow(QFrame):
	def createDatabase(self):
		self.mWin.changeState("dbcreate")
		
	def openDatabase(self):
		fileName = QFileDialog.getOpenFileName(self, str("Open File"),
			"",
			str("PassMng Database (*.pmdb)"))[0]

		if fileName:
			self.mWin.dbPath = Path(fileName)
			self.mWin.openDbFrame.dbPath = self.mWin.dbPath
			self.mWin.changeState("dbopen")

	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		#TODO: make big
		bigWelcome = QLabel("Welcome to PassMng")
		layout.addWidget(bigWelcome)

		self.createButton = QPushButton("Create a new database")
		self.createButton.clicked.connect(self.createDatabase)
		layout.addWidget(self.createButton)

		self.openButton = QPushButton("Open an existing database")
		self.openButton.clicked.connect(self.openDatabase)
		layout.addWidget(self.openButton)

		self.setLayout(layout)

