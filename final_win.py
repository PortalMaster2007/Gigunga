from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *
class FinalWin(QWidget):
    def __init__(self, exp):
       super().__init__()
       self.exp = exp
       self.result()
       self.initUI()
       self.set_appear()
       self.show()

    def initUI(self):
       self.workh_text = QLabel(txt_workheart + self.results())
       self.index_text = QLabel(txt_index + str(self.index))
       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        self.index = (4*(int(self.exp.test1)+int(self.exp.test2)+int(self.exp.test3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            elif self.index < 0.5:
                return txt_res5