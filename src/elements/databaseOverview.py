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

	def __init__(self, mWin):
		super().__init__()
		self.mWin = mWin

		layout = QVBoxLayout()

		self.list = QListWidget()
		self.list.currentItemChanged.connect(self.selectionChanged)
		
		self.label = QLabel("")

		layout.addWidget(self.list)

		layout.addWidget(self.label)

		#TODO: remove padding?
		self.setLayout(layout)
