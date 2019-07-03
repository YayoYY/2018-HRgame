import sys
import game

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = game.Ui_Form()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())