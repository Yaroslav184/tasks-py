import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Графическое приложение'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icon.png'))
        self.createGrid()
        self.show()

    def createGrid(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        self.createButtons()
        self.createLabels()

    def createButtons(self):
        self.button1 = QPushButton('Получить числа из файла')
        self.button1.clicked.connect(self.getNumbers)
        self.grid.addWidget(self.button1, 0, 0)

    def createLabels(self):
        self.label1 = QLabel('Числа из файла:')
        self.grid.addWidget(self.label1, 1, 0)
        self.label2 = QLabel('Числа возведенные в квадрат:')
        self.grid.addWidget(self.label2, 2, 0)

    def getNumbers(self):
        self.numbers = []
        self.numbersSquared = []
        self.numbersCubed = []
        with open('file', 'r') as file:
            for line in file:
                self.numbers.append(int(line))
        for number in self.numbers:
            self.numbersSquared.append(number**2)
            self.numbersCubed.append(number**3)
        self.label1.setText('Числа из файла: ' + str(self.numbers))
        self.label2.setText('Числа возведенные в квадрат: ' + str(self.numbersSquared))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())