from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from Fonts.QeFont import QeFont
from abc import ABC, abstractmethod


class QeView(QWidget):
    '''Classe abstracta que mostra les dades obtingudes des d'una QeFont
       La idea és fer-ne subclasses per crear coses com
        - Labels
        - Taules
        - Llistes'''

    def __init__(self, font: QeFont, tempsAct: int = None):
        '''Construeix una QeView '''
        super().__init__()
        self._lay = QVBoxLayout(self)
        self._lay.setContentsMargins(0,0,0,0)
        self.setLayout(self._lay)
        self._font = font
        if tempsAct is not None:
            self._timer = QTimer(self)
            self._timer.timeout.connect(self.setDades)
            self._temps = tempsAct
        self.setFont(QFont('Arial', 12))
        self.setStyleSheet('color: #38474f; background: #f9f9f9')
        # Definicions d'estil?

    @abstractmethod
    def setDades(self):
        pass

    def show(self):
        super().show()
        # if hasattr(self, '_timer'):
        #     self._timer.start(self._temps)
    def showEvent(self,event):
        super().showEvent(event)
        if hasattr(self, '_timer'):
            self._timer.start(self._temps)
    def hide(self):
        super().hide()
        if hasattr(self, '_timer'):
            self._timer.stop()
