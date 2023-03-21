import sys

from src.gui import *

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
