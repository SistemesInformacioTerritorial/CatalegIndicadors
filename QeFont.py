from abc import ABC, abstractmethod


class QeFont:
    '''Classe abstracta que permet obtenir dades d'una font de dades definida
       Les fonts poden ser (per exemple, i sense excloure'n d'altres):
        - SQL
        - Arxiu
        - URL
       Per fer una subclasse s'haurien d'implementar les funcions abstractes definides'''
    @abstractmethod
    def getUnic(self):
        pass

    @abstractmethod
    def getLlista(self):
        pass

    @abstractmethod
    def getTaula(self):
        pass
