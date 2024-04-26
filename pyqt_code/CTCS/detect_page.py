import warnings

import pandas as pd
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QTextEdit, QSpacerItem, QSizePolicy, QFrame, QComboBox,
                             QFileDialog, QMessageBox)
from PyQt5.QtGui import QPixmap, QIcon, QMovie, QFont
import os
from model_hasher import compute_hash, nested_dict, add_model_hash
from model_page import create_button
import preprocess
import pickle
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter


def use_add_model_hash():
    # ======================================================SVM======================================================
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'Original', 'No',
                   '596bde0e4965baaab179038c5efdb2a8711828c05c3d0c5e90d6fd03aa36c2f2', 'S,H1,H2')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'Pearson Correlation', 'No',
                   '723e739bc039755a4c8b305cd0f9586f528758cf91f3eb4a28c9f19b48b049a7', 'S,H1,H2,H3')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'Mutual Information', 'No',
                   'ae54cd3b9c9a38ee73338b8cd77d177fde99022cfdff0d4b2fc81afdd4f58860', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'Mutual Information', 'SMOTE',
                   '0b03a15a7d28a8a486bd5f84e6771d843292ad8e84b6405397cf570d9a8afe35', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'Mutual Information', 'ADASYN',
                   '7c32316b8e7c2a4d358af7833dd52691e8d966196a4704d62dad0b5f2243bd67', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'PCA', 'No',
                   '461e9e4a8b9f219e010420354baf2b797f4e744db17f85dc5fe264844ae0f333', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'PCA', 'SMOTE',
                   'aecd4fd5097b7aee69c3be079816dee4ed79f254a681ccb792e2ab82e243fe95', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'PCA', 'ADASYN',
                   '571dcb58f9d5c71bf59e75ddc0146a6af8baf2d03efc7131fef356e323d2cc35', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'SVM', 'One-Hot', 'LDA', 'No',
                   'faea37ebb4de9972c479f60d48c7282abd28d7b40d923e05e890112348781c6c', 'S,H1,H2,H6')

    add_model_hash(model_hashes, 'SVM', 'Label', 'Original', 'No',
                   'ec95ed765ba45164b26a74d4f05f7720a330d7d208cacf35d74ea45f659776f8', 'S,L1,L2')
    add_model_hash(model_hashes, 'SVM', 'Label', 'Pearson Correlation', 'No',
                   '97aa0219495a3719d7d51bd3c64fad2cf88a9a4f867bf36eae08794e300a3a2a', 'S,L1,L2,L3')
    add_model_hash(model_hashes, 'SVM', 'Label', 'Mutual Information', 'No',
                   '50b666cd28ddaa9b5e5ecbaddb157715c7ba73d60b72304e8d0d85ef6c4e7242', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'SVM', 'Label', 'Mutual Information', 'SMOTE',
                   '0a5ca30069cf53ef0d7b3080d62f6176e8a368708792e83334f470d03c82b49c', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'SVM', 'Label', 'Mutual Information', 'ADASYN',
                   'bb0d6672b937f546ccbfe38555d04d16ac70e3fb280821e0c0094aff57cd4904', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'SVM', 'Label', 'PCA', 'No',
                   '4fc603327508f7f3ac53b33ddbf0a4d43778741afba5697595c7b909763bf68d', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'SVM', 'Label', 'LDA', 'No',
                   'f0ec1bcb440ab22f6859ba2f764a062e8b64b13d1c469a1087e9441465e661df', 'S,L1,L2,L6')
    # ======================================================RF======================================================
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'Original', 'No',
                   'e3b7727d054f0e215dd446387ac6fc72883f26c876ba1edce2787dbb249f0a83', 'S,H1,H2')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'Pearson Correlation', 'No',
                   '6090453030769487dba523efefeae71c50334080ad27dab7656beaf7eb65fd8e', 'S,H1,H2,H3')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'Mutual Information', 'No',
                   'b6fc1756af3d73f50a3d073baa75a263d3ee25558feb3fc06352c43a59cec0a7', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'Mutual Information', 'SMOTE',
                   'dfd2d71da0f626cf5fb4a5c7896ede8dacbdaf48b165863da05ca3b7c29d44f1', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'Mutual Information', 'ADASYN',
                   '2ce55dce5f5cc15f282c9b9a1074c2faa5a0e9f9eec9623ecb98ff139d82b1a2', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'PCA', 'No',
                   'e7a1b38dbb0e1491658beb97410d88f19b6d04b1a40bd243c8fb0d1985106e3a', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'LDA', 'No',
                   '20e21fa5741bfc86254a1d96fffd5d104041a851cb0f472e73187188fa8d1642', 'S,H1,H2,H6')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'LDA', 'SMOTE',
                   '94cfb450a992253dcb360c6b9b28c8e9c087d7bc7626f6ebb14f0fd02343405d', 'S,H1,H2,H6')
    add_model_hash(model_hashes, 'RF', 'One-Hot', 'LDA', 'ADASYN',
                   'd1598d64128cb34422cf13455599a53920e25d5ff35fad39d9996086ade5f261', 'S,H1,H2,H6')

    add_model_hash(model_hashes, 'RF', 'Label', 'Original', 'No',
                   '0b489eed0e1aea535cd26fa89c86f982ba72dac0dd6bac92b9c32e52c2b1ad33', 'S,L1,L2')
    add_model_hash(model_hashes, 'RF', 'Label', 'Pearson Correlation', 'No',
                   '154a249c5ab8feb9445e8e60853a8e94cc12a7194f1fcb42bce63cf628b55b17', 'S,L1,L2,L3')
    add_model_hash(model_hashes, 'RF', 'Label', 'Mutual Information', 'No',
                   'fe61e682452e94a177269a112a2c626312d66836506b2f03912ece185c7eb177', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'RF', 'Label', 'Mutual Information', 'SMOTE',
                   '7899514d0803f025c785f3a9d58d3c8a0da87e56c74c6aef100064251ffffba6', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'RF', 'Label', 'Mutual Information', 'ADASYN',
                   'e57009db947fb2216183a8b230c53a342146c8f314de50429a73d4b2fbeacd19', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'RF', 'Label', 'PCA', 'No',
                   'be1c01c50ff35f2640e46eb5b782df144cb6893859b01452bb7894fdc9f844c6', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'RF', 'Label', 'PCA', 'SMOTE',
                   '9f18aa494da9460fc392a120e215cdb68de20811b0d46e2645c51f444fdc6932', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'RF', 'Label', 'PCA', 'ADASYN',
                   'b510ac715569247db8bade653add7be6f4b48758c03e19c3d893100299b450b9', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'RF', 'Label', 'LDA', 'No',
                   'a94c36620f1ed06597df03dc9dd07d2fbd13db2cf64a69bd056be0feb827ad63', 'S,L1,L2,L6')
    add_model_hash(model_hashes, 'RF', 'Label', 'LDA', 'SMOTE',
                   'a9386f0af64375da55af1d5e1116fa258ea800219bb9fb02e22a8712c4eac6e2', 'S,L1,L2,L6')
    add_model_hash(model_hashes, 'RF', 'Label', 'LDA', 'ADASYN',
                   '94ff77a4879ce8643ec7110be6f5e63ae2abd8c035ea76af663e7ab8f196c839', 'S,L1,L2,L6')
    # ======================================================LSTM======================================================
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'Original', 'No',
                   'e87f7f4d31e6d035d0a1dab04726d17e7a4032231ffd926237023ea8e380d154', 'S,H1,H2')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'Pearson Correlation', 'No',
                   'bff5dee2d2b0e2a96f54144a2ea45c74fc9d3e9a6a8c0eda83ae96b31b1e8d8b', 'S,H1,H2,H3')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'Mutual Information', 'No',
                   '6d6583f6716bd96d2da84c4f4be2f3ebc8f94593645fdec2affaf4013f71aa7a', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'Mutual Information', 'SMOTE',
                   '064785a4b47f103939f6620adc4c8038848cc324c2ed3c85bd99b46180de79a8', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'Mutual Information', 'ADASYN',
                   'd00f8818f7e93ae6296e7cc7037f2bd42dcdd1637e9254d582eb8b352eb8aa88', 'S,H1,H2,H4')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'PCA', 'No',
                   '745cfdcaf08fe4846b3e672edcbed060be2e36814d467033292bbb9e66e672c1', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'PCA', 'SMOTE',
                   '409b61fcfbf8fb2407582f86318b05cd2b51e683e41370750f2efcbbbc4fac43', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'PCA', 'ADASYN',
                   '8a51791f5989a830740d95024888b0f509b430019b3aa36117009a2730d4ee88', 'S,H1,H2,H5')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'LDA', 'No',
                   '5f58977be5c92617248fa52cb8ab34392a46fb3cbfffb90ed8cbff35e160552b', 'S,H1,H2,H6')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'LDA', 'SMOTE',
                   'b0794bc5f92caefc281c967754b324644c07fc58cb9287883130de7450acc93c', 'S,H1,H2,H6')
    add_model_hash(model_hashes, 'LSTM', 'One-Hot', 'LDA', 'ADASYN',
                   'dd16d360e2df4c1c98473fa8147f9b1cbe7f1b58bd3c451713f8ad6b28180f3b', 'S,H1,H2,H6')

    add_model_hash(model_hashes, 'LSTM', 'Label', 'Original', 'No',
                   '4324f3173796c1ca38b00a525cebbb2ced7ac00bcfe4233bc6dd1db69675c94e', 'S,L1,L2')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'Pearson Correlation', 'No',
                   'ff55b150385265e067a737563dc0ffe5d3fd8728854ab08528cf99f34395d2c3', 'S,L1,L2,L3')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'Mutual Information', 'No',
                   '7376696d81df4d0d35c4b68d75681731a4623f6999907376d44c5a35faf87cfd', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'Mutual Information', 'SMOTE',
                   '6d32c0024dc1ee7a08d2b13c6c5613fe58956251be6d3aef9621ba47c91d6c42', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'Mutual Information', 'ADASYN',
                   '4b5eb2dcd912511778c74db967bcb45c549aab585d580d09c5abc00c7b0875f2', 'S,L1,L2,L4')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'PCA', 'No',
                   'a700a9e44026561777aac3c6f50dbdf2e6e8e9c60292caefc5518fac33502697', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'PCA', 'SMOTE',
                   'b7deefa26c4c99002d12788c5551e21d9a7081b52b6fd43dc5fd37b98faa611f', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'PCA', 'ADASYN',
                   '9a8a3d82838df392fb12055960e8dede4ec577aaee65236dc5251392958e4bd9', 'S,L1,L2,L5')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'LDA', 'No',
                   '36a50e2318bd42f679c6c57ede4383e5d34a2c78dabd91e83d11453ea8a0b9b0', 'S,L1,L2,L6')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'LDA', 'SMOTE',
                   'bec8b3809e285205e45c2a1457acd7faf85d6cd33a9dd54a5f1a63d4bb76424d', 'S,L1,L2,L6')
    add_model_hash(model_hashes, 'LSTM', 'Label', 'LDA', 'ADASYN',
                   'c8fa46c48ea1d660698b26238932ed6fff00f4de94082341d024a2e87726fbef', 'S,L1,L2,L6')


