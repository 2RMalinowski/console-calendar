"""
You should not use any global variables. If you need to store state (for
example, a list of meetings), you will need to pass it to the functions that
need it.
"""

from modify import meeting_list
import modify
import storage
import sys
import ui


def choose_options_menu():
    user_choice = input('Your choice: ')
    if user_choice == 's':
        modify.add_new_meeting_to(meeting_list)
    elif user_choice == 'c':
        modify.cancel_meeting_in(meeting_list)
    elif user_choice == 'q':
        sys.exit()
    else:
        print('No such option')  # or raise KeyError("There isn't such option")


def handle_menu():
    menu_commands = ['schedule a new meeting',
                     'cancel an existing meeting',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        ui.display_schedule(meeting_list)
        handle_menu()
        try:
            choose_options_menu()
        except ValueError as error:
            ui.display_error_message(error)


if __name__ == '__main__':
    main()
