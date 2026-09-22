catalog = []
for i in range(1):
    while True:
        new_id:str = input("Introduzca un id único: ")
        if not any(item["item_id"] == new_id for item in catalog):
            break
        print("El id introducido no es único, por favor, introduzca uno nuevo.")

    while True:
        name:str = input("Introduzca el nombre del producto: ").strip()
        if name.strip():
            break
        print("El nombre no puede estar vacío.")

    while True:
        category:str = input("Introduzca la categoría del producto: ").strip()
        if category.strip():
            category = category.title()
            break
        print("La categoría no puede estar vacía.")

    while True:
        try:
            price = float(input("Introduzca el precio del producto: ").replace(',','.'))
            if price <= 0:
                raise ValueError
            break
        except:
            print("Debe introducir un valor numérico y superior a 0.")
    while True:
        state:str = input("Introduzca uno de los tres estados posibles (Disponible, Reservado o Vendido): ").lower().strip()
        if state in ("disponible", "reservado", "vendido"):
            state = state.title()
            break
        print("Debe indicar un estado válido")

    options = ("certificado", "certificada", "usado", "usada")
    while True:
        description:str = input("Introduzca la descripción del producto. Recuerde que debe indicar si está usado/a y/o certificado/a: ").lower()
        if any(option in description for option in options) and len(description) >= 50:
            break
        print("La descripción debe tener más de cincuenta(50) caracteres e indicar si el producto está certificado/a y/o usado/a.")

    item:dict = {
        "item_id": new_id,
        "name": name,
        "category": category,
        "price": price,
        "state": state,
        "description": description
    }
    catalog.append(item)

categories = {item["category"] for item in catalog}
for item in catalog:
    print(f"Nombre: {item['name']}\nID: {item['item_id']}\nCategoría: {item['category']}\nPrecio: {item['price']:.2f}\nEstado: {item['state']}\nDescripción: {item['description']}\n{'='*10}")
print(f"=== INFORMACIÓN GENERAL DEL CATÁLOGO ===")
print(f"Número total de piezas: {len(catalog)}")
print(f"Listado de las categorías únicas: {', '.join(categories)}")
print(f"Cantidad de categorías diferentes: {len(categories)}")

# * ===== NIVEL 2 ===== *

target_states:tuple = ("Disponible", "Reservado", "Vendido")
for current_state in target_states:
    print(f"\n=== PIEZAS EN ESTADO: {current_state.upper()} ===")
    if not any(item["state"] == current_state for item in catalog):
        print("No se han encontrado resultados para este filtro.")
    for item in catalog:
        if item["state"] == current_state:
            print(f"Nombre: {item['name']}\nID: {item['item_id']}\nCategoría: {item['category']}\nPrecio: {item['price']:.2f}\nEstado: {item['state']}\nDescripción: {item['description']}\n {'='*10}")


print("\n=== REGLA DE PUBLICACIÓN ===")
for item in catalog:
    can_publish = item["price"] > 0 and item["state"].lower() == "disponible"
    print(f"{item['name']}: {'Puede publicarse' if can_publish else 'No puede publicarse'}")

print("\n=== REGLA DE REVISIÓN ===")
for item in catalog:
    needs_review = item["state"].lower() == "reservado" or item["state"].lower() == "vendido"
    print(f"{item['name']}: {'Requiere revisión' if needs_review else 'No requiere revisión'}")

print("\n=== PIEZAS NO VENDIDAS ===")
for item in catalog:
    if item["state"].lower() != "vendido":
        print(f"{item['name']} - ID: {item['item_id']}")

item = catalog[0]

print("\n=== CONCATENACIÓN ===")
print(
    "Nombre: " + item["name"] +
    "\nID: " + item["item_id"] +
    "\nCategoría: " + item["category"] +
    "\nEstado: " + item["state"]
)

print("\n=== INTERPOLACIÓN ===")
print(
    f"Nombre: {item['name']}\n"
    f"ID: {item['item_id']}\n"
    f"Categoría: {item['category']}\n"
    f"Precio: {item['price']:.2f}€\n"
    f"Estado: {item['state']}"
)

tags_input = input("\nIntroduzca etiquetas separadas por comas: ")
tags = tags_input.split(",")

print("Etiquetas:")
for tag in tags:
    print(tag.strip())

replaced_description = item["description"].replace("usada", "certificada")
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
                f"ID: {item['item_id']}\n"
                f"Categoría: {item['category']}\n"
                f"Precio: {item['price']:.2f}€\n"
                f"Estado: {item['state']}\n"
                f"Descripción: {item['description']}\n"
                f"{'=' * 10}"
            )

    elif option == "2":
        print("\n=== PIEZAS DISPONIBLES ===")
        found = False

        for item in catalog:
            if item["state"].lower() == "disponible":
                found = True
                print(
                    f"Nombre: {item['name']}\n"
                    f"ID: {item['item_id']}\n"
                    f"Categoría: {item['category']}\n"
                    f"Precio: {item['price']:.2f}€\n"
                    f"Estado: {item['state']}\n"
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