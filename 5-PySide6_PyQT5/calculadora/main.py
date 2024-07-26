import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MyWindow
from components import WINDOW_ICON_PATH
from display import Display
from components import Info
from components import setupTheme
from components import Button, ButtonsGrid

# label1 = QLabel('My Text')
#     label1.setStyleSheet('font-size: 40px;')
#  window.addwidgetToVLayout(label1)



if __name__ == '__main__':
    # snake_case
    # PacalCase
    # camelCase

    # Cria Aplicação 
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MyWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)
    
    # Display
    display = Display('')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid) 

    # Button

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()

