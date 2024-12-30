import sys
from PyQt5 import QtWidgets
import MainDemo

app = QtWidgets.QApplication(sys.argv)

mw = MainDemo.MainDemo()
mw.show()

exit(app.exec_())


