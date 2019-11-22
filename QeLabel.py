from QeView import QeView
from qgis.PyQt.QtWidgets import QLabel
class QeLabel(QeView):
    def __init__(self, font, titol, tempsAct=None):
        super().__init__(font,tempsAct)
        self._lay.addWidget(QLabel(titol))
        self._lbl=QLabel()
        self._lay.addWidget(self._lbl)
        self.setDades()
    def setDades(self):
        print('setDades')
        self._lbl.setText(str(self._font.getUnic()))

if __name__=='__main__':
    import sys
    from qgis.PyQt.QtWidgets import QApplication
    from QeSQL import QeSQL
    app = QApplication(sys.argv)
    font=QeSQL({'Database':'QSQLITE','DatabaseName':'exemple.db'},consultaUnic='select salari from taula where nom="Oriol"; ')
    lbl=QeLabel(font,'Salari Oriol',10000)
    lbl.show()
    sys.exit(app.exec_())