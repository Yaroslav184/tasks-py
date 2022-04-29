import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задание 3')
        self.resize(300, 100)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setFont(QFont('Arial', 10))


        self.label = QLabel('Ввод:')
        self.label.setFont(QFont('Arial', 10))

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont('Arial', 10))

        self.button = QPushButton('Преобразовать')
        self.button.setFont(QFont('Arial', 10))
        self.button.clicked.connect(self.on_click)

        self.label_2 = QLabel('Вывод:')
        self.label_2.setFont(QFont('Arial', 10))

        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setFont(QFont('Arial', 10))

        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addWidget(self.button)

        self.hbox_2 = QHBoxLayout()

        self.hbox_2.addWidget(self.label_2)
        self.hbox_2.addWidget(self.line_edit_2)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox_2)

        self.setLayout(self.vbox)

    def on_click(self):
        text = self.line_edit.text()

        text_2 = ''
        for i in text:
            if i.isdigit():
                text_2 += str(int(i)**3)
            else:
                text_2 += i

        self.line_edit_2.setText(text_2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())