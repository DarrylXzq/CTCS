import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QTextEdit, QSpacerItem, QSizePolicy, QFrame)
from PyQt5.QtGui import QPixmap, QIcon, QMovie, QFont


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 主垂直布局
        main_layout = QVBoxLayout()

        # 主中间布局
        middle_layout = QHBoxLayout()

        # ===================导航栏部分===================
        nav_layout = QVBoxLayout()
        # 创建并设置按钮
        home_button = QPushButton()
        home_button.setIcon(QIcon('resource/figure/homepage.png'))  # 设置图标路径
        home_button.setIconSize(QSize(80, 80))  # 设置图标大小
        home_button.setFixedSize(110, 110)  # 设置按钮为正方形
        home_button.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; color: black;")

        model_button = QPushButton()
        model_button.setIcon(QIcon('resource/figure/model.png'))
        model_button.setIconSize(QSize(80, 80))
        model_button.setFixedSize(110, 110)
        model_button.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; color: black;")

        detect_button = QPushButton()
        detect_button.setIcon(QIcon('resource/figure/Detection.png'))
        detect_button.setIconSize(QSize(80, 80))
        detect_button.setFixedSize(110, 110)
        detect_button.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; color: black;")

        intel_button = QPushButton()
        intel_button.setIcon(QIcon('resource/figure/crawl.png'))
        intel_button.setIconSize(QSize(80, 80))
        intel_button.setFixedSize(110, 110)
        intel_button.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; color: black;")

        nav_layout.addWidget(home_button)
        nav_layout.addWidget(model_button)
        nav_layout.addWidget(detect_button)
        nav_layout.addWidget(intel_button)

        nav_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        nav_layout.addSpacerItem(nav_spacer)

        # 右边部分布局
        right_layout = QVBoxLayout()

        # ===================海报部分===================
        poster_label = QLabel()
        pixmap = QPixmap(r'resource/figure/poster.png')
        poster_label.setScaledContents(True)  # 保持图片的长宽比
        poster_label.setPixmap(pixmap.scaled(750, 400, Qt.KeepAspectRatio))  # 设置图片大小并保持长宽比
        right_layout.addWidget(poster_label, 2)

        content_notify_layout = QHBoxLayout()

        # ===================内容部分===================
        # 创建一个新的QWidget作为content_label的容器
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color:  #9E9E9E; border-radius: 10px;Color: black;")
        layout = QVBoxLayout(content_widget)  # 为这个widget设置一个垂直布局

        # 创建三个子标签并添加到布局中
        label1 = QLabel()
        label1.setText("""
            <h2 style='color: #616161;'>⭐<i>CTCS (Cyber Threat Cognition System)</i></h2>
            <p>🔹Includes two core components: Threat detection and intelligence collection.<br>
            🔹For the threat detection module, the system utilizes SVM, RF, and Bi-LSTM to achieve efficient threat identification.<br>
            🔹The intelligence collection module mainly gathers threat-related data from various security intelligence center websites through web crawling technology.</p>
        """)
        label1.setTextFormat(Qt.RichText)  # 设置文本格式为富文本

        label2 = QLabel()
        label2.setText("""
            <h2 style='color: #616161;'>📔<i>NSL-KDD Dataset</i></h2>
            <p>🔹A standard dataset for evaluating network intrusion detection systems.<br>
            🔹It includes various types of network attacks:<br>
            🔹Dos, Probe, U2R, and R2L.<br>
            🔹CTCS will specifically target these types of attacks for detection.</p>
        """)
        label2.setTextFormat(Qt.RichText)  # 设置文本格式为富文本

        label3 = QLabel()
        label3.setText("""
            <a href="https://github.com/DarrylXzq/CTCS_Code" style="text-decoration: none; color: black;">
                🫠GitHub Link：https://github.com/DarrylXzq/CTCS_Code
            </a>
        """)
        label3.setOpenExternalLinks(True)  # 确保超链接可点击
        label3.setTextFormat(Qt.RichText)  # 设置文本格式为富文本

        # 设置字体
        font = QFont("Times New Roman", 12, QFont.Bold)
        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(QFont("Times New Roman", 14, QFont.Bold))

        label1.setWordWrap(True)
        label2.setWordWrap(True)
        label3.setWordWrap(True)

        label1.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); border-radius: 10px; color: black;")
        label2.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); border-radius: 10px; color: black;")
        label3.setStyleSheet("background-color: rgba(255, 255, 255, 0.5); border-radius: 10px; color: black;")
        # 设置对齐方式
        label1.setAlignment(Qt.AlignLeft)
        label2.setAlignment(Qt.AlignLeft)
        label3.setAlignment(Qt.AlignCenter)

        # 添加标签到布局
        layout.addWidget(label1, 2)
        layout.addWidget(label2, 2)
        layout.addWidget(label3, 1)

        # 将这个content_widget添加到你的主布局中
        content_notify_layout.addWidget(content_widget, 6)

        # ===================通知部分===================
        notification_widget = QWidget()
        notification_widget.setStyleSheet("background-color:  #ae9a64; border-radius: 10px;Color: black;")
        layout_notify = QVBoxLayout(notification_widget)  # 为这个widget设置一个垂直布局

        # 设置notification_label
        notification_label = QLabel()
        notification_label.setText("""
            <h2 style='color: #616161;'>💡<i>Notification</i></h2>
            <p>🔹This project and its code may not be used for any form of commercial sales or services.<br>
            🔹The project must not be used as or embedded in any commercial product.<br></p>
            <h4 style='color: #616161;'>📧<i>Email: \nxiangzq.darryl@gmail.com<br></i></h4>
        """)
        notification_label.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0.5); border-radius: 10px; color: black;")
        notification_label.setFont(font)
        notification_label.setAlignment(Qt.AlignLeft)  # 文本左对齐
        notification_label.setTextFormat(Qt.RichText)  # 设置为富文本格式，以支持HTML

        notification_label.setWordWrap(True)

        layout_notify.addWidget(notification_label)
        content_notify_layout.addWidget(notification_widget, 2)

        right_layout.addLayout(content_notify_layout, 5)

        middle_layout.addLayout(nav_layout, 1)
        middle_layout.addLayout(right_layout, 8)

        main_layout.addLayout(middle_layout)

        # ===================底部部分===================
        footer_layout = QHBoxLayout()
        progress_bar = QProgressBar()
        progress_bar.setVisible(False)  # 初始化时隐藏进度条
        progress_bar.setMinimumHeight(15)  # 设置最小高度
        progress_bar.setMaximumHeight(15)  # 设置最小高度
        progress_bar.setValue(50)  # 设置进度条的值
        progress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        footer_layout.addWidget(progress_bar)
        main_layout.addLayout(footer_layout)

        # 主窗口设置
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 窗口标题
        self.setWindowTitle('CTCS')
        # 设置窗口图标
        self.setWindowIcon(QIcon(r'resource/figure/icon.png'))
        # 窗口大小调整
        self.resize(1400, 1075)
        # 设置窗口背景颜色
        self.setStyleSheet("color: black;")
        self.setStyleSheet("border: 5px solid #dcdcdc;")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomMainWindow()
    window.show()
    sys.exit(app.exec_())
