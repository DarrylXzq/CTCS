from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QTextEdit, QSpacerItem, QSizePolicy, QFrame)
from PyQt5.QtGui import QPixmap, QIcon, QMovie, QFont

class IntelPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is the Intelligence Page")
        layout.addWidget(label)
        self.setLayout(layout)