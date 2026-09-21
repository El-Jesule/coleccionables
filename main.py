print("Bienvenido al catálogo de piezas coleccionables.")

catalog = []
for i in range(10):
    item_id:str = input("Introduzca un id único: ")

    while True:
        name:str = input("Introduzca el nombre del producto: ")
        if name.strip():
            break
        print("El nombre no puede estar vacío.")

    while True:
        category:str = input("Introduzca la categoría del producto: ")
        if category.strip():
            break
        print("La categoría no puede estar vacía.")

    while True:
        try:
            price = float(input("Introduzca el precio del producto: ").replace(',','.'))
            if price <= 0:
                raise ValueError
            else:
                break
        except:
            print("Debe introducir un valor numérico y superior a 0.")
    while True:
        state:str = input("Introduzca uno de los tres estados posibles (Disponible, Reservado o Vendido): ").lower()
        if "disponible" in state or "reservado" in state or "vendido" in state:
            break
        else:
            print("Debe indicar un estado válido")

    options = ("certificado", "certificada", "usado", "usada")
    while True:
        description:str = input("Introduzca la descripción del producto. Recuerde que debe indicar si está usado/a y/o certificado/a: ").lower()
        if any(option in description for option in options) and len(description) >= 50:
            break
        print("La descripción debe tener más de cincuenta(50) caracteres e indicar si el producto está certificado/a y/o usado/a.")

    item:dict = {
        "item_id": item_id,
        "name": name,
        "category": category,
        "price": price,
        "state": state,
        "description": description
    }
    catalog.append(item)