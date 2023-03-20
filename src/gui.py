from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		# in simple terms
		# self = window
		# w = gui elements inside the window
		super().__init__()

		w = QWidget()

		layout = QVBoxLayout()
		topButtons = QHBoxLayout()

		layout.addLayout(topButtons)
		layout.addStretch(1)

		w.setLayout(layout)

		openButton = QPushButton("Open database")
		topButtons.addWidget(openButton)

		createButton = QPushButton("Create database")
		topButtons.addWidget(createButton)

		topButtons.addStretch(1)

		self.setLayout(layout)

		self.resize(600,400)
		self.setWindowTitle("manager")
		self.setCentralWidget(w)
