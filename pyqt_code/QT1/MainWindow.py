import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QListWidget, QHBoxLayout, QHeaderView, QStackedWidget,
    QPushButton, QLineEdit, QFormLayout, QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # Set the main window properties
        self.setWindowTitle('2.6.16')
        self.setGeometry(100, 100, 1314, 768)
        self.setStyleSheet("background-color: #2c2c2c; color: #dcdcdc;")

        # Create the main layout and stacked widget
        main_layout = QHBoxLayout()
        self.stacked_widget = QStackedWidget()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Create the sidebar
        self.sidebar = QListWidget()
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #333;
                color: white;
                border: none;
            }
            QListWidget::item:selected {
                background-color: #555;
            }
        """)
        self.sidebar.setMaximumWidth(200)
        self.sidebar.currentItemChanged.connect(self.display_page)

        # Populate the sidebar with icons and text
        self.sidebar.addItem('🏠 Home')
        self.sidebar.addItem('⚙ Settings')
        self.sidebar.addItem('🔐 Login')
        self.sidebar.addItem('📝 Register')
        # add other sidebar items

        # Add sidebar to the main layout
        main_layout.addWidget(self.sidebar)

        # Create the main content area
        main_layout.addWidget(self.stacked_widget)

        # Create the table page, settings page, login page, and register page
        self.create_table_page()
        self.create_settings_page()
        self.create_login_page()
        self.create_register_page()

    def create_table_page(self):
        # Create the table page
        table_page = QWidget()
        table_layout = QVBoxLayout(table_page)

        # Create the table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(25)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            'Model Name', 'Model Type', 'Author', 'Model Description',
            'Model Size', 'Creation Time', 'Actions'
        ])
        self.tableWidget.horizontalHeader().setStyleSheet("color: #dcdcdc;")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: none;
                selection-background-color: #3a3a3a;
            }
            QTableWidget::item {
                border-bottom: 1px solid #444;
            }
        """)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Fill the table with dummy data
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row, column, QTableWidgetItem(f'Item {row},{column}'))

        # Add the table to the table layout
        table_layout.addWidget(self.tableWidget)

        # Add the table page to the stacked widget
        self.stacked_widget.addWidget(table_page)

    def create_settings_page(self):
        # Create the settings page
        settings_page = QWidget()
        settings_layout = QFormLayout(settings_page)

        # Add settings inputs
        settings_layout.addRow("Username:", QLineEdit())
        settings_layout.addRow("Password:", QLineEdit())
        settings_layout.addRow(QPushButton('Save Settings'))

        # Add the settings page to the stacked widget
        self.stacked_widget.addWidget(settings_page)

    def create_login_page(self):
        # Create the login page
        login_page = QWidget()
        login_layout = QFormLayout(login_page)
        login_layout.addRow("Username:", QLineEdit())
        login_layout.addRow("Password:", QLineEdit())
        login_layout.addRow(QPushButton('Login'))
        self.stacked_widget.addWidget(login_page)

    def create_register_page(self):
        # Create the register page
        register_page = QWidget()
        register_layout = QFormLayout(register_page)
        register_layout.addRow("Username:", QLineEdit())
        register_layout.addRow("Password:", QLineEdit())
        register_layout.addRow("Confirm Password:", QLineEdit())
        register_layout.addRow(QPushButton('Register'))
        self.stacked_widget.addWidget(register_page)

    def display_page(self, current, previous):
        # Change the displayed page in the stacked widget based on selection
        if current:
            index = {
                '🏠 Home': 0,
                '⚙ Settings': 1,
                '🔐 Login': 2,
                '📝 Register': 3
            }.get(current.text(), 0)
            self.stacked_widget.setCurrentIndex(index)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use the Fusion theme, suitable for dark themes
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
