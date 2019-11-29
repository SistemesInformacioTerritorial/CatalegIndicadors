from Vistes.QeLabel import QeLabel
from Fonts.QeFont import QeFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import urllib


class QeImatge(QeLabel):
    def setPixmap(self,pixmap):
        self._pixmap=pixmap
        self._posaImatge()
    def _posaImatge(self):
        self._lbl.setPixmap(self.pixmapEscalat())
    def resizeEvent(self, event):
        if hasattr(self,'_pixmap'):
            self._posaImatge()
        pass
    def pixmapEscalat(self):
        return self._pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)


class QeImatgeURL(QeImatge):
    def setDades(self):
        url = self._font.getUnic()
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.setPixmap(pixmap)


class QeImatgeFile(QeImatge):
    def setDades(self):
        pixmap = QPixmap(self._font.getUnic())
        self._posaImatge(pixmap)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from Fonts.QeJSON import QeJSONWeb
    app = QApplication(sys.argv)
    # Enllaç que dóna un json que és una llista d'un únic element on hi ha un diccionari on un dels paràmetres és una url amb una foto d'un gatet
    jsonWeb = QeJSONWeb('https://api.thecatapi.com/v1/images/search',
                        paramUnic=[0, 'url'], paramLlista=[0])
    lbl = QeImatgeURL(jsonWeb, tempsAct=10000)
    lbl.show()
    sys.exit(app.exec_())
