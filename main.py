import catalog


def show_piece(piece):
    print(
        f"Nombre: {piece['name']}\n"
        f"ID: {piece['id']}\n"
        f"Categoría: {piece['category']}\n"
        f"Precio: {piece['price']:.2f}€\n"
        f"Estado: {piece['status']}\n"
        f"Descripción: {piece['description']}\n"
        f"{'=' * 10}"
    )


def register_piece():
    while True:
        try:
            piece = catalog.add_piece(
                id=input("Introduzca un id: ").strip(),
                name=input("Introduzca el nombre: ").strip(),
                category=input("Introduzca la categoría: ").strip(),
                price=input("Introduzca el precio: ").replace(",", ".").strip(),
                status=input(
                    "Introduzca el estado "
                    "(disponible, reservada o vendida): "
                ).strip().lower(),
                description=input(
                    "Introduzca la descripción "
                    "(debe incluir 'usada' o 'certificada'): "
                ).strip(),
            )

            return piece

        except ValueError as error:
            print(f"Error: {error}")
            print("Vuelva a introducir los datos de la pieza.\n")


def main():
    pieces = []

    while True:
        print("\n=== MENÚ DEL CATÁLOGO ===")
        print("1. Agregar una pieza")
        print("2. Mostrar todas las piezas")
        print("3. Mostrar piezas disponibles")
        print("4. Mostrar el precio promedio")
        print("5. Buscar una pieza por identificador")
        print("6. Eliminar una pieza")
        print("7. Salir")

        option = input("Seleccione una opción: ").strip()

        try:
            if option == "1":
                piece = register_piece()
                pieces.append(piece)
                print("\nPieza agregada correctamente.")
                show_piece(piece)

            elif option == "2":
                if not catalog.list_pieces(pieces):
                    print("El catálogo está vacío.")
                else:
                    print("\n=== TODAS LAS PIEZAS ===")

                    for position, piece in enumerate(pieces, start=1):
                        print(f"{position}.")
                        show_piece(piece)

            elif option == "3":
                available = catalog.filter_by_status(pieces, "disponible")

                if not available:
                    print("No se han encontrado piezas disponibles.")
                else:
                    print("\n=== PIEZAS DISPONIBLES ===")

                    for piece in available:
                        show_piece(piece)

            elif option == "4":
                average = catalog.get_average_price(pieces)
                print(f"\nPrecio promedio del catálogo: {average:.2f}€")

            elif option == "5":
                id = input("Introduzca el id a buscar: ").strip()
                piece = catalog.find_piece_by_id(pieces, id)

                if piece is None:
                    print(f"No se encontró ninguna pieza con el id '{id}'.")
                else:
                    show_piece(piece)

            elif option == "6":
                id = input("Introduzca el id a eliminar: ").strip()

                if catalog.remove_piece(pieces, id):
                    print(f"La pieza con id '{id}' fue eliminada.")
                else:
                    print(f"No se encontró ninguna pieza con el id '{id}'.")

            elif option == "7":
                print("\nGracias por utilizar el catálogo. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Introduzca una opción del 1 al 7.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
