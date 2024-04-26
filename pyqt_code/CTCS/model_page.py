import os
import shutil
import sys

from PyQt5.QtCore import QSize, QTime, QTimer, QFileInfo, QDateTime, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QStackedWidget, QWidget, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QLabel, QFileDialog, QMessageBox, QTableWidget, QHeaderView, QAbstractItemView, \
    QTableWidgetItem, QToolTip


def create_button(icon_path, tooltip_text, callback):
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
    button.clicked.connect(callback)
    return button


class ModelPage(QWidget):
    def __init__(self):
        super().__init__()
        model_layout = QVBoxLayout()
        # ===================操作部分===================
        operate_layout = QHBoxLayout()

        model_label = QLabel("Model Management")
        font = QFont("Times New Roman", 18, QFont.Bold)
        model_label.setFont(font)
        model_label.setStyleSheet("border: none;")
        operate_layout.addWidget(model_label)

        # 添加一个弹性空间推动所有按钮到右边
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        operate_layout.addSpacerItem(spacer)

        # 定义按钮
        open_folder_button = create_button('resource/figure/folder.png', 'Open Folder', self.open_model_file)
        refresh_list_button = create_button('resource/figure/refresh.png', 'Refresh List', self.refresh_list)
        add_model_button = create_button('resource/figure/add.png', 'Add Model', self.add_model)

        # 将按钮添加到布局中
        operate_layout.addWidget(open_folder_button)
        operate_layout.addWidget(refresh_list_button)
        operate_layout.addWidget(add_model_button)

        # ===================模型列表部分===================
        model_list_layout = QVBoxLayout()
        self.table = QTableWidget(0, 5)  # 初始时有0行，5列
        self.table.setHorizontalHeaderLabels(['Model Name', 'Size', 'Path', 'Added Time', 'Action'])
        self.table.verticalHeader().hide()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setFont(QFont("Times New Roman", 12, QFont.Bold))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # 第一列自动拉伸填充
        header.resizeSection(1, 150)
        header.resizeSection(2, 100)
        header.resizeSection(3, 250)
        header.resizeSection(4, 125)

        model_list_layout.addWidget(self.table)

        # 将布局添加到主布局中
        model_layout.addLayout(operate_layout, 2)
        model_layout.addLayout(model_list_layout, 5)
        self.refresh_list()  # 初始时刷新列表
        self.setLayout(model_layout)

    def add_model_row(self, model_name, size, path, added_time):
        """添加一行模型信息到表格中"""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(model_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(size))
        self.table.setItem(row_position, 2, QTableWidgetItem(path))
        self.table.setItem(row_position, 3, QTableWidgetItem(added_time))

        # 添加删除按钮
        btn_delete = QPushButton('Delete')
        btn_delete.clicked.connect(lambda: self.delete_model(row_position))
        # 设置样式表
        btn_delete.setStyleSheet("""
            QPushButton {
                background-color: #BB0020; /* 酒红色 */
                color: white; /* 文字颜色 */
                font-family: 'Times New Roman'; /* 字体 */
                font-size: 22px; /* 字体大小 */
                font-weight: bold; /* 字体粗细 */
                border-radius: 5px; /* 边角圆滑 */
                padding: 5px; /* 内边距 */
            }
            QPushButton:hover {
                background-color: #9A2E2E; /* 鼠标悬停时的颜色，稍亮的酒红色 */
            }
        """)
        self.table.setCellWidget(row_position, 4, btn_delete)

    def delete_model(self, row):
        """删除指定行的模型及其文件"""
        try:
            # 获取文件路径，假设路径在第4列（列索引从0开始，根据实际情况调整）
            file_path = self.table.item(row, 2).text()  # 调整索引为路径所在列
            # 检查文件是否存在并尝试删除
            if os.path.exists(file_path):
                os.remove(file_path)  # 删除文件
                self.table.removeRow(row)  # 如果文件删除成功，删除表格行
                QMessageBox.information(self, "Success", "Model and its file successfully deleted.")
            else:
                QMessageBox.warning(self, "Error", "File not found.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete the file. Error: {str(e)}")

    def open_model_file(self):
        """打开模型文件：允许用户选择.h5文件并打开"""
        start_dir = os.path.abspath("./resource/model/")
        if not os.path.exists(start_dir):
            os.makedirs(start_dir)  # 创建目录如果它不存在
        # 设置文件选择对话框只显示.h5文件
        file_path, _ = QFileDialog.getOpenFileName(self, "Model File", start_dir, "Model Files (*pkl; *.h5)")
        if file_path:
            # 这里可以添加你处理文件的逻辑
            os.startfile(file_path)  # 打开文件，或处理文件

    def refresh_list(self):
        """刷新模型列表：从指定目录获取模型文件信息并更新表格"""
        folder_path = os.path.abspath("./resource/model/")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)  # 创建目录如果它不存在
        if folder_path:
            self.table.setRowCount(0)  # 清空表格
            # 遍历文件夹中所有特定后缀的文件
            for file_name in os.listdir(folder_path):
                if file_name.endswith(('.pkl', '.h5')):
                    file_path = os.path.join(folder_path, file_name)
                    file_info = QFileInfo(file_path)
                    size_bytes = file_info.size()
                    size_mb = size_bytes / 1024 / 1024  # 转换为MB
                    size_mb = f"{size_mb:.2f} MB"  # 格式化为2位小数的字符串
                    # 使用文件的最后修改时间
                    added_time = file_info.birthTime().toString("yyyy-MM-dd hh:mm:ss")
                    # 更新表格显示
                    self.add_model_row(file_name, size_mb, file_path, added_time)

    def add_model(self):
        """添加模型功能：允许用户上传符合扩展名要求的模型，并将其复制到指定目录，检查是否有同名文件"""
        target_directory = "./resource/model/"  # 指定目标文件夹
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Model", target_directory,
                                                   "Model File (*.pkl; *.h5)")
        if file_path:
            file_info = QFileInfo(file_path)
            model_name = file_info.fileName()
            destination_path = os.path.join(target_directory, model_name)

            # 检查目标目录是否存在，如果不存在则创建
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # 检查是否有同名文件存在
            if os.path.exists(destination_path):
                QMessageBox.warning(self, "Error",
                                    "A model with the same name already exists. Please rename the file or choose a different file.")
            else:
                # 尝试复制文件到目标目录
                try:
                    shutil.copy(file_path, destination_path)
                    file_size = f"{file_info.size() / 1024 / 1024:.2f} MB"  # 文件大小转换为MB，并格式化为2位小数的字符串
                    creation_time = file_info.birthTime().toString("yyyy-MM-dd hh:mm:ss")
                    self.refresh_list()  # 刷新列表显示
                    QMessageBox.information(self, "Model Added",
                                            f"Name: {model_name}\nSize: {file_size}\nAdded Time: {creation_time}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Cannot copy the file: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelPage()
    window.show()
    sys.exit(app.exec_())
