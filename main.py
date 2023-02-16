import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.circles.append((random.randint(0, 500), random.randint(0, 500), *([random.randint(1, 50)] * 2)))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in self.circles:
            qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
            qp.drawEllipse(*i)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())