# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys
# QHBoxLayout, QVBoxLayout
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()

buttom = QPushButton('BUTTOM - 1')
buttom.setStyleSheet('font-size: 40px; color: black; background: white;')

buttom2 = QPushButton('BUTTOM - 2')
buttom2.setStyleSheet('font-size: 40px; color: black; background: white;')

buttom3 = QPushButton('BUTTOM - 3')
buttom3.setStyleSheet('font-size: 40px; color: black; background: white;')


central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(buttom, 1, 1)
layout.addWidget(buttom2, 1, 2)
layout.addWidget(buttom3, 2, 1, 1, 2)

def slot_example(sb):
    statusbar.showMessage('O meu slot foi exexutado')

# statusBar
statusbar = window.statusBar()
statusbar.showMessage('AQUI É A STATUS BAR')

# menuBar
menu =  window.menuBar()
first_menu = menu.addMenu('QUALQUER COISA')
first_action = first_menu.addAction('First Action')



first_action.triggered.connect(lambda: slot_example(statusbar)) 


window.show() 
app.exec() # o loop da aplicação
