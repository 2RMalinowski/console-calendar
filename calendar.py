import sys

import converts_and_valids
import storage
import modify
import ui
meetings = storage.convert_to_tuples_of_ints()


def choose_options_menu():
    user_choice = input('Your choice: ')
    if user_choice == 's':
        modify.add_new_meeting_to(meetings)
    elif user_choice == 'c':
        modify.cancel_meeting_in(meetings)
        # storage.export_data_to(meetings, 'meetings.txt')
    elif user_choice == 'e':
        modify.edit_meeting_in(meetings)
        # storage.export_data_to(meetings, 'meetings.txt')
    elif user_choice == 't':
        converts_and_valids.count_total_meetings_duration_in(meetings)
    elif user_choice == 'm':
        converts_and_valids.compact(meetings)
    elif user_choice == 'q':
        sys.exit()
    else:
        ui.display_message(ui.ORANGE, "There isn't such option")


def display_menu():
    menu_commands = ['schedule a new meeting',
                     'cancel an existing meeting',
                     'edit meeting',
                     'total meeting duration',
                     'meetings compact',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        ui.display_schedule(meetings)
        display_menu()
        choose_options_menu()


if __name__ == '__main__':
    main()
