# CatalegIndicadors
Sistema senzill per crear widgets que s'actualitzin a partir d'una font de dades. 
El sistema funciona ajuntant una vista i una font de dades. La vista obtindrà les dades que mostrarà a partir d'aquella font
## Fonts de dades
### QeFont
Classe base per les fonts de dades. Té els següents mètodes abstractes que han de ser escrits a les subclasses
#### Mètodes abstractes
* getUnic: Retorna un element únic
* getLlista: Retorna una llista d'elements
* getTaula: Retorna una taula (llista de llistes) d'elements
### QeSQL
Subclasse de QeFont per obtenir dades a partir d'una consulta SQL
#### QeSQL(params, consultaUnic, consultaLlista, consultaTaula)
1. params: Diccionari amb els paràmetres per la consulta (**'Database'**,'HostName','Port',**'DatabaseName'**, 'UserName', 'Password'). Només són obligatoris els que estan en negreta
2. consultaUnic: Consulta per obtenir un únic element
3. consultaLlista: Consulta per obtenir una llista
4. consultaTaula: Consulta per obtenir una taula
#### setConsultaUnic(consulta)
Setter per la consulta d'element únic. Equival a passar-li a la constructora
#### setConsultaLlista(consulta)
Setter per la consulta de llista. Equival a passar-li a la constructora
#### setConsultaTaula(consulta)
Setter per la consulta de taula. Equival a passar-li a la constructora

## Vistes
### QeView
Classe base per les vistes. Hereta de QWidget
#### Mètodes abstractes
* setDades: consultar a la font de dades i posar-li el resultat al widget
#### QeView(font: QeFont, tempsAct: int=None)
Construeix la base de l'estructura. Rep com a paràmetre la font de dades que farà servir (ha de ser una subclasse de QeFont) i el temps d'actualització si el widget s'ha d'anar actualitzant (temps en milisegons)
#### show()
Fa el show del widget i activa el timer si n'hi ha
#### hide()
Fa el hide del widget i desactiva el timer si n'hi ha

### QeLabel
Visualització de dades amb una label
#### QeLabel(font: QeFont, titol: str, tempsAct: int=None)
Mostrarà les dades obtingudes de la font en forma de label (cridant, per tant, getUnic). El widget resultant té un títol que etiqueta el contingut
#### setDades()
Crida getUnic de la font de dades i fa un setText a la seva label

## Exemple d'ús
```Python
    font=QeSQL({'Database':'QSQLITE','DatabaseName':'exemple.db'},consultaUnic='select salari from taula where nom="Oriol"; ')
    lbl=QeLabel(font,'Salari Oriol',10000) #Obtenim el salari del treballador Oriol. Actualitzem cada 10000 ms (10 segons)
    lbl.show()
```
