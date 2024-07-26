# Trabalhando com classes e heranças
import sys
# QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.buttom = self.mk_btn('Texto do Botão')
        self.buttom.clicked.connect(self.segunda_acao_marcada)
        
        self.buttom2 = self.mk_btn('Buttom - 2')

        self.buttom3 = self.mk_btn('Buttom - 3')


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('APP COURSE')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.buttom, 1, 1)
        self.grid_layout.addWidget(self.buttom2, 1, 2)
        self.grid_layout.addWidget(self.buttom3, 2, 1, 1, 2)

        # statusBar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('HERE IS STATUSBAR')

        # menuBar
        self.menu =  self.menuBar()
        self.first_menu = self.menu.addMenu('Menu - 1')

        self.first_action = self.first_menu.addAction('First Action')
        self.first_action.triggered.connect(self.mensagem_statusbar) 

        self.action2 = self.first_menu.addAction('Action - 2')
        self.action2.setCheckable(True)
        self.action2.toggled.connect(self.segunda_acao_marcada)
        self.action2.hovered.connect(self.segunda_acao_marcada)

        


    @Slot()
    def mensagem_statusbar(self, sb):
        self.statusbar.showMessage('My slot ran')
        

    @Slot()
    def segunda_acao_marcada(self):
        # statusbar.showMessage('My slot ran')
        print('ESTÁ MARCADO?', self.action2.isChecked())

    def mk_btn(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 40px; color: black; background: white;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show() 
    app.exec() # o loop da aplicação
