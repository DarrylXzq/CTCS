from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QTextEdit, QSpacerItem, QSizePolicy, QFrame)
from PyQt5.QtGui import QPixmap, QIcon, QMovie, QFont

class DetectPage(QWidget):
    def __init__(self):
        super().__init__()
        # layout = QVBoxLayout()
        # label = QLabel("This is the Detection Page")
        # layout.addWidget(label)
        # self.setLayout(layout)
        # # ===================底部部分===================
        # footer_layout = QHBoxLayout()
        # progress_bar = QProgressBar()
        # progress_bar.setVisible(True)  # 初始化时隐藏进度条
        # progress_bar.setMinimumHeight(15)  # 设置最小高度
        # progress_bar.setMaximumHeight(15)  # 设置最小高度
        # progress_bar.setValue(50)  # 设置进度条的值
        # progress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        # footer_layout.addWidget(progress_bar)

        # model_layout.addLayout(footer_layout, 1)

        # layout.addWidget(label)
        # self.setLayout(layout)