model_hashes = nested_dict()
use_add_model_hash()


class WorkerThread(QThread):
    results_signal = pyqtSignal(list)

    def __init__(self, directory, valid_hashes):
        super(WorkerThread, self).__init__()
        # 获取当前执行文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 获取当前文件所在的目录
        current_dir = os.path.dirname(current_file_path)
        # 构建目标目录的路径，确保它是绝对路径
        self.directory = os.path.abspath(os.path.join(current_dir, directory))
        self.valid_hashes = valid_hashes

    def run(self):
        matching_models = []
        try:
            # 确认路径存在
            if not os.path.exists(self.directory):
                raise Exception(f"Directory does not exist: {self.directory}")
            files = os.listdir(self.directory)
        except Exception as e:
            print(f"Error listing directory {self.directory}: {e}")
            return
        for filename in files:
            if filename.endswith(('.h5', '.pkl')):
                file_path = os.path.join(self.directory, filename)
                # print(f"Processing {file_path}...")  # 确认文件路径输出
                try:
                    file_hash = compute_hash(file_path)
                    # print(f"Hash computed: {file_hash}")  # 显示计算出的哈希值
                except Exception as e:
                    print(f"Error computing hash for {file_path}: {e}")
                    continue
                if file_hash in self.valid_hashes:
                    matching_models.append(filename)
        self.results_signal.emit(matching_models)


