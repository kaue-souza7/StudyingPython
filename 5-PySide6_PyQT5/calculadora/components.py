#------------------ VARIABLES ------------------
from pathlib import Path

ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / 'files'
WINDOW_ICON_PATH = FILES_DIR / 'calculator.png'

# # Colors
# PRIMARY_COLOR = '#1e81b0'
# DARKER_PRIMARY_COLOR = '#19232d'
# DARKEST_PRIMARY_COLOR = '#19232d'

PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'



# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 550





# --------------------- UTILS ---------------------

import re

NUM_OR_DOX_REGEX = re.compile(r'^[0-9.]$')

# print(NUM_OR_DOX_REGEX.search('2'))

def isNumOrDot(str: str):
    return bool(NUM_OR_DOX_REGEX.search(str))

def isValidNumber(string: str):
    valid = False
    try:
        convertToNumber(string)
        valid = True
    except ValueError:
        ...
    return valid


def isEmpty(str: str):
    return len(str) == 0


def convertToNumber(str: str):
    number = float(str)

    if number.is_integer():
        number = int(number)

    return number







# ------ INFO ---------
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt


class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)





#------------------------ STYLES --------------------
# QSS - Estilos do Qt for Python
# https://doc.qt.io/qtforpython-6/tutorials/basictutorial/widgetstyling.html
import qdarkstyle
# #19232d
qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
 
def setupTheme(app):
    # Aplicar o estilo escuro do qdarkstyle
    app.setStyleSheet(qdarkstyle.load_stylesheet())
 
    # Sobrepor com o QSS personalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + qss)




# -------------------- Buttons -----------------
from PySide6.QtWidgets import QPushButton, QGridLayout, QMessageBox
from PySide6.QtCore import Slot
import math


from main_window import MyWindow
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setItalic(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        if self.text() not in '0123456789. ':
            self.setStyleSheet(f'background-color: {PRIMARY_COLOR};')
        else:
            self.setStyleSheet(f'color: white;'
                               f'border: 2px solid gray;')
                            #    f'{self}:hover: #19232d;')
                            #    f'background-color: #19232d')
            

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: MyWindow, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window

        self._equation = ''
        self._equationInitialValue = 'Sua conta'

        self._left = None
        self._rigth = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)


    def _makeGrid(self):
        
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.opPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    self._configSpecialButton(button)
                
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, button_text,)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClicked(button, self._clear)
        
        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._configLeftOp, text)
                )
            
        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)
            
        if text == '=':
            self._connectButtonClicked(button, self._eq)
        
    @Slot()      
    def _makeSlot(self, func, *agrs, **kwargs):
        @Slot()
        def realSlot(_):
            func(*agrs, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newNumber = convertToNumber(displayText) * -1
        self.display.setText(str(newNumber))


    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return


        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._rigth = None
        self._op = None

        self.info.clear()
        self.display.clear()
        self.display.setFocus()

        self.equation = self._equationInitialValue

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text() # Deverá ser meu número _left
        self.display.clear() # Limpa o display

        self.display.setFocus()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return
        
        # Se houver algo no numero da erquerda
        # não famos nada. Aguardamos o número da direita
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()
        

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta.')
            return

        self._rigth = convertToNumber(displayText)
        # self._left: convertToNumber
        self.equation = f'{self._left} {self._op} {self._rigth}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._rigth) 
                # result = eval(self.equation.replace('^', '**'))
            else:
                result = eval(self.equation)
        except ZeroDivisionError: 
            self._showError('Division by zero.')
        except OverflowError:
            self._showError("I can't make the bill.")

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._rigth = None
        self._left = result

        self.display.setFocus()
        
        if result != 'error':
            self._left = None
    
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()
    
    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Close 
        )
        msgBox.exec()


    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Close 
        )
        msgBox.exec()
        
    
        








    