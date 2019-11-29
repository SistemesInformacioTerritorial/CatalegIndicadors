from Fonts.QeFont import QeFont
import json
from urllib.request import urlopen


class QeJSONBase(QeFont):
    def __init__(self, content, paramUnic, paramLlista, paramTaula):
        super().__init__()
        self.setJson(content)
        self._paramUnic = paramUnic
        self._paramLlista = paramLlista
        self._paramTaula = paramTaula

    def _get(self, params):
        self.setJson(self._getContingut())
        res = self._json
        for x in params:
            res = res[x]
        return res

    def setJson(self, content):
        self._content = content
        self._json = json.loads(self._content)

    def getUnic(self):
        return str(self._get(self._paramUnic))

    def getLlista(self):
        res = self._get(self._paramLlista)
        if isinstance(res, dict):
            res = res.values()
        return (str(x) for x in res)

    def getTaula(self):
        # Un JSON pot contenir arrays o diccionaris.
        # Per obtenir la taula arreglarem el resultat, agafant els valors dels diccionaris interns
        res = self._get(self._paramTaula)
        if isinstance(res, dict):
            res = res.values()
        res = (x if isinstance(x, list) else x.values() for x in res)
        return ((str(y) for y in x) for x in res)
    pass


class QeJSONFile(QeJSONBase):
    def __init__(self, ruta, paramUnic=[], paramLlista=[], paramTaula=[]):
        self._ruta = ruta
        content = self._getContingut()
        super().__init__(content, paramUnic, paramLlista, paramTaula)

    def _getContingut(self):
        with open(self._ruta, 'r') as f:
            return f.read()


class QeJSONWeb(QeJSONBase):
    def __init__(self, url, paramUnic=[], paramLlista=[], paramTaula=[]):
        self._url = url
        content = self._getContingut()
        super().__init__(content, paramUnic, paramLlista, paramTaula)

    def _getContingut(self):
        return urlopen(self._url).read()
    # def getUnic(self):
    #     self.setJson(self._getContingut())
    #     return super().getUnic()
    # def getLlista(self):
    #     self.setJson(self._getContingut())
    #     return super().getLlista()
    # def getTaula(self):
    #     self.setJson(self._getContingut())
    #     return super().getTaula()


if __name__ == '__main__':
    # Enllaç que dóna un json que és una llista d'un únic element on hi ha un diccionari on un dels paràmetres és una url amb una foto d'un gatet
    jsonWeb = QeJSONWeb('https://api.thecatapi.com/v1/images/search',
                        paramUnic=[0, 'url'], paramLlista=[0])
    for i in range(5):
        print(jsonWeb.getUnic())
    for i in range(5):
        print(jsonWeb.getLlista())
