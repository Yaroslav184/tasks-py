# Ильин Ярослав 1993
# Вариант 2
# Задание 1

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('Нижний левый угол')
window.resize(300, 100)

desktop = QtWidgets.QApplication.desktop()

taskBarHeight = \
    (
        desktop.screenGeometry().height() -
        desktop.availableGeometry().height()
    )

x = 0
y = desktop.height() - window.frameSize().height() - taskBarHeight

window.move(x, y)
window.show()

app.exec_()