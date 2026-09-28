ALLOWED_STATUSES = ("disponible", "reservada", "vendida")

REQUIRED_DESCRIPTION_WORDS = ("usada", "certificada")


def validate_not_empty(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"El campo '{field_name}' no puede estar vacío.")

    return True


def validate_price(price):
    try:
        numeric_price = float(price)
    except (TypeError, ValueError):
        raise ValueError("El precio debe ser un valor numérico.")

    if numeric_price <= 0:
        raise ValueError("El precio debe ser mayor que 0.")

    return True


def validate_status(status):
    if status not in ALLOWED_STATUSES:
        raise ValueError(
            "El estado debe ser uno de los siguientes: "
            "disponible, reservada o vendida."
        )

    return True


def validate_description(description):
    text = str(description).lower()

    if not any(word in text for word in REQUIRED_DESCRIPTION_WORDS):
        raise ValueError(
            "La descripción debe contener la palabra 'usada' o 'certificada'."
        )

    return True