class DetectionThread(QThread):
    finished = pyqtSignal()  # 发送操作结果和消息

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            # 执行传入的函数
            self.func(*self.args, **self.kwargs)
            self.finished.emit()
        except Exception as e:
            print(e)


match_prep_model = []
csv_file_path = ''
error_messages = []


def apply_preprocessing(data, steps):
    # 分割步骤字符串并遍历每一个步骤
    steps_list = steps.split(',')
    for step in steps_list:
        if step in preprocess.preprocessing_steps:
            data = preprocess.preprocessing_steps[step](data)
        else:
            print(f"No such preprocessing step: {step}")
    return data


class DetectPage(QWidget):
    warning_signal = pyqtSignal(str, str)
    progress_signal = pyqtSignal(str, int)
    def __init__(self):
        super().__init__()
        detect_layout = QVBoxLayout()
        # ===================模型选择部分================
        choice_layout = QVBoxLayout()

        combo_layout = QHBoxLayout()

        detect_label = QLabel("Model Selection")
        font = QFont("Times New Roman", 18, QFont.Bold)
        detect_label.setFont(font)
        detect_label.setStyleSheet("border: none;")
        choice_layout.addWidget(detect_label)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        choice_layout.addSpacerItem(spacer)

        # 初始化选择框
        self.model_type_combo = QComboBox()
        self.encoding_type_combo = QComboBox()
        self.preprocessing_combo = QComboBox()
        self.data_augmentation_combo = QComboBox()
        self.model_combo = QComboBox()

        # 添加选择框到布局
        self.setup_combobox_with_label('Type:', ['SVM', 'RF', 'LSTM'], combo_layout, self.model_type_combo)
        self.setup_combobox_with_label('Encoding:', ['Label', 'One-Hot'], combo_layout, self.encoding_type_combo)
        self.setup_combobox_with_label('Feature:',
                                       ['Original', 'LDA', 'PCA', 'Pearson Correlation', 'Mutual Information'],
                                       combo_layout, self.preprocessing_combo)
        self.setup_combobox_with_label('Augmentation:', ['No', 'SMOTE', 'ADASYN'], combo_layout,
                                       self.data_augmentation_combo)
        self.setup_combobox_with_label('Model:', [], combo_layout, self.model_combo)

        self.check_combos()
        self.connect_signals()
        choice_layout.addLayout(combo_layout)
        # ===================操作部分===================
        operate_layout = QHBoxLayout()
        operate_layout.setContentsMargins(0, 30, 0, 30)  # This sets 10 pixels margin on the top and bottom

        self.start_detection = create_button('resource/figure/start.png', 'Start Detection', self.start_detection_task)
        self.start_detection_thread = DetectionThread(self.check_variables_and_proceed)  # 创建线程实例
        self.start_detection_thread.finished.connect(self.on_detection_finished)  # 连接信号到完成处理函数

        self.stop_detection = create_button('resource/figure/stop.png', 'Stop Detection', self.detection_stop)
        self.stop_detection.setDisabled(True)  # 初始化时禁用停止按钮
        self.create_report = create_button('resource/figure/report.png', 'Create Report', self.create_report)
        self.create_report.setDisabled(True)  # 初始化时禁用报告按钮
        self.upload_csv = create_button('resource/figure/CSV.png', 'Upload CSV', self.upload_csv)
        self.upload_csv.setDisabled(False)

        self.warning_signal.connect(self.display_warning)  # 连接警告信号到槽函数
        # 连接信号
        self.progress_signal.connect(self.update_progress)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        operate_layout.addSpacerItem(spacer)

        # 创建显示GIF的标签
        self.gif_label = QLabel()
        self.movie = QMovie(".gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # 创建显示消息的标签
        self.message_label = QLabel("Readying the system...")
        self.message_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # 添加到布局
        operate_layout.addWidget(self.gif_label)
        operate_layout.addWidget(self.message_label)

        # 将按钮添加到布局中
        operate_layout.addWidget(self.upload_csv)
        operate_layout.addWidget(self.create_report)
        operate_layout.addWidget(self.stop_detection)
        operate_layout.addWidget(self.start_detection)

        # ===================图表部分===================
        self.chart_layout = QVBoxLayout()
        self.chart_container = QWidget()
        self.chart_container.setLayout(self.chart_layout)
        self.chart_container.setStyleSheet("""
                    QWidget {
                        border: 2px solid black;
                        border-radius: 5px;
                    }
                """)
        self.setup_chart()
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
        detect_layout.addLayout(choice_layout, 1)
        detect_layout.addLayout(operate_layout, 3)
        detect_layout.addWidget(self.chart_container, 5)
        detect_layout.addLayout(footer_layout, 1)

        self.setLayout(detect_layout)

    def start_detection_task(self):
        # 禁用按钮，防止重复点击
        self.start_detection.setDisabled(True)
        self.upload_csv.setDisabled(True)
        self.create_report.setDisabled(True)
        # 准备图表视图
        self.setup_chart()
        # 启动线程
        self.start_detection_thread.start()

    def on_detection_finished(self):
        # 任务完成后，重新启用按钮
        self.start_detection.setEnabled(True)
        self.upload_csv.setEnabled(True)

    def setup_combobox_with_label(self, label_text, items, layout, combo):
        """Creates a labeled combobox and adds it to the specified layout with custom styling."""
        # Vertical box layout for the label and combobox
        hbox = QHBoxLayout()
        # Create and style the label
        label = QLabel(label_text)
        label_font = QFont("Times New Roman", 11, QFont.Bold)  # Set label font (family, size, weight)
        label.setFont(label_font)
        label.setStyleSheet("color: gray;")  # Set label text color
        label.setAlignment(Qt.AlignCenter)  # Center the label text

        # Add items and set style for the combobox
        combo.addItems(items)
        combo_font = QFont("Times New Roman", 12)  # Set combobox font (simpler, smaller than label)
        combo.setFont(combo_font)
        combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 2px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }
        """)

        # Add the label and combobox to the vertical layout
        hbox.addWidget(label)
        hbox.addWidget(combo)

        # Add the vertical layout to the main layout
        layout.addLayout(hbox)

    def connect_signals(self):
        # Connect all relevant combo boxes to the check_combos method
        self.model_type_combo.currentIndexChanged.connect(self.check_combos)
        self.encoding_type_combo.currentIndexChanged.connect(self.check_combos)
        self.preprocessing_combo.currentIndexChanged.connect(self.check_combos)
        self.data_augmentation_combo.currentIndexChanged.connect(self.check_combos)

    def check_combos(self):
        # Check if all combo boxes have valid selections (not empty)
        if (self.model_type_combo.currentText() and
                self.encoding_type_combo.currentText() and
                self.preprocessing_combo.currentText() and
                self.data_augmentation_combo.currentText()):
            self.update_model_options()

    def get_combos(self):
        return (self.model_type_combo.currentText(),
                self.encoding_type_combo.currentText(),
                self.preprocessing_combo.currentText(),
                self.data_augmentation_combo.currentText())

    def update_model_options(self):
        type_choice, encoding_choice, preprocessing_choice, augmentation_choice = self.get_combos()

        # Assume 'model_hashes' is available and initialized elsewhere in your code
        try:
            models = model_hashes[type_choice][encoding_choice][preprocessing_choice][augmentation_choice]
            valid_hashes = [models['hash']]  # Adapt this line if your data structure differs
            # Start the thread
            self.thread = WorkerThread(r'./resource/model/', valid_hashes)
            self.thread.results_signal.connect(self.update_model_combo)
            self.thread.start()
        except KeyError:
            print("No models found for the selected options.")
            self.model_combo.clear()
            self.model_combo.addItem("No matching")

    def update_model_combo(self, matching_models):
        global match_prep_model
        self.model_combo.clear()
        if matching_models:
            self.model_combo.addItems(matching_models)
            type_choice, encoding_choice, preprocessing_choice, augmentation_choice = self.get_combos()
            match_prep_model.clear()
            match_prep_model.append(
                (type_choice, encoding_choice, preprocessing_choice, augmentation_choice, matching_models[0]))
            print('match_prep_model:', match_prep_model)

        else:
            self.model_combo.addItem("No matching")
            match_prep_model.clear()
            print('match_prep_model:', match_prep_model)

    def setup_chart(self):
        if not hasattr(self, 'chart'):
            self.series = QPieSeries()
            self.chart = QChart()
            self.chart.addSeries(self.series)
            self.chart.setTitle("Prediction Results")
            self.chart.setTitleFont(QFont("Times New Roman", 16))
            self.chart.legend().setVisible(True)
            self.chart.setFont(QFont("Times New Roman", 10))
            self.chart_view = QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.chart_layout.addWidget(self.chart_view)
        else:
            self.series.clear()  # 清除现有数据，准备新的数据填充

    def display_warning(self, title, message):
        QMessageBox.warning(None, title, message)  # 在主线程中显示消息框

    def update_progress(self, message, value):
        self.message_label.setText(message)
        self.progress_bar.setValue(value)

    def detection_start(self, prep, path):
        # 创建新的文件路径
        data = apply_preprocessing(csv_file_path, prep[0])
        X = data.to_numpy()
        with open(path, 'rb') as file:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                loaded_model = pickle.load(file)
        print("Loaded model from disk")
        y_pred = loaded_model.predict(X)
        order = {0: 'Normal', 1: 'DoS', 2: 'Probe', 3: 'R2L', 4: 'U2R'}
        self.show_results(y_pred, order)
        print('Detection over')
        # 检测完成后，重新启用按钮
        self.stop_detection.setEnabled(False)
        self.create_report.setEnabled(True)

    def check_csv_format(self, file_path):
        """检查无列名的CSV文件格式是否符合预设的要求"""
        try:
            # 读取CSV文件，不指定列名
            error_messages.clear()
            df = pd.read_csv(file_path, header=None)
            # 检查是否有41列
            if df.shape[1] != 41:
                error_messages.append(f"❗Error: Expected 41 columns, found {df.shape[1]}.")

            # 检查是否有空值
            if df.isnull().values.any():
                error_messages.append("❗Error: Missing values found in the CSV file.")

            # 数值范围设置
            ranges = {
                0: range(0, 57716),
                1: {'tcp', 'udp', 'icmp'},
                2: {'http', 'private', 'domain_u', 'smtp', 'ftp_data', 'other', 'telnet', 'eco_i', 'ecr_i', 'ftp',
                    'finger',
                    'pop_3', 'imap4', 'auth', 'Z39_50', 'uucp', 'courier', 'bgp', 'whois', 'iso_tsap', 'uucp_path',
                    'time',
                    'nnsp', 'vmnet', 'domain', 'ctf', 'urp_i', 'sunrpc', 'csnet_ns', 'http_443', 'supdup', 'gopher',
                    'discard', 'daytime', 'efs', 'link', 'systat', 'exec', 'name', 'hostnames', 'mtp', 'echo', 'klogin',
                    'login', 'netbios_dgm', 'ldap', 'netbios_ns', 'netstat', 'netbios_ssn', 'ssh', 'kshell', 'nntp',
                    'sql_net',
                    'IRC', 'ntp_u', 'X11', 'rje', 'remote_job', 'pop_2', 'shell', 'printer', 'pm_dump', 'tim_i',
                    'urh_i',
                    'red_i', 'tftp_u', 'http_8001', 'aol', 'harvest', 'http_2784'},
                3: {'SF', 'S0', 'REJ', 'RSTR', 'RSTO', 'S3', 'S1', 'SH', 'S2', 'RSTOS0', 'OTH'},
                4: range(0, 1379963889),
                5: range(0, 1309937402),
                6: {0, 1},
                7: {0, 1, 3},
                8: {0, 1, 2, 3},
                9: range(0, 102),
                10: range(0, 6),
                11: {0, 1},
                12: range(0, 7480),
                13: {0, 1},
                14: {0, 1, 2},
                15: range(0, 7469),
                16: range(0, 101),
                17: range(0, 6),
                18: range(0, 10),
                19: {0},
                20: {0, 1},
                21: {0, 1},
                22: range(0, 512),
                23: range(0, 512),
                24: [0, 1],
                25: [0, 1],
                26: [0, 1],
                27: [0, 1],
                28: [0, 1],
                29: [0, 1],
                30: [0, 1],
                31: range(0, 256),
                32: range(0, 256),
                33: [0, 1],
                34: [0, 1],
                35: [0, 1],
                36: [0, 1],
                37: [0, 1],
                38: [0, 1],
                39: [0, 1],
                40: [0, 1]
            }

            # 检查第2，3，4列的字符串是否有效
            for col in [1, 2, 3]:
                if not all(df[col].dropna().isin(ranges[col])):
                    invalid_entries = df[~df[col].isin(ranges[col])][col].dropna().unique()
                    error_messages.append(f"❗Error: Invalid entries in column {col}: {invalid_entries}")

            # 验证每个数值列的范围
            for col, valid_range in ranges.items():
                if isinstance(valid_range, range) or isinstance(valid_range, set):
                    invalid_values = [x for x in df[col].dropna() if x not in valid_range]
                    if invalid_values:
                        error_messages.append(f"❗Error in column {col} Values out of range")
                elif isinstance(valid_range, list):  # 对于浮点范围的简单处理
                    invalid_values = [x for x in df[col].dropna() if not (0 <= x <= 1)]
                    if invalid_values:
                        error_messages.append(f"❗Error in column {col} Values out of range 0-1")

            if error_messages:
                return False

            return True

        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return False

    def check_variables_and_proceed(self):
        # 检查 match_prep_model 是否为空以及 csv_file_path 是否为空或未指定
        if match_prep_model and csv_file_path:
            result_list = list(match_prep_model[0])
            model = model_hashes[result_list[0]][result_list[1]][result_list[2]][result_list[3]]
            valid_hashes = [model['hash']]
            new_path = './resource/model/' + result_list[4]
            file_hash = compute_hash(new_path)

            hash_matches = file_hash in valid_hashes
            csv_is_valid = self.check_csv_format(csv_file_path)

            if hash_matches and csv_is_valid:
                self.stop_detection.setDisabled(False)
                prep = [model['preprocessing']]
                self.detection_start(prep, new_path)
            else:
                message = ""
                if not hash_matches and not csv_is_valid:
                    message = "Both file hash and CSV format are invalid."
                elif not hash_matches:
                    message = "File hash is invalid."
                elif not csv_is_valid:
                    message = ("CSV format is not correct.\n" +
                               "\n".join(error_messages) +
                               "\n⚠️⚠️⚠️"
                               "\nThe uploaded CSV file must conform to the NSL-KDD dataset format (the last two columns of data are not required)\n"
                               "🔹The data consists of 41 columns (no header)\n"
                               "🔹There are no empty values in the data\n"
                               "🔹Each column of data conforms to the type and range specified by the NSL-KDD dataset\n")
                self.warning_signal.emit("Warning", message)  # 使用信号发射消息
        else:
            # 如果有一个或两个为空，则弹出消息框提醒用户
            message = ""
            if not match_prep_model and not csv_file_path:
                message = "Both model and csv file are empty."
            elif not match_prep_model:
                message = "model is empty."
            elif not csv_file_path:
                message = "csv file is empty."

            self.warning_signal.emit("Warning", message)  # 使用信号发射消息

    def show_results(self, predictions, order):
        self.series.clear()  # 清除之前的数据
        unique, counts = np.unique(predictions, return_counts=True)
        total = sum(counts)
        for pred, count in zip(unique, counts):
            percentage = 100 * count / total
            label = f"{order.get(pred, 'Unknown')}: {percentage:.2f}% ({count})"
            slice = QPieSlice(label, count)
            slice.setLabelFont(QFont("Times New Roman", 10))
            self.series.append(slice)

    def detection_stop(self):
        pass

    def create_report(self):
        pass

    def upload_csv(self):
        global csv_file_path  # 声明全局变量
        # 使用 QFileDialog 来让用户选择文件
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV file", "", "CSV Files (*.csv)", options=options)
        csv_file_path = ''
        # 检查用户是否选择了文件，同时检查路径是否为空
        if file_path:  # 如果 file_path 不为空，意味着用户选择了文件
            if file_path.lower().endswith('.csv'):
                # 记录选中的文件路径
                csv_file_path = file_path
            else:
                # 如果选中的文件不是 CSV，显示错误消息
                QMessageBox.warning(self, "File Type Error", "Please select a CSV file.")
        else:
            # 如果 file_path 为空，用户取消了选择或关闭了对话框，不执行任何操作
            print("No file selected or dialog closed.")
