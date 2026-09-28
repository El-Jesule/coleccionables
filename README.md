# Catálogo de Piezas Coleccionables

> **Nota:** Todo lo descrito en esta primera parte corresponde a la implementación del **Nivel 1** del proyecto, que ahora se encuentra en el archivo `level_1.py`. La versión refactorizada en módulos se explica en la sección [Nivel 2](#nivel-2) al final del documento.

## Objetivo

El objetivo de este programa es gestionar mediante consola un catálogo básico de piezas coleccionables.

El programa permite registrar piezas, consultar su información, aplicar filtros, realizar operaciones sobre sus datos y calcular diferentes métricas del catálogo.

## Contexto

El catálogo está compuesto por piezas coleccionables. Cada pieza contiene:

- Identificador único.
- Nombre.
- Categoría.
- Precio.
- Estado.
- Descripción.

Los estados permitidos para una pieza son:

- `disponible`
- `reservada`
- `vendida`

Además, la descripción de cada pieza debe contener las palabras `usada` o `certificada`.

## Funcionalidades implementadas

### Registro de piezas

- Registro de 10 piezas mediante la terminal.
- Validación de identificadores únicos.
- Validación de nombres no vacíos.
- Validación de precios numéricos y superiores a cero.
- Validación de estados permitidos.
- Validación de descripciones.

### Gestión y consulta del catálogo

- Almacenamiento de las piezas en una colección `catalog`.
- Consulta de la información individual de cada pieza.
- Visualización de todas las piezas.
- Creación de un conjunto con las categorías únicas.
- Cálculo del número de categorías diferentes.

### Filtros

- Filtrado de piezas por estado.
- Filtrado de piezas por precio mínimo.
- Mensaje cuando no existen resultados.

### Operadores lógicos

- Comprobación de si una pieza puede publicarse.
- Comprobación de si una pieza requiere revisión.
- Consulta de piezas que todavía no han sido vendidas.

### Manipulación de strings

- Concatenación de información.
- Interpolación de strings.
- Conversión de etiquetas separadas por comas.
- Reemplazo de `usada` por `certificada`.
- Transformación de nombres de usuario a diferentes formatos.
- Normalización del nombre de una pieza.

### Menú interactivo

El programa incluye un menú que permite:

1. Mostrar todas las piezas.
2. Mostrar las piezas disponibles.
3. Mostrar el precio promedio.
4. Salir del programa.

El menú permanece activo hasta seleccionar la opción de salida y controla las opciones no válidas.

### Métricas

El programa calcula y muestra:

- Número de piezas disponibles.
- Número de piezas reservadas.
- Número de piezas vendidas.
- Número total de piezas.
- Suma total de los precios.
- Precio promedio del catálogo.
- Piezas enumeradas según su posición en el catálogo.

## Ejemplo de interacción

```text
Bienvenido al catálogo de piezas coleccionables.

Introduzca un id único: 001
Introduzca el nombre del producto: Figura Dragon
Introduzca la categoría del producto: Anime
Introduzca el precio del producto: 25,50
Introduzca uno de los tres estados posibles (disponible, reservada o vendida): disponible
Introduzca la descripción del producto. Recuerde que debe incluir 'usada' o 'certificada': Figura usada en buen estado de conservación.

...

=== MENÚ DEL CATÁLOGO ===
1. Mostrar todas las piezas
2. Mostrar solo las piezas disponibles
3. Mostrar el precio promedio
4. Salir

Seleccione una opción: 3

Precio promedio del catálogo: 42.75€

Seleccione una opción: 4

Gracias por utilizar el catálogo. ¡Hasta luego!
```

---

## Nivel 2

El **Nivel 2** es una refactorización del programa anterior. En lugar de concentrar toda la lógica en un único archivo, el código se organiza en **módulos**, separando responsabilidades. La implementación original del Nivel 1 se conserva en `level_1.py`.

### Estructura

```text
catalogo_coleccionables/
├── catalog.py        -> Funciones relacionadas con el catálogo
├── validations.py    -> Funciones de validación de datos de una pieza
├── main.py           -> Programa principal, menú y flujo de ejecución
└── level_1.py        -> Implementación original (Nivel 1) en un solo archivo
```

- `catalog.py` importa `validations.py` y reutiliza sus validaciones.
- `main.py` importa `catalog.py` y usa sus funciones.
- La lógica de validación **no se duplica** entre archivos.

### `validations.py`

Contiene las validaciones de los datos de una pieza, cada una enfocada en una sola responsabilidad. **No imprimen mensajes**: lanzan una excepción `ValueError` con un mensaje claro, y es quien las llama quien decide cómo mostrar el error.

- `validate_not_empty(value, field_name)`: valida que un valor no esté vacío, indicando el nombre del campo.
- `validate_price(price)`: valida que el precio sea numérico y mayor que cero.
- `validate_status(status)`: valida que el estado esté entre los permitidos.
- `validate_description(description)`: valida que la descripción contenga `usada` o `certificada`.

### `catalog.py`

Contiene las funciones que operan sobre el catálogo (una lista de piezas). Importa `validations.py` para no repetir las reglas de validación.

- `add_piece(...)`: valida los datos y construye/retorna el diccionario de una pieza.
- `list_pieces(catalog)`: retorna los nombres de todas las piezas.
- `find_piece_by_id(catalog, id)`: retorna la pieza con ese id o `None`.
- `piece_exists(catalog, id)`: retorna `True` si la pieza existe o `False` si no.
- `remove_piece(catalog, id)`: elimina una pieza; retorna `True` si lo logra o `False` si no existe.
- `get_catalog_summary(catalog)`: retorna un diccionario con la cantidad de piezas por categoría.
- `get_pieces_by_category(catalog, category)`: retorna los nombres de las piezas de una categoría.
- `filter_by_status(catalog, status)`: retorna las piezas con ese estado.
- `filter_by_min_price(catalog, min_price)`: retorna las piezas con precio superior al valor indicado.
- `get_average_price(catalog)`: retorna el precio promedio; `0` si el catálogo está vacío.

### `main.py`

Es el punto de entrada del programa. Importa `catalog.py`, mantiene el catálogo en una lista y muestra un **menú interactivo** que permanece activo hasta que el usuario elige salir. Cada opción **delega en una función de `catalog.py`** y captura los errores (`ValueError`) para mostrar mensajes claros, evitando tener la lógica dentro del bucle del menú.

Opciones del menú:

1. Agregar una pieza.
2. Mostrar todas las piezas.
3. Mostrar las piezas disponibles.
4. Mostrar el precio promedio.
5. Buscar una pieza por identificador.
6. Eliminar una pieza.
7. Salir.

Al agregar una pieza se comprueba que el `id` no esté repetido usando `piece_exists`, y los datos se validan con `add_piece`.

El programa se ejecuta con:

```text
python main.py
```
