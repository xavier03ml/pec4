# COVID Approval Checker (PEC 4)
Este paquete de Python tiene como objetivo resolver las actividades indicadas en la PEC 4
## Dependencias
  - Python 3.6+
  - Pandas 1.2.4+
  - Matplotlib 3.0+
  - Coverage 5.5+

## Construir desde la fuente
Desde el directorio _pec_ ejecutar 
```python
python -m build
```
Se creará el paquete _whl_ con los respectivos requerimientos a instalar.

## Instalación
Para instalar el paquete _whl_ desde nuestro sistema de archivos local usamos la siguiente instrucción.
```python
python -m pip install dist/covid_approval_checker-0.0.1-py3-none-any.whl
```
## Tests
Para correr los tests sobre el código fuente debe ejecutarse la siguiente instrucción desde el directorio ```tests``` dentro del directorio del código fuente ```covid_approval_checker```.
```python
python -m unitest discover -s tests
```
Para los tests de covertura ejecutar 
```python
coverage run -m unittest discover -s tests
coverage report
```
El cuál nos da un 88% de cobertura.

## Uso
Para poder hacer uso de la librería, se debe importar las funciones e instanciar un objeto de la clase
```ApprovalChecker``` el cuál recibe 3 parámetros:
1. ```approval_polls_path``` (ruta del dataset _approval_polls_)
2. ```concern_polls_path``` (ruta del dataset _concern_polls_)
3. ```pollster_ratings_path``` (ruta del dataset _pollster_ratings_)
```python
from covid_approval_checker import functions as f

ac = f.ApprovalChecker('C:/ds/covid_approval_polls.csv',
                       'C:/ds/covid_concern_polls',
                       'C:/ds/pollster_ratings.xlsx')
```
Luego los datasets deben ser preparados (cargados) por medio del método _preparar_datasets_, si los datasets fueron
cargados correctamente, el atributo _ready_ del objeto pasa a ser ```True```. Adicionalmente, cada vez que se requiera usar las funciones para resolver esta PEC, se chequea el estado del atributo _ready_ a manera de validación.
```python
ac.preparar_datasets()
```

#### Ejercicio 1) 
Para contar cuántas veces aparece un término dentro del dataset ejecutamos de la siguiente instrucción:
```python
ac.contar_termino_palabra('Huffington Post')
ac.contar_termino_palabra('Un término inexistente')
```
Mientras que para saber la ocurrencia de una determinada URL:
```python
ac.contar_termino_url(
    'https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/73jqd6u5mv/econTabReport.pdf')
ac.contar_termino_url(
    'https://servidor/unReporte.pdf')
```
La librería propuesta no tiene problemas al leer archivos de 1Gb, pues, se apalanca en la lectura de archivos
de Pandas, la cuál está muy optimizada.

Para el caso en que se tenga 100 archivos de 1Gb (o tamaño similar), la solución eficiente consiste en usar una solución de carga paralela y al final unificar en un dataset final.

#### Ejercicio 2) 
Se pide filtrar los datasets dada las siguientes reglas:
- Entrevistas con agente entrevistador perteneciente al dataset _pollster_ratings_.
- Entrevistas sin tracking.
- Entrevistas sin un entrevistador vetado.

Para filtrar los datasets  se hace uso de la siguiente instrucción, recordando que, la clase _ApprovalChecker_ debe estar previamente instanciada y los datasets _preparados_.
```python
ac.filtrar_datasets()
```
#### Ejercicio 3) 
Se pide graficar la aprobación/desaprobación de los términos _Coronavirus, Trump_ agrupados por partido político.
Esto lo hacemos son la siguiente instrucción que genera el archivo ```ejercicio3.png```.
```python
ac.graficar_aprobacion_covid_trump()
```

#### Ejercicio 4) 
Se pide imprimir la cantidad de personas participante en las encuestas según las reglas de filtrado aplicadas en el **Ejercicio 2**, para lo cual hacemos uso de la siguiente instrucción.
```python
ac.participacion_gente()
```
Además se pide aplicar una transformación del campo _grade_ de un valor alfabético a uno numérico, **pero**, esto no ha sido posible pues el campo que se hace en mención ```grade``` no está disponible, lo más parecido es el campo ```538 Grade``` además de que no todos los valores alfabéticos tienen su equivalencia numérica, ejemplo :```A+,A/B, C/D```

#### Ejercicio 5) 
**No implementado**

## Licencia
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Distribuido bajo licencia MIT.


### Todos
 - Implementar más tests unitarios.
 - Implementar los ejercicios 4.2, 4.3, 4.4, y 5.