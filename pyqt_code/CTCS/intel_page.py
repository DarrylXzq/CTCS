import time

import feedparser
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QThread, QPoint, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QTextEdit, QSpacerItem, QSizePolicy, QFrame,
                             QMessageBox, QStackedWidget, QScrollArea)
from PyQt5.QtGui import QPixmap, QIcon, QMovie, QFont

from model_page import create_button


def create_intel_button(icon_path, tooltip_text):
    """创建并返回一个配置好的按钮，带有鼠标悬停提示并自定义样式"""
    button = QPushButton()
    button.setIcon(QIcon(icon_path))
    button.setIconSize(QSize(100, 100))  # 设置图标大小
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


class CollectionThread(QThread):
    finished = pyqtSignal()  # 发送操作完成信号
    data_fetched = pyqtSignal(list)  # 用来发送数据的信号

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            # 执行传入的函数并获取结果
            result = self.func(*self.args, **self.kwargs)
            self.data_fetched.emit(result)  # 发送数据
            self.finished.emit()  # 发送完成信号
        except Exception as e:
            print(e)


class IntelPage(QWidget):
    warning_signal = pyqtSignal(str, str)
    progress_signal = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        intel_layout = QVBoxLayout()
        # ===================操作部分===================
        operate_layout = QHBoxLayout()

        self.rss_urls = [
            "https://www.zerodayinitiative.com/rss/published/",
            "https://rss.packetstormsecurity.com/",
            "https://www.exploit-db.com/rss.xml",
            "https://feeds.feedburner.com/TheHackersNews"
        ]

        self.start_collection = create_button('resource/figure/start.png', 'Start Detection',
                                              self.start_collection_task)

        self.start_collection_thread = CollectionThread(self.rss_crawler, self.rss_urls)
        self.start_collection_thread.data_fetched.connect(self.handle_data_fetched)
        self.start_collection_thread.finished.connect(self.on_collection_finished)  # 连接信号到完成处理函数

        self.warning_signal.connect(self.display_warning)  # 连接警告信号到槽函数
        # 连接信号
        self.progress_signal.connect(self.update_progress)

        # 添加GIF动画
        self.gif_label = QLabel()
        self.movie = QMovie("./resource/figure/loading.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.gif_label.setScaledContents(True)
        self.gif_label.setMaximumSize(150, 150)  # 根据实际GIF尺寸调整

        # 添加消息标签
        self.message_label = QLabel("✨Click the button to start intel collection✨")
        self.message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.message_label.setMaximumSize(750, 150)
        self.message_label.setFont(QFont("Times New Roman", 16, QFont.Bold))

        # 添加到布局
        operate_layout.addWidget(self.gif_label)
        operate_layout.addWidget(self.message_label)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        operate_layout.addSpacerItem(spacer)

        # 将按钮添加到布局中
        operate_layout.addWidget(self.start_collection)
        # ===================图表部分===================
        self.chart_layout = QHBoxLayout()
        self.chart_layout.setContentsMargins(0, 30, 0, 0)
        self.stacked_widget = QStackedWidget()
        # 创建导航按钮
        self.button_layout = QVBoxLayout()

        self.zeroday_button = create_intel_button('resource/figure/zeroday.png', 'Zero Day Initiative')
        self.pss_button = create_intel_button('resource/figure/pss.png', 'Packet Storm Security')
        self.exploit_button = create_intel_button('resource/figure/exploit.png', 'Exploit Database')
        self.TheHackersNews_button = create_intel_button('resource/figure/hacker.png', 'The Hackers News')

        self.zeroday_button.setEnabled(False)
        self.pss_button.setEnabled(False)
        self.exploit_button.setEnabled(False)
        self.TheHackersNews_button.setEnabled(False)

        buttons = [
            self.zeroday_button,
            self.pss_button,
            self.exploit_button,
            self.TheHackersNews_button
        ]

        for i, button in enumerate(buttons):
            button.clicked.connect(lambda checked, index=i: self.stacked_widget.setCurrentIndex(index))
            self.button_layout.addWidget(button)

        nav_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button_layout.addSpacerItem(nav_spacer)

        self.chart_layout.addWidget(self.stacked_widget)
        self.chart_layout.addLayout(self.button_layout)

        # ===================底部部分===================
        footer_layout = QHBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(True)  # 初始化时隐藏进度条
        self.progress_bar.setMinimumHeight(15)  # 设置最小高度
        self.progress_bar.setMaximumHeight(15)  # 设置最小高度
        self.progress_bar.setValue(0)  # 设置进度条的值
        self.progress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        footer_layout.addWidget(self.progress_bar)
        # ===================添加到主布局===================
        intel_layout.addLayout(operate_layout, 3)
        intel_layout.addLayout(footer_layout, 1)
        intel_layout.addLayout(self.chart_layout, 5)

        self.setLayout(intel_layout)

    def handle_data_fetched(self, data):
        # 处理从线程接收到的数据
        for entries in data:
            page = self.create_scrollable_page(entries)
            self.stacked_widget.addWidget(page)
        time.sleep(3)
        self.progress_signal.emit('🚀Data Processing completed! Waiting for operation...', 100)

    def create_scrollable_page(self, entries):
        scroll_area = QScrollArea()  # 创建滚动区域
        container = QWidget()  # 创建用于内容的容器
        layout = QVBoxLayout()

        for i, entry in enumerate(entries):  # 最多显示20条
            entry_widget = self.create_entry_widget(i, entry)
            layout.addWidget(entry_widget)

        container.setLayout(layout)
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)
        return scroll_area

    def create_entry_widget(self, num, entry):
        entry_layout = QVBoxLayout()
        entry_container = QWidget()
        entry_container.setLayout(entry_layout)

        # 设置基本样式
        entry_container.setStyleSheet("""
            QWidget {
                border: 2px solid black;
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
                background-color: #9E9E9E;
                transition: background-color 0.5s, transform 0.5s;
            }
            QWidget:hover {
                background-color: lightblue;  # 鼠标悬停时的背景色
                transform: scale(1.05);  # 放大效果
            }
        """)

        # 添加编号、标题、链接和发布日期
        num_label = QLabel(f'🔢 Number: #{num + 1}')
        title_label = QLabel(f'📝 Title: {entry.title}')
        link_label = QLabel(f'🔗 Link: <a href="{entry.link}">{entry.link}</a>')
        # 处理发布日期，移除时区部分
        pub_date_text = entry.published
        # 分割字符串以移除时区信息
        pub_date_text = pub_date_text.rsplit(' ', 1)[0]  # 假设时区总是在最后部分，通过空格分隔
        pub_date_label = QLabel(f'📅 Date: {pub_date_text}')

        # 设置标签样式
        labels = [num_label, title_label, link_label, pub_date_label]
        for label in labels:
            label.setStyleSheet("""
                QLabel {
                    font-family: 'Times New Roman';
                    font-weight: bold;
                    font-size: 11pt;
                    color: black;
                    background-color: rgba(255, 255, 255, 0.5);
                }
            """)
            label.setOpenExternalLinks(True)

        # 将每个QLabel添加到布局中
        entry_layout.addWidget(num_label)
        entry_layout.addWidget(title_label)
        entry_layout.addWidget(link_label)
        entry_layout.addWidget(pub_date_label)

        return entry_container

    def start_collection_task(self):
        # 禁用按钮，防止重复点击
        self.start_collection.setDisabled(True)
        self.zeroday_button.setEnabled(False)
        self.pss_button.setEnabled(False)
        self.exploit_button.setEnabled(False)
        self.TheHackersNews_button.setEnabled(False)
        # 启动线程
        self.start_collection_thread.start()

    def on_collection_finished(self):
        # 任务完成后，重新启用按钮
        self.start_collection.setEnabled(True)
        self.zeroday_button.setEnabled(True)
        self.pss_button.setEnabled(True)
        self.exploit_button.setEnabled(True)
        self.TheHackersNews_button.setEnabled(True)

    def display_warning(self, title, message):
        QMessageBox.warning(None, title, message)  # 在主线程中显示消息框

    def update_progress(self, message, value):
        self.slide_message(message)
        self.progress_bar.setValue(value)

    def slide_message(self, new_message):
        # 当前位置，用于结束动画
        final_position = self.message_label.pos()  # 获取当前位置作为动画结束位置
        # 动画的初始位置（从当前位置的正上方一小段距离开始）
        initial_position = QPoint(final_position.x(), final_position.y() - self.message_label.height() * 2)
        # 更新标签文本
        self.message_label.setText(new_message)
        self.message_label.move(initial_position)  # 设置初始位置

        # 创建动画对象
        self.animation = QPropertyAnimation(self.message_label, b"pos")
        self.animation.setDuration(500)  # 动画持续时间，单位为毫秒
        self.animation.setStartValue(initial_position)
        self.animation.setEndValue(final_position)  # 结束位置为当前位置
        self.animation.setEasingCurve(QEasingCurve.OutBounce)  # 使用弹跳效果
        self.animation.start()

    def rss_crawler(self, urls):
        self.progress_signal.emit("🔍Collecting data from RSS feeds...", 30)
        time.sleep(4)  # 模拟耗时操作
        self.progress_signal.emit('🧮Processing data...', 70)
        data = []
        for url in urls:
            feed = feedparser.parse(url)
            entries = feed.entries[:25]
            data.append(entries)
        return data
