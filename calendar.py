"""
You should not use any global variables. If you need to store state (for
example, a list of meetings), you will need to pass it to the functions that
need it.
"""

import sys

import converts_and_valids
import storage
import modify
import ui
from storage import meetings


def choose_options_menu():
    user_choice = input('Your choice: ')
    if user_choice == 's':
        modify.add_new_meeting_to(meetings)
        # save
    elif user_choice == 'c':
        modify.cancel_meeting_in(meetings)
        # save
    elif user_choice == 'q':
        sys.exit()
    else:
        print('No such option')  # or raise KeyError("There isn't such option")


def display_menu():
    menu_commands = ['schedule a new meeting',
                     'cancel an existing meeting',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        converts_and_valids.convert_duration_to_meeting_hours(meetings)
        display_menu()
        choose_options_menu()


if __name__ == '__main__':
    main()
