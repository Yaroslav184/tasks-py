import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Приложение площадь'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icon.png'))
        self.createGrid()
        self.show()

    def createGrid(self):
        self.label_1 = QLabel('Выберите фигуру:', self)
        self.label_1.move(20, 20)
        self.label_2 = QLabel('Введите первую сторону:', self)
        self.label_2.move(20, 60)
        self.label_3 = QLabel('Введите вторую сторону:', self)
        self.label_3.move(20, 100)
        self.label_4 = QLabel('Введите третью сторону:', self)
        self.label_4.move(20, 140)
        self.label_5 = QLabel('Площадь:', self)
        self.label_5.move(20, 180)
        self.label_6 = QLabel('Периметр:', self)
        self.label_6.move(20, 220)
        self.combo = QComboBox(self)
        self.combo.addItem('Квадрат')
        self.combo.addItem('Прямоугольник')
        self.combo.addItem('Треугольник')
        self.combo.move(20, 40)
        self.line_1 = QLineEdit(self)
        self.line_1.move(20, 80)
        self.line_2 = QLineEdit(self)
        self.line_2.move(20, 120)
        self.line_3 = QLineEdit(self)
        self.line_3.move(20, 160)
        self.line_4 = QLineEdit(self)
        self.line_4.move(20, 200)
        self.line_5 = QLineEdit(self)
        self.line_5.move(20, 240)
        self.button = QPushButton('Рассчитать', self)
        self.button.move(20, 280)
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        if self.combo.currentText() == 'Квадрат':
            self.line_1.setText(str(int(self.line_1.text()) ** 2))
            self.line_2.setText(str(int(self.line_1.text()) * 4))
        elif self.combo.currentText() == 'Прямоугольник':
            self.line_1.setText(str(int(self.line_1.text()) * int(self.line_2.text())))
            self.line_2.setText(str(int(self.line_1.text()) + int(self.line_2.text())))
        elif self.combo.currentText() == 'Треугольник':
            if int(self.line_1.text()) == int(self.line_2.text()) == int(self.line_3.text()):
                self.line_1.setText('Треугольник не существует')
            else:
                self.line_1.setText(str(int(self.line_1.text()) * int(self.line_2.text()) / 2))
                self.line_2.setText(str(int(self.line_1.text()) + int(self.line_2.text()) + int(self.line_3.text())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())