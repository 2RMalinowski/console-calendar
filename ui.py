
# getting input form user functions


def title(message):
    while True:
        meeting_title = input(message)
        if len(meeting_title) > 43:
            error_message = "Message title is longer than 42 chars"
            display_error_message(error_message)
        else:
            return meeting_title.title()


def duration(message):
    while True:
        duration = int(input(message))
        if duration not in range(1, 3):
            error_message = 'Please enter proper value'
            display_error_message(error_message)
        else:
            return duration


def start_time(message):
    while True:
        try:
            time = int(input(message))
            if 0 < time > 17:
                raise ValueError
        except(KeyError, ValueError):
            error_message = 'Please enter hour no later than 17'
            display_error_message(error_message)
        else:
            return time


#  displaying functions
# def display_schedule(meeting_list):
#     print('Your schedule for the day:')
#     for element in meeting_list:
#         print(' '.join(element))
#     if not meeting_list:
#         print('(empty)')


def display_program_menu(menu_commands):
    print('Menu:')
    for option in menu_commands:
        print(f'({option[0]}) {option}')


def display_message(message):
    print(message)


def display_error_message(message):
    print(f'ERROR {message}')
