from QeFont import QeFont
from qgis.PyQt.QtSql import QSqlDatabase

class BaseDadesInvalida(ValueError):
    pass

class QeSQL(QeFont):
    def __init__(self,paramsBD: dict,consultaUnic: str='',consultaLlista: str='', consultaTaula: str=''):
        '''Construeix una font de dades que consulta un SQL. Només cal passar-li les consultes necessàries
        Arguments:
            paramsDB {dict} -- Paràmetres de la base de dades ('Database','HostName','Port','DatabaseName', 'UserName', 'Password'). Posar només els que calguin
        Keyword Arguments:
            consultaUnic {str} -- Consulta que retorna un únic element. Si en retorna més ho convertirà tot a un únic str (default: '') 
            consultaLlista {str} -- Consulta que retorna una llista d'elements. Si retornés una taula, convertirà cada fila en un str (default: '')
            consultaTaula {str} -- Consulta que retorna una taula d'elements (llista de llistes) (default: '') 
        '''
        self.setConsultaUnic(consultaUnic)
        self.setConsultaLlista(consultaLlista)
        self.setConsultaTaula(consultaTaula)
        if 'Database' not in paramsBD:
            raise BaseDadesInvalida('La base de dades passada com a paràmetre no és vàlida',"El diccionari hauria d'incloure un element 'Database'")
        self._paramsBD=paramsBD
    def setConsultaUnic(self,consulta):
        '''Dóna valor a la consulta per obtenir valors únics. Equival a passar-li com a paràmetre a la constructora'''
        self._consultaUnic=consulta
    def setConsultaLlista(self,consulta):
        '''Dóna valor a la consulta per obtenir una llista. Equival a passar-li com a paràmetre a la constructora'''
        self._consultaLlista=consulta
    def setConsultaTaula(self,consulta):
        '''Dóna valor a la consulta per obtenir una taula. Equival a passar-li com a paràmetre a la constructora'''
        self._consultaTaula=consulta
    def _connectaBD(self, Database=None, HostName=None, Port=None, DatabaseName=None, UserName=None, Password=None):
        #Per definició la crida serà self._connectaBD(**self._paramsBD). Els paràmetres s'agafaran del diccionari desempaquetat
        #Per aquesta raó, malgrat que en general les variables comencen per minúscula, com que hem definit que les claus del diccionari comencen per majúscula, ens cenyim a "practicality beats purity"
        self.db=QSqlDatabase.addDatabase(Database)
        if self.db.isValid():
            if HostName is not None:
                self.db.setHostName(HostName)
                if Port is not None:
                    self.db.setPort(Port)
            if DatabaseName is not None:
                self.db.setDatabaseName(DatabaseName)
            if UserName is not None:
                self.db.setUsername(UserName)
                if Password is not None:
                    self.db.setPassword(Password)
    def _obreBD(self):
        if not hasattr(self,'db'):
            self._connectaBD(**self._paramsBD)
        self.db.open()
    def _tancaBD(self):
        self.db.close()
        pass 
    def _consulta(self,cons):
        #Realitza la consulta com a tal a la base de dades
        #Retorna una llista de llistes amb els valors
        #Si les consultes estan ben fetes, els resultats haurien de ser de l'estil:
        #valor -> [[val]]
        #Llista -> [[v1],[v2],[v3],...]
        #Taula -> [[v11,v12,..],[v21,v22,...],...]
        self._obreBD()
        res=[]
        query=self.db.exec(cons)
        # query=self.db.exec('SELECT * from taula')
        while query.next():
            act=[query.value(i) for i in range(query.record().count())]
            res.append(act)
        self._tancaBD()
        return res

    def getUnic(self):
        '''Retorna un únic element com a resultat de fer una consulta'''
        res=self._consulta(self._consultaUnic)
        if len(res)>1:
            #Consulta mal definida. Retornem tot com a string (?)
            return str(res)
        else:
            if len(res[0])>1:
                #Consulta mal definida. Ídem que abans
                return str(res[0])
            else:
                return res[0][0]
    def getLlista(self):
        '''Retorna una llista d'elements com a resultat de fer una consulta'''
        res=self._consulta(self._consultaLlista)
        if not all(map(lambda x: len(x)==1, res)):
            #El resultat no és de la forma [[v],[v],[v]...]. Alguna llista interna té més d'un element
            return [x[0] if len(x)==1 else str(x) for x in res]
        else:
            return [x[0] for x in res] #Aplanem la llista de llistes perquè sigui una llista única
    def getTaula(self):
        '''Retorna una taula d'elements (llista de llistes) com a resultat de fer una consulta'''
        return self._consulta(self._consultaTaula)