#TODO: remove once that method is nice enough
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class databaseOverviewWindow(QFrame):
	def getIndexSelected(self):
		return self.list.currentRow()

	def updateList(self):
		titles = self.mWin.database.getTitles()

		self.list.clear()
		for t in titles:
			self.list.addItem(QListWidgetItem(t))

	def selectionChanged(self):
		idx = self.list.currentRow()
		#TODO: make a database method instead of this goofy "patch"
		val = self.mWin.database.data[idx]

		#TODO: make nice instead of a POC
		self.label.setText(json.dumps(val))
		
	def saveDatabase(self):
		if self.mWin.dbPath:
			print()

		with open(self.mWin.dbPath, "w") as f:
			d = f.write(self.mWin.database.encrypt())
		
	def createDatabase(self):
		print()

	def addEntryClicked(self):
		self.mWin.changeState("enmod")
		self.mWin.eModFrame.pushState("create", -1)
		self.mWin.eModFrame.clearInputBoxes()

	def modifyEntryClicked(self):
		self.mWin.changeState("enmod")

		i = self.mWin.dbViewFrame.getIndexSelected()
		self.mWin.eModFrame.pushState("edit", i)
		self.mWin.eModFrame.changeInputBoxes(self.mWin.database.getMemberAt(i))


	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		topButtons = QHBoxLayout()
		layout.addLayout(topButtons)

		self.saveButton = QPushButton("Save database")
		self.saveButton.clicked.connect(self.saveDatabase)
		topButtons.addWidget(self.saveButton)

		self.addEntry = QPushButton("Add entry")
		self.addEntry.clicked.connect(self.addEntryClicked)
		topButtons.addWidget(self.addEntry)

		self.modifyEntry = QPushButton("Modify entry")
		self.modifyEntry.clicked.connect(self.modifyEntryClicked)
		topButtons.addWidget(self.modifyEntry)

		topButtons.addStretch(1)

		self.list = QListWidget()
		self.list.currentItemChanged.connect(self.selectionChanged)
		
		self.label = QLabel("")

		layout.addWidget(self.list)

		layout.addWidget(self.label)

		#TODO: remove padding?
		self.setLayout(layout)
