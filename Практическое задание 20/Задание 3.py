import sys
from PyQt5 import QtCore, QtWidgets, QtGui

def on_clicked():
    dialog = QtWidgets.QInputDialog(window)
    dialog.setWindowTitle('Это заголовок окна')
    dialog.setLabelText('Это текст подсказки')
    dialog.setOkButtonText('&Ввод')
    dialog.setCancelButtonText('&Отмена')
    dialog.setOption(QtWidgets.QInputDialog.UseListViewForComboBoxItems, on=True)
    dialog.setComboBoxItems(['Пункт 1', 'Пункт 2', 'Пункт 3'])
    result = dialog.exec_()
    if result == QtWidgets.QDialog.Accepted:
        print(dialog.textValue())
    else:
        print('Нажата кнопка Cancel')

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle('Вывод')
window.resize(300, 70)

button = QtWidgets.QPushButton('Отобразить диалоговое окно')
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)

window.setLayout(box)
window.show()

app.exec_()
