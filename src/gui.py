from src.database import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def entryModificationWindow():
	#TODO: cleanup?
	p = QVBoxLayout()

	line = QHBoxLayout()
	label = QLabel("Title")
	line.addWidget(label)

	lineEdit = QLineEdit("")
	line.addWidget(lineEdit)
	p.addLayout(line) ######################

	line = QHBoxLayout()
	label = QLabel("Username")
	line.addWidget(label)

	lineEdit = QLineEdit("")
	line.addWidget(lineEdit)
	p.addLayout(line) ######################

	line = QHBoxLayout()
	label = QLabel("Password")
	line.addWidget(label)

	lineEdit = QLineEdit("")
	line.addWidget(lineEdit)
	p.addLayout(line) ######################

	line = QHBoxLayout()
	label = QLabel("Note")
	line.addWidget(label)

	lineEdit = QLineEdit("")
	line.addWidget(lineEdit)
	p.addLayout(line) ######################



	return p

class MainWindow(QMainWindow):
	def loadDatabase(self):
		print()
		
	def createDatabase(self):
		print()

	def addEntry(self):
		print()

	def modifyEntry(self):
		self.state = 1
		print()

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
		entryModification = entryModificationWindow()

			###
		layout.addLayout(entryModification)
		# BOTTOM SCREEN
		layout.addStretch(1)

		w.setLayout(layout)

		openButton = QPushButton("Open database")
		openButton.clicked.connect(self.loadDatabase)
		topButtons.addWidget(openButton)

		createButton = QPushButton("Create database")
		topButtons.addWidget(createButton)

		addEntry = QPushButton("Add entry")
		addEntry.clicked.connect(self.addEntry)
		topButtons.addWidget(addEntry)

		modifyEntry = QPushButton("Modify entry")
		topButtons.addWidget(modifyEntry)

		topButtons.addStretch(1)

		self.setLayout(layout)

		self.resize(600,400)
		self.setWindowTitle("manager")
		self.setCentralWidget(w)
