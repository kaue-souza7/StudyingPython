# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

buttom = QPushButton('''
                Example buttom with DocString
                    ''')
buttom.setStyleSheet('font-size: 40px; color: white; background: black;')
buttom.show()

buttom2 = QPushButton('BUTTOM')
buttom2.setStyleSheet('font-size: 40px; color: black; background: white;')
buttom2.show()

app.exec()