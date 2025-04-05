from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit
)

from instr import *

class TestWin(QWidget):
    def __init__(self): 
        super().__init__() 
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.resize(1500, 900)
        self.move(300, 50)

    def initUI(self):
       self.txt_name = QLabel('Введите Ф.И.О.:')
       self.line_edit = QLineEdit("Ф.И.О.")
       self.txt_age = QLabel('Полных лет:')
       self.age = QLineEdit("0")
       self.txt_test1 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
       self.button1 = QPushButton('Начать первый тест', self) 
       self.txt_test2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
       self.button2 = QPushButton('Начать делать приседания', self) 
       self.txt_test3 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
       self.button3 = QPushButton('Начать финальный тест', self) 
       self.buttn = QPushButton('Отправить результаты')
       self.txt_timer = QLabel('') 
       self.test1 = QLineEdit('0')
       self.test2 = QLineEdit('0')
       self.test3 = QLineEdit('0')
       self.l_line = QVBoxLayout()
       self.r_line = QVBoxLayout()
       self.h_line = QHBoxLayout()
       self.r_line.addWidget(self.txt_timer, alignment = Qt.AlignCenter)
       self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.line_edit, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.button1, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.button2, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
       self.l_line.addWidget(self.button3, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft) 
       self.l_line.addWidget(self.buttn, alignment = Qt.AlignCenter)
       self.h_line.addLayout(self.l_line)
       self.h_line.addLayout(self.r_line)
       self.setLayout(self.h_line)

    def next_click(self):
        self.tw = Mainwin() 
        self.hide()

    def connects(self):
        self.button1.clicked.connect(self.next_click)