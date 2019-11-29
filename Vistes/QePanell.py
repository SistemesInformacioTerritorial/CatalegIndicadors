from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from Vistes.flowlayout import FlowLayout
from abc import abstractmethod

class QePanell(QFrame):
    def __init__(self, parent=None, f=Qt.WindowFlags()):
        super().__init__(parent,f)
        self._setUp()
        #self._lay=QVBoxLayout(self,parent)
        self.setLayout(self._lay)
    @abstractmethod
    def _setUp(self):
        #Cal que la funció instanciï self._lay com a layout
        pass
    def afegir(self,wid: QWidget):
        self._lay.addWidget(wid)

class QePanellV(QePanell):
    '''Panell que distribueix els widgets afegits de manera vertical'''
    def _setUp(self):
        self._lay=QVBoxLayout(self,self.parentWidget())

class QePanellH(QePanell):
    '''Panell que distribueix els widgets afegits de manera horitzontal'''
    def _setUp(self):
        self._lay=QHBoxLayout(self,self.parentWidget())

class QePanellG(QePanell):
    '''Panell que distribueix els widgets afegits en graella. Cal indicar-li les posicions x y on es vol posar'''
    def _setUp(self):
        self._lay=QGridLayout()
    def afegir(self,widget):
        pass
    def afegir(self, widget, i, j):
        self._lay.addWidget(widget, i, j)

class QePanellA(QePanell):
    '''Panell que distribueix els widgets afegits automàticament aprofitant un flowlayout'''
    def _setUp(self):
        self._lay=FlowLayout(self)

if __name__=='__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Fonts.QeJSON import QeJSONWeb
    from Vistes.QeImatge import QeImatgeURL
    app = QApplication(sys.argv)
    # Enllaç que dóna un json que és una llista d'un únic element on hi ha un diccionari on un dels paràmetres és una url amb una foto d'un gatet
    jsonWeb = QeJSONWeb('https://api.thecatapi.com/v1/images/search',
                        paramUnic=[0, 'url'], paramLlista=[0])
    imatge1 = QeImatgeURL(jsonWeb, tempsAct=10000)
    imatge1.setMinimumWidth(500)
    imatge2 = QeImatgeURL(jsonWeb, tempsAct=15000)
    imatge2.setMinimumWidth(500)
    imatge3 = QeImatgeURL(jsonWeb, tempsAct=20000)
    imatge3.setMinimumWidth(500)
    imatge4 = QeImatgeURL(jsonWeb)
    imatge4.setMinimumWidth(500)

    # panell=QePanellG()
    # panell.afegir(imatge1,0,0)
    # panell.afegir(imatge2,0,1)
    # panell.afegir(imatge3,1,0)
    # panell.afegir(imatge4,1,1)

    panell=QePanellA()
    panell.afegir(imatge1)
    panell.afegir(imatge2)
    panell.afegir(imatge3)
    panell.afegir(imatge4)
    panell.show()
    sys.exit(app.exec_())