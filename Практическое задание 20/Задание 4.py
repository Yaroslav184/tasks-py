"""
The program is a text editor
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QFontDialog, QColorDialog
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QAction('Текстовый редактор', self)
        self.textEdit.setShortcut('Ctrl+T')
        self.textEdit.setStatusTip('Текстовый редактор')
        self.textEdit.triggered.connect(self.text_editor)

        self.font = QAction('Шрифт', self)
        self.font.setShortcut('Ctrl+F')
        self.font.setStatusTip('Шрифт')
        self.font.triggered.connect(self.font_dialog)

        self.color = QAction('Цвет', self)
        self.color.setShortcut('Ctrl+C')
        self.color.setStatusTip('Цвет')
        self.color.triggered.connect(self.color_dialog)

        self.exit = QAction('Выход', self)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Выход')
        self.exit.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(self.textEdit)
        fileMenu.addAction(self.font)
        fileMenu.addAction(self.color)
        fileMenu.addAction(self.exit)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Текстовый редактор')
        self.show()

    def text_editor(self):
        self.textEdit = QWidget(self)
        self.setCentralWidget(self.textEdit)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setStyleSheet('QWidget { background-color: %s}' % color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
