import validations


def add_piece(id, name, category, price, status, description):
    validations.validate_not_empty(id, "id")
    validations.validate_not_empty(name, "name")
    validations.validate_not_empty(category, "category")
    validations.validate_price(price)
    validations.validate_status(status)
    validations.validate_description(description)

    piece = {
        "id": id,
        "name": name,
        "category": category,
        "price": float(price),
        "status": status,
        "description": description,
    }

    return piece


def list_pieces(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    for piece in catalog:
        if piece["id"] == id:
            return piece

    return None
