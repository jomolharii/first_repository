from  PyQt6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QGridLayout, QWidget, QFormLayout, QLineEdit, QApplication, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.setWindowTitle("GUI")
        self.container = QWidget()
        self.main_layout = QHBoxLayout()
        
        self.button = QPushButton("Click!")
        self.button1 = QPushButton("Reset")
        self.label = QLabel("Content")

        self.main_layout.addwidget(self.button)
        self.main_layout.addwidget(self.label)
        self.main_layout.setLayout(self.main_layout)
     
                              
app = QApplication([])


