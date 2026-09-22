print("Bienvenido al catálogo de piezas coleccionables.")

catalog = []

for i in range(10):
    while True:
        id = input("Introduzca un id único: ").strip()

        if not id:
            print("El id no puede estar vacío, por favor, introduzca uno nuevo.")
            continue

        if any(item["id"] == id for item in catalog):
            print("El id introducido no es único, por favor, introduzca uno nuevo.")
            continue

        break

    while True:
        name = input("Introduzca el nombre del producto: ").strip()

        if name:
            break

        print("El nombre no puede estar vacío.")

    while True:
        category = input("Introduzca la categoría del producto: ").strip()

        if category:
            category = category.title()
            break

        print("La categoría no puede estar vacía.")

    while True:
        try:
            price = float(
                input("Introduzca el precio del producto: ").replace(",", ".")
            )

            if price <= 0:
                raise ValueError

            break

        except ValueError:
            print("Debe introducir un valor numérico y superior a 0.")

    while True:
        status = input(
            "Introduzca uno de los tres estados posibles "
            "(disponible, reservada o vendida): "
        ).lower().strip()

        if status in ("disponible", "reservada", "vendida"):
            break

        print(
            "Debe indicar un estado válido: "
            "disponible, reservada o vendida."
        )

    while True:
        description = input(
            "Introduzca la descripción del producto. "
            "Recuerde que debe incluir 'usada' o 'certificada': "
        ).strip()

        if "usada" in description.lower() or "certificada" in description.lower():
            break

        print(
            "La descripción debe contener la palabra "
            "'usada' o 'certificada'."
        )

    item = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    catalog.append(item)


# ===== PARTE 4 Y 5 =====

categories = {item["category"] for item in catalog}

for item in catalog:
    print(
        f"Nombre: {item['name']}\n"
        f"ID: {item['id']}\n"
        f"Categoría: {item['category']}\n"
        f"Precio: {item['price']:.2f}\n"
        f"Estado: {item['status']}\n"
        f"Descripción: {item['description']}\n"
        f"{'=' * 10}"
    )

print("=== INFORMACIÓN GENERAL DEL CATÁLOGO ===")
print(f"Número total de piezas: {len(catalog)}")
print(f"Listado de las categorías únicas: {', '.join(categories)}")
print(f"Cantidad de categorías diferentes: {len(categories)}")


# ===== NIVEL 2 - PARTE 6 =====

target_statuses = ("disponible", "reservada", "vendida")

for current_status in target_statuses:
    print(f"\n=== PIEZAS EN ESTADO: {current_status.upper()} ===")

    if not any(item["status"] == current_status for item in catalog):
        print("No se han encontrado resultados para este filtro.")

    for item in catalog:
        if item["status"] == current_status:
            print(
                f"Nombre: {item['name']}\n"
                f"ID: {item['id']}\n"
                f"Categoría: {item['category']}\n"
                f"Precio: {item['price']:.2f}\n"
                f"Estado: {item['status']}\n"
                f"Descripción: {item['description']}\n"
                f"{'=' * 10}"
            )


# ===== PARTE 7 =====

while True:
    try:
        min_price = float(
            input("Introduzca el precio mínimo por el que desea filtrar: ")
            .replace(",", ".")
        )

        if min_price <= 0:
            raise ValueError

        break

    except ValueError:
        print("Debe introducir un valor numérico y superior a 0.")


if not any(item["price"] > min_price for item in catalog):
    print("No se han encontrado resultados para este filtro.")

for item in catalog:
    if item["price"] > min_price:
        print(
            f"Nombre: {item['name']}\n"
            f"ID: {item['id']}\n"
            f"Categoría: {item['category']}\n"
            f"Precio: {item['price']:.2f}\n"
            f"Estado: {item['status']}\n"
            f"Descripción: {item['description']}\n"
            f"{'=' * 10}"
        )


# ===== PARTE 8 =====

print("\n=== REGLA DE PUBLICACIÓN ===")

for item in catalog:
    can_publish = (
        item["price"] > 0
        and item["status"] == "disponible"
    )

    print(
        f"{item['name']}: "
        f"{'Puede publicarse' if can_publish else 'No puede publicarse'}"
    )


print("\n=== REGLA DE REVISIÓN ===")

