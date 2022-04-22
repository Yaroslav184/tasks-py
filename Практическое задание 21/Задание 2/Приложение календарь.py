# Ильин Ярослав 1993
# Вариант 6

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.show_date)
        self.label = QLabel(self)
        self.label.setText('Выберите дату')
        self.button = QPushButton('Отобразить рисунок', self)
        self.button.clicked.connect(self.show_image)
        self.button.setEnabled(False)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.setWindowTitle('Календарь')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def show_date(self, date):
        self.label.setText(date.toString())
        self.button.setEnabled(True)

    def show_image(self):
        self.label.setPixmap(QPixmap('images/' + self.label.text() + '.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())