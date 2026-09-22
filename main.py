print("Bienvenido al catálogo de piezas coleccionables.")

catalog = []
for i in range(10):
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

target_states:tuple = ("disponible", "reservado", "vendido")
for current_state in target_states:
    print(f"\n=== PIEZAS EN ESTADO: {current_state.upper()} ===")
    if not any(item["state"] == current_state for item in catalog):
        print("No se han encontrado resultados para este filtro.")
    for item in catalog:
        if item["state"] == current_state:
            print(f"Nombre: {item['name']}\nID: {item['item_id']}\nCategoría: {item['category']}\nPrecio: {item['price']:.2f}\nEstado: {item['state']}\nDescripción: {item['description']}\n {'='*10}")

while True:
    try:
        min_price = float(input("Introduzca el precio mínimo por el que desea filtrar: ").replace(',','.'))
        if min_price <= 0:
            raise ValueError
        break
    except:
        print("Debe introducir un valor numérico y superior a 0.")

if not any(item["price"] > min_price for item in catalog):
    print("No se han encontrado resultados para este filtro.")

for item in catalog:
    if item["price"] > min_price:
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