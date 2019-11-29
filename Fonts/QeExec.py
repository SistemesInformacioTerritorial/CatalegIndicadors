from Fonts.QeFont import QeFont
from typing import Callable, Iterable

class QeExec(QeFont):
    '''Font de dades resultat d'executar codi encapsulat en una funció'''
    def __init__(self,funcUnic: Callable[[],str]=None, funcLlista: Callable[[],Iterable[str]]=None, funcTaula: Callable[[],Iterable[Iterable[str]]]=None):
        self._funcUnic=funcUnic
        self._funcLlista=funcLlista
        self._funcTaula=funcTaula
    def getUnic(self) -> str:
        return self._funcUnic()
    def getLlista(self) -> Iterable[str]:
        return self._funcLlista()
    def getTaula(self) -> Iterable[Iterable[str]]:
        return self._funcTaula()

class QeExecExpr(QeFont):
    '''Font de dades resultat d'avaluar un string com a codi python. 
        ATENCIÓ! Cal anar amb molt de compte amb d'on surt aquest codi, ja que pot arribar a trencar el programa
        Millor no utilitzar-la si no s'està molt segur del que es fa'''
    def __init__(self,strUnic: str=None, strLlista: str=None, strTaula: str=None):
        self._unic=compile(strUnic,'unic','eval')
        self._llista=compile(strUnic,'unic','eval')
        self._taula=compile(strUnic,'unic','eval')
    def getUnic(self):
        return eval(self._unic)
    def getLlista(self):
        return eval(self._llista)
    def getTaula(self):
        return eval(self._taula)

if __name__=='__main__':
    def nombreAleatoriStr(min,max):
        import random
        return str(random.randint(min,max))
    font=QeExec(funcUnic=lambda: nombreAleatoriStr(1,1000))
    for i in range(5):
        print(font.getUnic())