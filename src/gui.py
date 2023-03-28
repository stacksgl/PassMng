from src.database import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.elements.mainDecision import *

from src.elements.entryModification import *
from src.elements.databaseOverview import *

from src.elements.openDatabase import *
from src.elements.createDatabase import *

class MainWindow(QMainWindow):
	def changeState(self, state):
		#hide bottom part based on the state
		#main = thing you see first
		#dbcreate = new database password input
		#dbopen = database unlocking thingy
		#dbview = database overview
		#enmod = entry modification
		self.eModFrame.setHidden(state != "enmod")
		self.dbViewFrame.setHidden(state != "dbview")
		self.openDbFrame.setHidden(state != "dbopen")
		self.createDbFrame.setHidden(state != "dbcreate")
		self.mainDcsnFrame.setHidden(state != "main")

		self.dbViewFrame.modifyEntry.setEnabled(state != "enmod")
		self.dbViewFrame.addEntry.setEnabled(state != "enmod")

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

		# BOTTOM SCREEN
		# TODO: move to different file
		self.eModFrame = entryModificationWindow(self)
		self.eModFrame.hide()
		layout.addWidget(self.eModFrame)

		self.dbViewFrame = databaseOverviewWindow(self)
		self.dbViewFrame.hide()
		layout.addWidget(self.dbViewFrame)

		self.openDbFrame = openDatabaseWindow(self)
		self.openDbFrame.hide()
		layout.addWidget(self.openDbFrame)

		self.createDbFrame = createDatabaseWindow(self)
		self.createDbFrame.hide()
		layout.addWidget(self.createDbFrame)

		self.mainDcsnFrame = mainDecisionWindow(self)
		layout.addWidget(self.mainDcsnFrame)
		# BOTTOM SCREEN
		layout.addStretch(1)

		w.setLayout(layout)

		#self.openButton = QPushButton("Open database")
		#self.openButton.clicked.connect(self.loadDatabase)
		#topButtons.addWidget(self.openButton)

		self.setLayout(layout)

		self.resize(600,400)
		self.setWindowTitle("manager")
		self.setCentralWidget(w)
