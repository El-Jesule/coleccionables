# Catálogo de Piezas Coleccionables

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
