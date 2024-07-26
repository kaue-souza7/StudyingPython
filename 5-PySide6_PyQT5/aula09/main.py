from PySide6.QtCore import Qt, QObject, Signal, QThread
from time import sleep
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_Form
import sys

class Worker1(QObject):
    started = Signal(str)
    progress = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = '0'
        self.started.emit('0')
        for i in range(5):
            value = str(i)
            self.progress.emit(value)
            sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.pushButton_2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.workker1Started)
        worker.progress.connect(self.workker1Progressed)
        worker.finished.connect(self.workker1Finished)

        thread.start()

    def workker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('Worker Iniciado')

    def workker1Progressed(self, value):
        self.label1.setText(value)
        print('Em progresso')

    def workker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('Worker finalizado')

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.workker2Started)
        worker.progress.connect(self.workker2Progressed)
        worker.finished.connect(self.workker2Finished)

        thread.start()

    def workker2Started(self, value):
        self.pushButton_2.setDisabled(True)
        self.label_2.setText(value)
        print('Worker2 Iniciado')

    def workker2Progressed(self, value):
        self.label_2.setText(value)
        print('2 Em progresso')

    def workker2Finished(self, value):
        self.pushButton_2.setDisabled(False)
        self.label_2.setText(value)
        print('Worker 2 finalizado')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()

    myWidget.show()
    app.exec()

