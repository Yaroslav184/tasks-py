import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Регестрация'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label_1 = QLabel('Введите имя:', self)
        self.label_2 = QLabel('Введите пароль:', self)
        self.label_3 = QLabel('Повторите пароль:', self)
        self.label_4 = QLabel('Введите почту:', self)
        self.label_5 = QLabel('Введите номер телефона:', self)
        self.label_6 = QLabel('Введите адрес:', self)

        self.line_1 = QLineEdit(self)
        self.line_2 = QLineEdit(self)
        self.line_3 = QLineEdit(self)
        self.line_4 = QLineEdit(self)
        self.line_5 = QLineEdit(self)
        self.line_6 = QLineEdit(self)

        self.button_1 = QPushButton('Зарегистрироваться', self)
        self.button_1.clicked.connect(self.on_click)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label_1, 1, 0)
        grid.addWidget(self.line_1, 1, 1)

        grid.addWidget(self.label_2, 2, 0)
        grid.addWidget(self.line_2, 2, 1)

        grid.addWidget(self.label_3, 3, 0)
        grid.addWidget(self.line_3, 3, 1)

        grid.addWidget(self.label_4, 4, 0)
        grid.addWidget(self.line_4, 4, 1)

        grid.addWidget(self.label_5, 5, 0)
        grid.addWidget(self.line_5, 5, 1)

        grid.addWidget(self.label_6, 6, 0)
        grid.addWidget(self.line_6, 6, 1)

        grid.addWidget(self.button_1, 7, 0, 1, 2)

        self.setLayout(grid)
        self.show()

    @pyqtSlot()
    def on_click(self):
        if self.line_1.text() == '' or self.line_2.text() == '' or self.line_3.text() == '' or self.line_4.text() == '' or self.line_5.text() == '' or self.line_6.text() == '':
            QMessageBox.question(self, 'Ошибка', 'Заполните все поля!', QMessageBox.Ok)

        else:
            if self.line_2.text() == self.line_3.text():
                with open('registration.txt', 'a') as file:
                    file.write(self.line_1.text() + '\n')
                    file.write(self.line_2.text() + '\n')
                    file.write(self.line_4.text() + '\n')
                    file.write(self.line_5.text() + '\n')
                    file.write(self.line_6.text() + '\n')

                QMessageBox.question(self, 'Успешно', 'Вы успешно зарегистрировались!', QMessageBox.Ok)
                self.close()

            else:
                QMessageBox.question(self, 'Ошибка', 'Пароли не совпадают!', QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())