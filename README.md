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

#### Ejemplo Ocurrencias de palabra/url
Las siguientes
```python
ac.preparar_datasets()
```

## Licencia
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Distribuido bajo licencia MIT.


### Todos
 - Mejorar los tests unitarios