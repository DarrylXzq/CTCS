import os
import sys

from PyQt5.QtCore import QSize, QTime, QTimer, QFileInfo
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
        # 模型列表部分
        model_list_layout = QVBoxLayout()
        self.table = QTableWidget(0, 6)  # 初始时有0行，6列
        self.table.setHorizontalHeaderLabels(['Model ID', 'Model Name', 'Size', 'Path', 'Added Time', 'Action'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().hide()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setFont(QFont("Times New Roman", 12, QFont.Normal))
        model_list_layout.addWidget(self.table)

        # 将布局添加到主布局中
        model_layout.addLayout(operate_layout, 2)
        model_layout.addLayout(model_list_layout, 5)
        self.setLayout(model_layout)

    def add_model_row(self, model_name, size, path, added_time, model_id):
        """添加一行模型信息到表格中"""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(model_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(size))
        self.table.setItem(row_position, 2, QTableWidgetItem(path))
        self.table.setItem(row_position, 3, QTableWidgetItem(added_time))
        self.table.setItem(row_position, 4, QTableWidgetItem(model_id))

        # 添加删除按钮
        btn_delete = QPushButton('Delete')
        btn_delete.clicked.connect(lambda: self.delete_model(row_position))
        self.table.setCellWidget(row_position, 5, btn_delete)

    def delete_model(self, row):
        """删除指定行的模型"""
        # 这里应添加实际的删除逻辑，比如从数据库删除模型
        self.table.removeRow(row)

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
        """刷新列表功能：获取指定目录下的特定扩展名的文件列表"""
        folder_path = QFileDialog.getExistingDirectory(self, "./resource/model/")
        if folder_path:
            for file_name in os.listdir(folder_path):
                if file_name.endswith(('.model', '.h5')):  # 假设 .model 和 .h5 为有效的扩展名
                    print(file_name)  # 实际应用中应更新到UI组件或记录下来

    def add_model(self):
        """添加模型功能：允许用户上传符合扩展名要求的模型，并获取其详细信息"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Model", "./resource/model/",
                                                   "Model File (*.model; *.h5)")
        if file_path:
            file_info = QFileInfo(file_path)
            model_name = file_info.fileName()
            file_size = file_info.size()
            creation_time = file_info.birthTime().toString("yyyy-MM-dd hh:mm:ss")
            model_id = 'ModelID'  # 此ID应从数据库生成或获取
            # TODO: 加入数据库
            QMessageBox.information(self, "模型已添加",
                                    f"名称: {model_name}\n大小: {file_size} 字节\n添加时间: {creation_time}\nID: {model_id}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelPage()
    window.show()
    sys.exit(app.exec_())
