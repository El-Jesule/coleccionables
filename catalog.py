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
