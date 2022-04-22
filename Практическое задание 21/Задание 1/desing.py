import sys
from PyQt5 import QtWidgets
import app

class ExampleApp(QtWidgets.QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listView.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory:
            for file_name in sys.listdir(directory):
                self.listView.addItem(file_name)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ExampleApp()
    win.show()
    sys.exit(app.exec_())