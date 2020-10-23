import sys
from PyQt5.QtWidgets import QApplication, QWidget

class OurApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CITIZEN CLASS PROJECT')
        self.move(300,300)
        self.resize(400,200)
        self.show()

if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    ex = OurApp()
    sys.exit(app.exec_())

