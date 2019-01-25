import converts_and_valids

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
        try:
            duration = int(input(message))
            if duration not in range(1, 3):
                raise ValueError
        except(ValueError):
            error_message = 'Please enter proper value'
            display_error_message(error_message)
        else:
            return duration


def start_time(message):
    while True:
        try:
            time = int(input(message))
            if time not in range(8, 18):
                raise ValueError
        except(ValueError):
            error_message = 'Please enter hour from 8 to 17'
            display_error_message(error_message)
            # if not converts_and_valids.check_meeting_overlpas(time):
            #     error_message = 'Meeting overlaps with existing meeting!'
            #     display_error_message(error_message)
        else:
            return time


def start_time_of_meeting_to_remove(message):
    while True:
        try:
            time = int(input(message))
            if time not in range(8, 18):  # podczepić walidację w converts and valids
                raise ValueError
        except(ValueError):
            error_message = 'Please enter hour'
            display_error_message(error_message)


#  displaying functions
START_TIME = 0
END_TIME = 1
TITLE = 2


def display_schedule(meeting_list):
    print('Your schedule for the day:')
    for element in meeting_list:
        print(f'{int(element[START_TIME]):02} - {int(element[END_TIME]):02} {element[TITLE]}')
    if not element:
        print('(empty)')


def display_program_menu(menu_commands):
    print('Menu:')
    for option in menu_commands:
        print(f'({option[0]}) {option}')  # initial letter in brackets and option name


def display_message(message):
    print(display_colored_text(ORANGE, message))


def display_error_message(message):
    # print(f'ERROR: {message}')
    print(display_colored_text(RED, (f'ERROR: {message}')))


#  coloring function
ORANGE = '33m'
BLUE = '34m'
RED = '91m'
GREEN = '92m'
YELLOW = '93m'
CYAN = '96m'


def display_colored_text(color, message):
    colored_text = (f"\033[{color}{message}\033[00m")
    return colored_text
