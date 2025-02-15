from ret_car_app.rent_car_bl import get_available_cars, get_rented_cars, rent_car
from text_gui import *


def get_menu() -> tuple:
    return (
        "Lista wypożyczonych samochodów",
        "Lista dostępnych samochodów",
        "Wypożycz samochód",
        "Wyjście"
    )


def get_exit_code() -> int:
    return len(get_menu())


bl_actions = (
    {"action": get_rented_cars, "view": show_lws},
    {"action": get_available_cars, "view": show_lds},
    {"action": rent_car, "view": show_rent_car},
)


def main() -> None:
    show_menu(get_menu())

    while (user_action := get_user_action()) != get_exit_code():
        try:
            action_data: dict = bl_actions[user_action - 1]
            function = action_data["action"]
            action_data["view"](function)
        except IndexError:
            show_menu(get_menu())


if __name__ == '__main__':
    main()
