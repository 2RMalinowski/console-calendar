"""
You should not use any global variables. If you need to store state (for
example, a list of meetings), you will need to pass it to the functions that
need it.
"""

import ui
import storage
import modify


def handle_menu():
    menu_commands = ['schedule a new meeting',
                     'cancel an existing meeting',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        handle_menu()
        try:
            choose_options_menu()
        except ValueError as error:
            ui.display_error_message(error)


if __name__ == '__main__':
    main()
