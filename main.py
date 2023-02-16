import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.circles.append((random.randint(0, 500), random.randint(0, 500), *([random.randint(1, 50)] * 2)))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        for i in self.circles:
            qp.drawEllipse(*i)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())