from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class databaseOverviewWindow(QFrame):
	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		lst = QListWidget()
		lst.addItem(QListWidgetItem("boing"))

		layout.addWidget(lst)

		#TODO: remove padding?
		self.setLayout(layout)
