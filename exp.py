import sys
import gui

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt


def main(i):

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gui.Ui_Form()
    ui.setupUi(MainWindow, user_name, w, i)

    MainWindow.show()
    app.exec_()

if __name__ == '__main__':

    user_name = input('name=')
    w = input('w=')

    for i in range(6):
        print('round', i , 'begin')
        main(i)
