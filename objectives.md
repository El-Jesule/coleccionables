# Objetivo general

Construir un programa en Python que funcione por consola y permita gestionar un catálogo básico de piezas coleccionables.

El programa debe permitir registrar piezas, consultar la información del catálogo, aplicar filtros, calcular métricas y validar los datos ingresados por el usuario.

# Reglas de negocio
## Estructura de datos de una pieza
Cada pieza debe contener los siguientes datos:

| Campo | Tipo de dato esperado | Descripción |
|---|---|---|
| `id` | Texto | Identificador único de la pieza |
| `name` | Texto | Nombre de la pieza |
| `category` | Texto | Categoría a la que pertenece |
| `price` | Número decimal | Precio de venta o valor de referencia |
| `status` | Texto | Estado actual de la pieza |
| `description` | Texto | Descripción detallada de la pieza |

Las piezas deben almacenarse dentro de una colección principal llamada `catalog`.
La información de cada pieza debe organizarse utilizando una estructura de datos que permita asociar cada campo con su valor correspondiente.

## Estados permitidos
Cada pieza solo puede tener uno de los siguientes estados:
- `disponible` --->  la pieza puede venderse o intercambiarse.
- `reservada` ---> la pieza está apartada temporalmente para un comprador.
- `vendida` ---> la pieza ya fue vendida y no está disponible.

## La descripción
La descripción de una pieza debe explicar brevemente las características de la pieza.
Además, debe incluir obligatoriamente una de las siguientes palabras:
- `usada`
- `certificada`

### Ejemplos de descripciones válidas
- Figura usada con algunos detalles de conservación.
- Pieza certificada en caja original.
- Carta usada en buen estado.
- Moneda certificada por un experto.
### Ejemplo de descripción no válida
- Figura roja de colección.
La descripción anterior no contiene las palabras `usada` ni `certificada`.

---
# NIVEL I – Registro de piezas y estructuras base

## Parte 1. Preparación del proyecto

1. Crear un repositorio en GitHub para el reto.
2. Clonar el repositorio en el equipo local.
3. Crear el archivo principal del programa.
4. Crear el archivo `README.md`.
5. Definir el nombre del sistema.
6. Mostrar un mensaje de bienvenida al iniciar el programa.

El mensaje debe indicar que el usuario está ingresando al catálogo de piezas coleccionables.

## Parte 2. Captura de piezas por terminal

El programa debe solicitar por terminal la información de **10 piezas coleccionables**.
Cada pieza debe solicitar los siguientes datos:
* Identificador.
* Nombre.
* Categoría.
* Precio.
* Estado.
* Descripción.

## Parte 3. Almacenamiento de la información

Al finalizar la captura:

- el catálogo deberá contener como mínimo 10 piezas.
- Cada pieza debe conservar todos sus datos.
- El catálogo debe permitir recorrer y consultar las piezas individualmente.
- Los datos deben estar organizados de forma que sea posible acceder al identificador, nombre, categoría, precio, estado y descripción de cada pieza.

## Parte 4. Información adicional del catálogo

Crear también un set con las categorías utilizadas en las piezas registradas.

El set debe:
- Contener únicamente categorías.
- Eliminar automáticamente las categorías repetidas.
- Permitir conocer cuántas categorías diferentes existen.

## Parte 5. Mostrar el catálogo

Recorrer el catálogo y mostrar la información de todas las piezas.
De cada pieza se debe mostrar:
- Identificador.
- Nombre.
- Categoría.
- Precio.
- Estado.
- Descripción.

También se debe mostrar:
- La cantidad total de piezas.
- Las categorías únicas.
- La información general del catálogo.
- La cantidad de categorías diferentes.

---
# NIVEL II – Filtros, operadores y strings

## Parte 6. Filtrar piezas por estado

* Mostrar únicamente las piezas que se encuentren en estado `disponible`.
* Después, mostrar únicamente las piezas que se encuentren en estado `reservada`.
* Finalmente, mostrar únicamente las piezas que se encuentren en estado `vendida`.

Cada filtro debe mostrar la información suficiente para identificar las piezas encontradas.

