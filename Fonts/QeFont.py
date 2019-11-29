from abc import ABC, abstractmethod
from typing import Iterable


class QeFont:
    '''Classe abstracta que permet obtenir dades d'una font de dades definida
       Les fonts poden ser (per exemple, i sense excloure'n d'altres):
        - SQL
        - Arxiu
        - URL
       Per fer una subclasse s'haurien d'implementar les funcions abstractes definides'''
    @abstractmethod
    def getUnic(self) -> str:
        pass

    @abstractmethod
    def getLlista(self) -> Iterable[str]:
        '''Retorna un iterable de strings'''
        pass

    @abstractmethod
    def getTaula(self) -> Iterable[Iterable[str]]:
        '''Retorna un iterable d'iterables de strings'''
        pass