for item in catalog:
    needs_review = (
        item["status"] == "reservada"
        or item["status"] == "vendida"
    )

    print(
        f"{item['name']}: "
        f"{'Requiere revisión' if needs_review else 'No requiere revisión'}"
    )


print("\n=== PIEZAS NO VENDIDAS ===")

for item in catalog:
    if item["status"] != "vendida":
        print(f"{item['name']} - ID: {item['id']}")


# ===== PARTE 9 =====

item = catalog[0]

print("\n=== CONCATENACIÓN ===")

print(
    "Nombre: " + item["name"] +
    "\nID: " + item["id"] +
    "\nCategoría: " + item["category"] +
    "\nEstado: " + item["status"]
)


print("\n=== INTERPOLACIÓN ===")

print(
    f"Nombre: {item['name']}\n"
    f"ID: {item['id']}\n"
    f"Categoría: {item['category']}\n"
    f"Precio: {item['price']:.2f}€\n"
    f"Estado: {item['status']}"
)


tags_input = input("\nIntroduzca etiquetas separadas por comas: ")
tags = tags_input.split(",")

print("Etiquetas:")

for tag in tags:
    print(tag.strip())


replaced_description = item["description"].replace(
    "usada",
    "certificada"
)

print("\n=== DESCRIPCIÓN MODIFICADA ===")
print(replaced_description)


username = input("\nIntroduzca su nombre de usuario: ")

username = username.strip()

print(f"Sin espacios: {username}")
print(f"Minúsculas: {username.lower()}")
print(f"Mayúsculas: {username.upper()}")
print(f"Formato título: {username.title()}")


normalized_name = item["name"].strip().title()

print(f"\nNombre normalizado de la pieza: {normalized_name}")


# ===== NIVEL 3 - PARTE 10 =====

while True:
    print("\n=== MENÚ DEL CATÁLOGO ===")
    print("1. Mostrar todas las piezas")
    print("2. Mostrar solo las piezas disponibles")
    print("3. Mostrar el precio promedio")
    print("4. Salir")

    option = input("Seleccione una opción: ").strip()

    if option == "1":
        print("\n=== TODAS LAS PIEZAS ===")

        for position, item in enumerate(catalog, start=1):
            print(
                f"{position}. {item['name']}\n"
                f"ID: {item['id']}\n"
                f"Categoría: {item['category']}\n"
                f"Precio: {item['price']:.2f}€\n"
                f"Estado: {item['status']}\n"
                f"Descripción: {item['description']}\n"
                f"{'=' * 10}"
            )

    elif option == "2":
        print("\n=== PIEZAS DISPONIBLES ===")

        found = False

        for item in catalog:
            if item["status"] == "disponible":
                found = True

                print(
                    f"Nombre: {item['name']}\n"
                    f"ID: {item['id']}\n"
                    f"Categoría: {item['category']}\n"
                    f"Precio: {item['price']:.2f}€\n"
                    f"Estado: {item['status']}\n"
                    f"Descripción: {item['description']}\n"
                    f"{'=' * 10}"
                )

        if not found:
            print("No se han encontrado piezas disponibles.")

    elif option == "3":
        total_price = sum(item["price"] for item in catalog)
        average_price = total_price / len(catalog)

        print(f"\nPrecio promedio del catálogo: {average_price:.2f}€")

    elif option == "4":
        print("\nGracias por utilizar el catálogo. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Introduzca una opción del 1 al 4.")


# ===== PARTE 11 =====

available = sum(
    1 for item in catalog
    if item["status"] == "disponible"
)

reserved = sum(
    1 for item in catalog
    if item["status"] == "reservada"
)

sold = sum(
    1 for item in catalog
    if item["status"] == "vendida"
)

total_items = len(catalog)

total_price = sum(item["price"] for item in catalog)

average_price = total_price / total_items


print("\n=== MÉTRICAS DEL CATÁLOGO ===")
print(f"Piezas disponibles: {available}")
print(f"Piezas reservadas: {reserved}")
print(f"Piezas vendidas: {sold}")
print(f"Piezas totales: {total_items}")
print(f"Suma total de precios: {total_price:.2f}€")
print(f"Precio promedio: {average_price:.2f}€")


print("\n=== PIEZAS ENUMERADAS ===")

for position, item in enumerate(catalog, start=1):
    print(f"{position}. {item['name']}")