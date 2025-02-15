ERROR_MESSAGE = "\n\nA Ty co???? Nie widzisz dostępnych opcji???\n\n"


def show_lws(lws_function: callable) -> None:
    if not (lws := lws_function()):
        print("All car are available!")
        return

    for rent in lws:
        print(rent)


def show_lds(lds_function: callable) -> None:
    if not (lds := lds_function()):
        print("All car are rented!")
        return

    for rent in lds:
        print(rent)


def show_rent_car(rent_car_function: callable):
    first_name = input("Imię: ")
    last_name = input("Nazwisko: ")
    licence_number = input("Numer prawa jazdy: ")

    if not (car_rented := rent_car_function(first_name, last_name, licence_number)):
        print("Nie ma dostępnych samochodów!")
        return

    print(f"Wypożyczono: {car_rented}")


def show_menu(menu_item: tuple) -> None:
    for action, element in enumerate(menu_item):
        print(f"{action + 1}: {element}")


def get_user_action() -> int:
    try:
        return int(input("> "))
    except ValueError:
        print(ERROR_MESSAGE)
        return get_user_action()
