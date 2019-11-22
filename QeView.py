from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from QeFont import QeFont
from abc import ABC, abstractmethod
#No hauria de ser instanciada
class QeView(QWidget):
    def __init__(self, font: QeFont, tempsAct=None):
        '''Construeix una QeView '''
        super().__init__()
        self._lay=QVBoxLayout(self)
        self.setLayout(self._lay)
        self._font=font
        if tempsAct is not None:
            self._timer=QTimer(self)
            self._timer.timeout.connect(self.setDades)
            self._temps=tempsAct
        #Definicions d'estil?
    
    @abstractmethod
    def setDades(self):
        pass

    def show(self):
        super().show()
        if hasattr(self,'_timer'):
            self._timer.start(self._temps)
    def hide(self):
        super().hide()
        if hasattr(self,'_timer'):
            self._timer.stop()