# getting input form user functions
def get_input(message):
    user_input = input(message)
    return user_input


def title(message):
    while True:
        try:
            meeting_title = str(get_input(message))
            if len(meeting_title) > 43:
                raise ValueError
        except ValueError:
            error_message = "Message title is longer than 42 chars"
            display_error_message(error_message)
        else:
            return meeting_title.title()
            break


def duration(message):
    while True:
        try:
            duration = int(get_input(message))
            if duration not in range(1, 3):
                raise ValueError
        except (KeyError, ValueError):
            error_message = 'Please enter proper value'
            display_error_message(error_message)
        else:
            return str(duration)
            break


#  displaying functions
def display_schedule(meeting_list):
    print('Your schedule for the day:')
    for element in meeting_list:
        print(' '.join(element))
    if not meeting_list:
        print('(empty)')


def display_program_menu(menu_commands):
    print('Menu:')
    for option in menu_commands:
        print(f'({option[0]}) {option}')


def display_message(message):
    print(message)


def display_error_message(message):
    print(f'ERROR {message}')
