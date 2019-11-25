from csv import reader
import sys
from QeFont import QeFont


class QeCSV(QeFont):
    def __init__(self, ruta):
        super().__init__()
        self._ruta = ruta

    def getUnic(self):
        pass

    def getLlista(self):
        pass

    def getTaula(self):
        with open(self._ruta) as f:
            r = reader(f)
            for row in r:
                print(row)
                yield row


if __name__ == '__main__':
    font = QeCSV(sys.argv[1])
    cont = font.getTaula()
    for x in cont:
        print(x)
