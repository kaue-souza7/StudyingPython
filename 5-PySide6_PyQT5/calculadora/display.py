from components import isEmpty, isNumOrDot
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from components import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    opPressed = Signal(str)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE*2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip() # 'a'
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOp = key in [
            KEYS.Key_Plus, 
            KEYS.Key_Minus, 
            KEYS.Key_Slash, 
            KEYS.Key_Asterisk,
            KEYS.Key_P
            ]

        if isEnter or text == '=':
            print(f'EQ "{text}" pressionado, sinal emitido!', self.__class__.__name__)
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            print('isDelete pressionado, sinal emitido!', self.__class__.__name__)
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            print('isEsc pressionado, sinal emitido!', self.__class__.__name__)
            self.clearPressed.emit()
            return event.ignore()
        
        if isOp:
            print('isOp pressionado, sinal emitido!', self.__class__.__name__)
            if text.lower() == 'p':
                text = '^'
            self.opPressed.emit(text)
            return event.ignore()
        
        # Não passar daqui se não tiver texto

        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            print('inputPressed pressionado, sinal emitido!', self.__class__.__name__)
            self.inputPressed.emit(text)
            return event.ignore()
        