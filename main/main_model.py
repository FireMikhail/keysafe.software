import sys

from PyQt4 import QtGui

from main.design import main_design
from get_key.get_key_model import GetKeyWindow
from read_card.read_card_model import ReadCardWindow
from database.models import User, Key, UserKeyLink


class MainFirstWindow(QtGui.QMainWindow, main_design.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.get_keys_window = GetKeyWindow()
        self.get_key.clicked.connect(self.get_the_keys)

    def authenticate_user(self):
        # TODO: open scanning window for 30 sec
        # TODO: run scanning script
        # TODO: close after 30 second \ return bad answer \ get rights
        return

    def get_the_keys(self):
        # TODO: Open window with user auth
        self.get_keys_window.showFullScreen()

    def put_the_keys(self):
        # TODO: Add a window for put keys
        return


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainFirstWindow()
    form.showFullScreen()
    app.exec_()


if __name__ == '__main__':
    main()