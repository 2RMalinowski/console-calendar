# getting input form user
def get_input(message):
    user_input = input(message)
    return user_input


#  displaying functions
def display_schedule(meeting_list):
    print('Your schedule for the day :')
    for element in meeting_list:
        print(' '.join(element))


def display_program_menu(menu_commands):
    for option in menu_commands:
        print(f'({option[0]}) {option}')


def display_message(message):
    print(message)


def display_error_message(message):
    print(message)
