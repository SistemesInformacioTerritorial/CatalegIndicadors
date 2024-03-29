from QeView import QeView
from Fonts.QeFont import QeFont
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem, QSizePolicy
from PyQt5.QtCore import pyqtSignal, Qt


class QeTaula(QeView):
    elementclicat = pyqtSignal(object)
    elementdobleclicat = pyqtSignal(object)

    def __init__(self, font: QeFont, titol: str, tempsAct: int = None):
        super().__init__(font, tempsAct)
        self._lay.addWidget(QLabel(titol))
        self._taula = QTableWidget()
        self._taula.itemClicked.connect(
            lambda x: self.elementclicat.emit(x.data(Qt.DisplayRole)))
        self._taula.itemDoubleClicked.connect(
            lambda x: self.elementdobleclicat.emit(x.data(Qt.DisplayRole)))
        self.setDades()
        self._lay.addWidget(self._taula)

    def setDades(self):
        taula = self._font.getTaula()
        self._taula.setRowCount(len(taula))
        # Assumirem que totes les files tenen la mateixa longitud
        self._taula.setColumnCount(len(taula[0]))
        for i, x in enumerate(taula):
            for j, y in enumerate(x):
                self._taula.setItem(i, j, QTableWidgetItem(str(y)))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Fonts.QeSQL import QeSQL
    app = QApplication(sys.argv)
    # Obtenim el salari del treballador Oriol. Actualitzem cada 10000 ms (10 segons)
    font = QeSQL({'Database': 'QSQLITE', 'DatabaseName': 'exemple.db'},
                 consultaTaula='select nom, salari from taula;')
    taula = QeTaula(font, 'Treballadors', 10000)
    taula.elementclicat.connect(lambda x: print(x, 'clicat'))
    taula.elementdobleclicat.connect(lambda x: print(x, 'doble clicat'))
    taula.show()
    sys.exit(app.exec_())
