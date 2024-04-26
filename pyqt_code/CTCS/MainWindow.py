import sys

from PyQt5.QtCore import QSize, QTime, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QStackedWidget, QWidget, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QLabel
from home_page import HomePage
from model_page import ModelPage
from detect_page import DetectPage
from intel_page import IntelPage


def create_button(icon_path, tooltip_text):
    """创建并返回一个配置好的按钮，带有鼠标悬停提示并自定义样式"""
    button = QPushButton()
    button.setIcon(QIcon(icon_path))
    button.setIconSize(QSize(80, 80))  # 设置图标大小
    button.setFixedSize(110, 110)  # 设置按钮为方形
    # 设置按钮和工具提示的样式
    button.setStyleSheet("""
        QPushButton {
            background-color: rgb(255, 255, 255); 
            border-radius: 10px; 
            color: black;
            padding: 5px;
        }
        QPushButton::hover {
            background-color: #f0f0f0;
        }
        QToolTip {
            font-family: 'Times New Roman';
            font-weight: bold;
            font-size: 12pt;
            color: black; 
            background-color: white; 
            border: 1px solid black;
            padding: 6px;
            border-radius: 5px;
            opacity: 230;
        }
    """)
    button.setToolTip(tooltip_text)  # 设置提示文本
    return button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 窗口标题
        self.setWindowTitle('CTCS')
        # 设置窗口图标
        self.setWindowIcon(QIcon(r'resource/figure/icon.png'))
        # 窗口大小调整
        self.resize(1400, 1075)
        # 设置窗口背景颜色
        # self.setStyleSheet("color: black;")
        # self.setStyleSheet("border: 5px solid #dcdcdc;")

        # 创建 QStackedWidget
        self.stack_widget = QStackedWidget()

        # 创建并添加页面
        self.stack_widget.addWidget(HomePage())
        self.stack_widget.addWidget(ModelPage())
        self.stack_widget.addWidget(DetectPage())
        self.stack_widget.addWidget(IntelPage())

        # 创建导航按钮
        button_layout = QVBoxLayout()

        home_button = create_button('resource/figure/homepage.png', 'Home Page')
        model_button = create_button('resource/figure/model.png', 'Model Page')
        detect_button = create_button('resource/figure/Detection.png', 'Detection Page')
        intel_button = create_button('resource/figure/crawl.png', 'Intelligence Page')

        # 创建并设置按钮
        buttons = [
            home_button,
            model_button,
            detect_button,
            intel_button
        ]
        for i, button in enumerate(buttons):
            button.clicked.connect(lambda _, x=i: self.stack_widget.setCurrentIndex(x))
            button_layout.addWidget(button)

        nav_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_layout.addSpacerItem(nav_spacer)

        # 运行时间标签和定时器设置
        self.timer_label = QLabel("00:00:00")
        font = QFont("Times New Roman", 14, QFont.Bold)
        self.timer_label.setFont(font)
        self.timer_label.setStyleSheet("color: black;")
        button_layout.addWidget(self.timer_label)

        self.start_time = QTime(0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # 每1000毫秒更新一次，即每秒更新一次

        # 主布局
        layout = QHBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.stack_widget)

        # 设置中心小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_timer(self):
        """更新运行时间显示"""
        self.start_time = self.start_time.addSecs(1)
        self.timer_label.setText(self.start_time.toString("hh:mm:ss"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
