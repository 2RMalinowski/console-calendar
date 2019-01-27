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
meetings = storage.import_data_from('meetings.txt')


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
        ui.display_message(ui.ORANGE, "There isn't such option")


def display_menu():
    menu_commands = ['schedule a new meeting',
                     'cancel an existing meeting',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        ui.display_schedule(meetings)
        display_menu()
        choose_options_menu()


if __name__ == '__main__':
    main()
