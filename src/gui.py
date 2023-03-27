from src.database import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.elements.entryModification import *
from src.elements.databaseOverview import *
from src.elements.openDatabase import *

class MainWindow(QMainWindow):
	def loadDatabase(self):
		fileName = QFileDialog.getOpenFileName(self, str("Open File"),
			"",
			str("PassMng Database (*.pmdb)"))[0]

		if fileName:
			self.dbPath = Path(fileName)
			with open(self.dbPath) as f:
				d = f.read()
			self.database.load(d, "1234567812345678")

			self.dbViewFrame.updateList()

	def saveDatabase(self):
		if self.dbPath:
			print()

		with open("x.pmdb", "w") as f:
			d = f.write(self.database.encrypt())
		
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
		#dbopen = database unlocking thingy
		#dbview = database overview
		#enmod = entry modification
		self.eModFrame.setHidden(state != "enmod")
		self.dbViewFrame.setHidden(state != "dbview")
		self.openDbFrame.setHidden(state != "dbopen")

		self.modifyEntry.setEnabled(state != "enmod")
		self.addEntry.setEnabled(state != "enmod")

		#TODO: move update method somewhere else, when the database is actually modified
		if state == "dbview":
			self.dbViewFrame.updateList()

		self.database.print()

	def __init__(self):
		super().__init__()

		self.dbPath = None
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

		self.dbViewFrame = databaseOverviewWindow(self)
		self.dbViewFrame.hide()
		layout.addWidget(self.dbViewFrame)

		self.openDbFrame = openDatabaseWindow(self)
		layout.addWidget(self.openDbFrame)
		# BOTTOM SCREEN
		layout.addStretch(1)

		w.setLayout(layout)

		self.openButton = QPushButton("Close database")
		self.openButton.clicked.connect(self.loadDatabase)
		topButtons.addWidget(self.openButton)

		self.createButton = QPushButton("Create database")
		topButtons.addWidget(self.createButton)

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

		self.setLayout(layout)

		self.resize(600,400)
		self.setWindowTitle("manager")
		self.setCentralWidget(w)