Si no existen piezas con el estado consultado, se debe mostrar un mensaje indicando que no hay resultados.

## Parte 7. Filtrar piezas por precio

Solicitar al usuario un precio mínimo.
Mostrar las piezas cuyo precio sea superior al valor ingresado.

El programa debe:
- Solicitar el precio por terminal.
- Validar que sea un valor numérico.
- Comparar el precio con el de cada pieza.
- Mostrar las piezas que cumplen la condición.
- Informar si no se encontraron piezas.

## Parte 8. Aplicar operadores lógicos

Aplicar las siguientes reglas al catálogo.
### Regla de publicación
Una pieza puede publicarse únicamente cuando:
- Tiene un precio mayor que cero.
- Su estado es `disponible`.
Mostrar para cada pieza si puede publicarse o no.
### Regla de revisión
Una pieza requiere revisión cuando:
- Está `reservada`, o
- Está `vendida`.
Mostrar para cada pieza si requiere revisión o no.

### Regla de piezas no vendidas
Mostrar las piezas que no tienen el estado `vendida`.

## Parte 9. Manipulación de strings

Realizar las siguientes operaciones:

1. Mostrar la información de una pieza utilizando concatenación.
2. Mostrar la información de una pieza utilizando interpolación.
3. Solicitar al usuario una cadena de etiquetas separadas por comas.
4. Convertir esa cadena de etiquetas en elementos separados.
5. Reemplazar la palabra `usada` por `certificada` en una descripción.
6. Solicitar un nombre de usuario por terminal.
7. Mostrar el nombre:
   - Sin espacios al inicio o al final.
   - En minúsculas.
   - En mayúsculas.
   - En formato título.
8. Normalizar el nombre de una pieza antes de mostrarlo.

Ejemplo de etiquetas que puede introducir el usuario:

```text
retro,anime,limited
```

___

# NIVEL III – Bucles, menú y métricas (Opcional)

## Parte 10. Crear un menú interactivo

* El programa debe mostrar un menú que permita consultar el catálogo.
* El menú debe repetirse hasta que el usuario seleccione la opción de salida.

El menú debe incluir como mínimo las siguientes opciones:
1. Mostrar todas las piezas.
2. Mostrar solo las piezas disponibles.
3. Mostrar el precio promedio.
4. Salir.

### Comportamiento esperado

#### Opción 1: Mostrar todas las piezas
Debe mostrar toda la información de las piezas registradas en el catálogo.
#### Opción 2: Mostrar piezas disponibles
Debe mostrar únicamente las piezas que tengan el estado `disponible`.
#### Opción 3: Mostrar precio promedio
Debe calcular y mostrar el precio promedio de todas las piezas.
#### Opción 4: Salir
Debe mostrar un mensaje de despedida y finalizar el programa.
#### Opción no válida
Si el usuario introduce una opción que no existe:
- Mostrar un mensaje de error.
- No finalizar el programa.
- Volver a mostrar el menú.

El menú debe permanecer activo hasta que el usuario seleccione la opción de salida.

## Parte 11. Calcular métricas del catálogo

Calcular y mostrar:

1. Cantidad de piezas disponibles.
2. Cantidad de piezas reservadas.
3. Cantidad de piezas vendidas.
4. Cantidad total de piezas.
5. Suma total de los precios.
6. Precio promedio del catálogo.

Además, mostrar las piezas enumeradas, indicando una posición consecutiva para cada una.

Ejemplo del resultado esperado:

```text
1. Figura Dragon Red
2. Blue Trading Card
3. Ancient Coin
```

## Parte 12. Validaciones básicas

El programa debe validar:
1. Que el precio sea numérico.
2. Que el precio sea mayor que cero.
3. Que el nombre no esté vacío.
4. Que el estado pertenezca a los estados permitidos.
5. Que la descripción contenga `usada` o `certificada`.
6. Que el usuario seleccione una opción válida en el menú.

Cuando un dato sea inválido:
- Mostrar un mensaje claro.
- No continuar con ese dato incorrecto.
- Solicitar nuevamente la información cuando corresponda.
