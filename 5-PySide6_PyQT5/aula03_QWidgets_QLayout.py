# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

buttom = QPushButton('BUTTOM - 1')
buttom.setStyleSheet('font-size: 40px; color: black; background: white;')

buttom2 = QPushButton('BUTTOM - 2')
buttom2.setStyleSheet('font-size: 40px; color: black; background: white;')

buttom3 = QPushButton('BUTTOM - 3')
buttom3.setStyleSheet('font-size: 40px; color: black; background: white;')

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(buttom, 1, 1)
layout.addWidget(buttom2, 1, 2)
layout.addWidget(buttom3, 2, 1, 1, 2)

central_widget.show() # Central Widget entre na hierarquia e mostre sua janela

app.exec() # o loop da aplicação
