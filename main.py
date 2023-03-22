import sys

from src.gui import *

"""app = QApplication(sys.argv)

#window = MainWindow()
window.show()

app.exec()"""

db = Database()
db.createMember({
	"title": "visible title",
	"username": "visible username",
	"password": "visible password",
	"note": "visible note"
})
db.print()
db.editMember(0, {
	"title": "visible edited title",
	"username": "visible username",
	"password": "visible password",
	"note": "visible note"
})
db.print()
db.deleteMember(0)
db.print()
