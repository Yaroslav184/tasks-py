import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Приложение')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel('Введите числа из файла file:', self)
        self.label.move(20, 20)

        self.line = QLineEdit(self)
        self.line.move(20, 50)
        self.line.resize(280, 40)

        self.button = QPushButton('Подсчитать', self)
        self.button.move(20, 100)
        self.button.clicked.connect(self.on_click)

        self.label_sum = QLabel('Сумма:', self)
        self.label_sum.move(20, 150)

        self.label_mult = QLabel('Произведение:', self)
        self.label_mult.move(20, 170)

        self.show()

    def on_click(self):
        with open('file', 'r') as f:
            data = f.read()
        data = data.split()
        sum = 0
        mult = 1
        for i in data:
            sum += int(i)
            mult *= int(i)
        self.label_sum.setText(str(sum))
        self.label_mult.setText(str(mult))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())