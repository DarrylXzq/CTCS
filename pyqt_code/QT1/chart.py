import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo

class PlotlyWidget(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = go.Figure(data=[go.Pie(labels=['Type 1', 'Type 2', 'Type 3', 'Type 4'], values=[10, 15, 20, 25])])
        self.setHtml(pyo.plot(self.figure, auto_open=False, output_type='div', include_plotlyjs='cdn'))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.plot_widget = PlotlyWidget()
        self.layout.addWidget(self.plot_widget)
        self.setWindowTitle('PyQt with Plotly')
        self.setGeometry(100, 100, 800, 600)

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
