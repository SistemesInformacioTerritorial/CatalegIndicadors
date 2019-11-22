from QeView import QeView
from QeFont import QeFont
from PyQt5.QtWidgets import QLabel


class QeLabel(QeView):
    def __init__(self, font: QeFont, titol: str, tempsAct: int = None):
        super().__init__(font, tempsAct)
        self._lay.addWidget(QLabel(titol))
        self._lbl = QLabel()
        self._lay.addWidget(self._lbl)
        self.setDades()

    def setDades(self):
        self._lbl.setText(str(self._font.getUnic()))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from QeSQL import QeSQL
    app = QApplication(sys.argv)
    # Obtenim el salari del treballador Oriol. Actualitzem cada 10000 ms (10 segons)
    font = QeSQL({'Database': 'QSQLITE', 'DatabaseName': 'exemple.db'},
                 consultaUnic='select salari from taula where nom="Oriol"; ')
    lbl = QeLabel(font, 'Salari Oriol', 10000)
    lbl.show()
    sys.exit(app.exec_())
