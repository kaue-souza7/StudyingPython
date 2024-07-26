from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configuraando o Layout Básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.setCentralWidget(self.cw)
        self.cw.setLayout(self.vLayout)

        # Titulo Janela
        self.setWindowTitle('Calculadora')

        

        # Última coisa a ser feita
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())


    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)