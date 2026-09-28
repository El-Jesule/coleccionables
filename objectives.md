# Objetivo general

Construir un programa en Python que funcione por consola y permita gestionar un catálogo básico de piezas coleccionables.

El programa debe permitir registrar piezas, consultar la información del catálogo, aplicar filtros, calcular métricas y validar los datos ingresados por el usuario.

# Structure
### Estructura del proyecto
El proyecto debe organizarse en varios archivos (módulos), no todo en uno solo:

```
catalogo_coleccionables/
├── catalog.py        -> Funciones relacionadas con el catálogo (agregar, listar, buscar, quitar, filtrar, métricas)
├── validations.py    -> Funciones de validación de datos de una pieza
├── main.py           -> Programa principal, menú y flujo de ejecución
└── README.md
```

- `catalog.py` debe importarse desde `main.py`.
- `validations.py` debe importarse desde `catalog.py` y/o `main.py`, según corresponda.
- No se debe duplicar lógica de validación en varios archivos.
---
### Recordatorio: estructura de una pieza
Cada pieza sigue siendo un diccionario con esta forma:
```
{
    "id": "...",
    "name": "...",
    "category": "...",
    "price": 0.0,
    "status": "...",
    "description": "..."
}
```
Estados permitidos: `disponible`, `reservada`, `vendida`
La descripción debe contener obligatoriamente la palabra `usada` o `certificada`

---
# Technical requirements

## Parte 1.  Agregar una pieza

Archivo: `catalog.py`

Crea una función llamada `add_piece` que reciba los datos necesarios para construir una pieza (`id`, `name`, `category`, `price`, `status`, `description`) y retorne un diccionario con esa información.

La función debe:
- Validar que ningún campo obligatorio venga vacío antes de construir la pieza.
- Validar que el precio sea numérico y mayor que cero.
- Validar que el estado esté dentro de los estados permitidos.
- Validar que la descripción contenga `usada` o `certificada`.
- Si alguna validación falla, debe lanzarse una excepción adecuada (`ValueError`) con un mensaje claro.
- Si todo es correcto, debe retornar el diccionario de la pieza.

> Sugerencia: las validaciones pueden delegarse a funciones del archivo `validations.py`.

## Parte 2. Listar piezas

Archivo: `catalog.py`

Crea una función llamada `list_pieces` que reciba el catálogo (una lista de piezas) y retorne una lista con los nombres de todas las piezas.

La función debe:
- Validar que el argumento recibido sea una lista.
- Si el catálogo está vacío, retornar una lista vacía.
- Si el argumento no es una lista, manejar el error adecuadamente.

## Parte 3. Buscar una pieza por identificador

Archivo: `catalog.py`

Crea una función llamada `find_piece_by_id` que reciba el catálogo y un `id`, y retorne el diccionario de la pieza cuyo identificador coincida.

La función debe:
- Validar que el catálogo sea una lista.
- Retornar `None` si no se encuentra ninguna pieza con ese identificador.
- No debe lanzar una excepción si simplemente no se encuentra la pieza (eso no es un error, es un resultado válido).

## Parte 4. Quitar una pieza del catálogo

Archivo: `catalog.py`

Crea una función llamada `remove_piece` que reciba el catálogo y un `id`, e intente eliminar la pieza correspondiente.

La función debe:
- Validar que el catálogo sea una lista.
- Si la pieza no existe, debe lanzarse una excepción indicando que no fue encontrada.
- Manejar la excepción adecuadamente y retornar `False` en caso de error.
- Retornar `True` si la pieza fue eliminada con éxito.

## Parte 5. Resumen del catálogo (diccionario)

Archivo: `catalog.py`

Crea una función llamada `get_catalog_summary` que reciba el catálogo y retorne un diccionario con la cantidad de piezas por categoría.

La función debe:
- Validar que el catálogo sea una lista.
- Recorrer las piezas y contar cuántas hay por cada categoría.
- Retornar el diccionario resultante.

## Parte 6. Piezas por categoría (lista)

Archivo: `catalog.py`

Crea una función llamada `get_pieces_by_category` que reciba el catálogo y una categoría, y retorne una lista con los nombres de las piezas que pertenecen a esa categoría.

La función debe:
- Validar que el catálogo sea una lista.
- Retornar una lista vacía si no hay coincidencias.

## Parte 7. Verificar existencia de una pieza (booleano)

Archivo: `catalog.py`

Crea una función llamada `piece_exists` que reciba el catálogo y un `id`, y retorne `True` si la pieza existe, o `False` en caso contrario.

La función debe:
- Validar que el catálogo sea una lista.
- No debe lanzar una excepción cuando la pieza no existe.

## Parte 8. Filtrar por estado

Archivo: `catalog.py`

Crea una función llamada `filter_by_status` que reciba el catálogo y un estado, y retorne una lista con las piezas que tengan ese estado.

La función debe:
- Validar que el estado recibido sea uno de los estados permitidos.
- Si el estado no es válido, lanzar una excepción con un mensaje claro.
- Retornar una lista vacía si no hay piezas con ese estado.

## Parte 9. Filtrar por precio mínimo

Archivo: `catalog.py`

Crea una función llamada `filter_by_min_price` que reciba el catálogo y un precio mínimo, y retorne las piezas cuyo precio sea mayor al valor indicado.

La función debe:
- Validar que el precio mínimo sea numérico.
- Lanzar una excepción si el valor no es numérico.
- Retornar una lista vacía si ninguna pieza cumple la condición.

## Parte 10. Calcular el precio promedio

Archivo: `catalog.py`

Crea una función llamada `get_average_price` que reciba el catálogo y retorne el precio promedio de todas las piezas.

La función debe:
- Validar que el catálogo no esté vacío antes de calcular el promedio.
- Si el catálogo está vacío, manejar el error adecuadamente y retornar `0`.

## Parte 11. Validaciones de una pieza

Archivo: `validations.py`

Crea funciones de validación independientes, cada una enfocada en una sola responsabilidad:
- `validate_price(price)`: valida que el precio sea numérico y mayor que cero.
- `validate_status(status)`: valida que el estado esté entre los permitidos.
- `validate_description(description)`: valida que la descripción contenga `usada` o `certificada`.
- `validate_not_empty(value, field_name)`: valida que un valor no esté vacío, indicando el nombre del campo en el mensaje de error.

Cada función debe:
- Lanzar una excepción (`ValueError`) con un mensaje claro cuando la validación falla.
- No imprimir mensajes por sí misma: la responsabilidad de mostrar o manejar el error es de quien llama a la función.

> Estas funciones deben ser utilizadas desde `catalog.py`, evitando repetir la misma lógica de validación en varios lugares.

## Parte 12. Menú principal usando funciones

Archivo: `main.py`

Refactoriza el menú interactivo del taller anterior para que cada opción del menú llame a una función específica de `catalog.py`, en lugar de tener la lógica directamente escrita dentro del bucle del menú.

El menú debe seguir contemplando como mínimo:
1. Agregar una pieza.
2. Mostrar todas las piezas.
3. Mostrar piezas disponibles.
4. Mostrar el precio promedio.
5. Buscar una pieza por identificador.
6. Eliminar una pieza.
7. Salir.

El `main.py` debe:
- Importar las funciones necesarias desde `catalog.py`.
- Capturar los errores lanzados por las funciones y mostrar mensajes claros al usuario.
- Mantener el programa en ejecución hasta que el usuario elija salir.