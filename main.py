from PySide6 import QtCore, QtGui, QtWidgets
from toggleWidget import PyToggleButton, PyPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 437)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(610, 440))
        MainWindow.setStyleSheet("QMainWindow {\n"
            "background-color: #222;\n"
            "}"
        )
        MainWindow.setWindowFlags(QtGui.Qt.FramelessWindowHint | QtGui.Qt.WindowStaysOnTopHint)
        # MainWindow.center()
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = PyToggleButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = PyPushButton(self.centralwidget) # Establizing
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.oldPos = MainWindow.pos()
        self.MainWindow.mousePressEvent = self.mousePressEvent
        self.MainWindow.mouseMoveEvent = self.mouseMoveEvent
        self.MainWindow.mouseReleaseEvent = self.mouseReleaseEvent
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def mouseReleaseEvent(self, event):
        self.MainWindow.setCursor(QtCore.Qt.ArrowCursor)
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.MainWindow.setCursor(QtCore.Qt.OpenHandCursor)
        self.oldPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        delta = QtCore.QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.MainWindow.move(self.MainWindow.x() + delta.x(), self.MainWindow.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()
        self.MainWindow.setCursor(QtCore.Qt.ClosedHandCursor)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
