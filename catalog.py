import validations


def _ensure_catalog_is_list(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista.")

    return True


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
    _ensure_catalog_is_list(catalog)

    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, id):
    _ensure_catalog_is_list(catalog)

    for piece in catalog:
        if piece["id"] == id:
            return piece

    return None


def remove_piece(catalog, id):
    _ensure_catalog_is_list(catalog)

    piece = find_piece_by_id(catalog, id)

    try:
        if piece is None:
            raise ValueError(f"No se encontró una pieza con el id '{id}'.")

        catalog.remove(piece)

    except ValueError:
        return False

    return True


def get_catalog_summary(catalog):
    _ensure_catalog_is_list(catalog)

    summary = {}

    for piece in catalog:
        category = piece["category"]
        summary[category] = summary.get(category, 0) + 1

    return summary
