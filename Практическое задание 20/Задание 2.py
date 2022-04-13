# Ильин Ярослав 1993
# Задание 2

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget

class MyWindow(QWidget.OWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lbl = QLabel('Щёлкните мышью в окно', self)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.setLayout(self.vbox)

    def mousePressEvent(self, e):
        self.lbl.setText('X: {}, Y: {}'.format(e.x(), e.y()))
        e.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('Пользовательский указатель')
    w.resize(300, 300)
    w.show()
    sys.exit(app.exec_())