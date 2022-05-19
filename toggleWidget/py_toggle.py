from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyToggleButton(QCheckBox):
    def __init__(self, parent, **kargs):
        self._width = kargs.get('width', 60)
        self._height = kargs.get('height', 28)
        self._bg_color = kargs.get('bg_color', "#777")
        self._circle_color = kargs.get('circle_color', "#fff")
        self._active_color = kargs.get("active_color", "#077adf")
        self.animation_curve = kargs.get("animation_curve", QEasingCurve.InOutCirc)
        QCheckBox.__init__(self)
        
        # Setting Cursor and Sizes
        self.setFixedSize(self._width, self._height)
        self.setCursor(Qt.PointingHandCursor)
        self.stateChanged.connect(self.start_transitioning)
        
        # Creating Animations
        self._circle_position = 3
        self.animate = QPropertyAnimation(self, b"circle_position", self)
        self.animate.setEasingCurve(self.animation_curve)
        self.animate.setDuration(500) # MS
    @Property(float)
    def circle_position(self):
        return self._circle_position
    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()
    def start_transitioning(self, value):
        # Incase animation is running, stoping to avoid complications
        self.animate.stop()
        if value:
            value = self.width() - 26
        else:
            value = 3
        self.animate.setEndValue(value)
        self.animate.start()
        print("Status: {}".format(self.isChecked()))
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)
    def paintEvent(self, event: QPaintEvent):
        # Setting Up Painter and property
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        
        # Drawing Reactangle
        rect = QRect(0, 0, self.width(), self.height())
        if not self.isChecked():
            painter.setBrush(QColor(self._bg_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), 14, 14) # self.height() / 2
        
            # Creating Circle inside Box
            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(self._circle_position, 3, 22, 22)
        else:
            painter.setBrush(QColor(self._active_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), 14, 14) # self.height() / 2

            painter.setBrush(QColor(self._circle_color))
            painter.drawEllipse(self._circle_position, 3, 22, 22)
            
        # Ending Painter to avoid error
        painter.end()
        
class PyPushButton(QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self)
        
        self.setFixedSize(100, 30)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName("pushbutton")
        self.setStyleSheet("#pushbutton {color: #333; background-color: #fff; border-radius: 10px;} ")
        self.setText("Press to Exit")
        self.clicked.connect(exit)