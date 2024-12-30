# <Python编程基础及应用> 随书代码 高等教育出版社
import sys
from PyQt5 import QtWidgets
import MainWidget

app = QtWidgets.QApplication(sys.argv)

mw = MainWidget.MainWidget()
mw.show()

exit(app.exec_())

