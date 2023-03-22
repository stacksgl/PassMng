from src.database import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.elements.entryModification import *
from src.elements.databaseOverview import *

class MainWindow(QMainWindow):
	def loadDatabase(self):
		print()
		
	def createDatabase(self):
		print()

	def addEntryClicked(self):
		self.changeState("enmod")
		self.eModFrame.pushState("create", -1)
		self.eModFrame.clearInputBoxes()

	def modifyEntryClicked(self):
		self.changeState("enmod")

		i = self.dbViewFrame.getIndexSelected()
		self.eModFrame.pushState("edit", i)
		self.eModFrame.changeInputBoxes(self.database.getMemberAt(i))

	def changeState(self, state):
		#hide bottom part based on the state
		#pw = password input
		#dbview = database overview
		#enmod = entry modification
		self.eModFrame.setHidden(state != "enmod")
		self.modifyEntry.setEnabled(state != "enmod")
		self.addEntry.setEnabled(state != "enmod")
		self.dbViewFrame.setHidden(state != "dbview")

		#TODO: move update method somewhere else, when the database is actually modified
		if state == "dbview":
			self.dbViewFrame.updateList()

		self.database.print()

	def __init__(self):
		super().__init__()

		self.database = Database()

		# in simple terms
		# self = window
		# w = gui elements inside the window

		w = QWidget()

		layout = QVBoxLayout()
		topButtons = QHBoxLayout()

		layout.addLayout(topButtons)
		# BOTTOM SCREEN
		# TODO: move to different file
		self.eModFrame = entryModificationWindow(self)
		self.eModFrame.hide()
		layout.addWidget(self.eModFrame)

		#self.dbViewFrame.addWidget(lst)

		self.dbViewFrame = databaseOverviewWindow(self)
		layout.addWidget(self.dbViewFrame)
			###
		# BOTTOM SCREEN
		layout.addStretch(1)

		w.setLayout(layout)

		self.openButton = QPushButton("Open database")
		self.openButton.clicked.connect(self.loadDatabase)
		topButtons.addWidget(self.openButton)

		self.createButton = QPushButton("Create database")
		topButtons.addWidget(self.createButton)

		self.addEntry = QPushButton("Add entry")
		self.addEntry.clicked.connect(self.addEntryClicked)
		topButtons.addWidget(self.addEntry)

		self.modifyEntry = QPushButton("Modify entry")
		self.modifyEntry.clicked.connect(self.modifyEntryClicked)
		topButtons.addWidget(self.modifyEntry)

		topButtons.addStretch(1)

		self.setLayout(layout)

		self.resize(600,400)
		self.setWindowTitle("manager")
		self.setCentralWidget(w)
