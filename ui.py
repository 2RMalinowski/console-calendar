# getting input form user
def get_input(message):
    user_input = input(message)
    return user_input


#  displaying functions
def display_elements_of(any_list):
    for element in any_list:
        print(element)


def display_program_menu(menu_commands):
    for option in menu_commands:
        print(f'({option[0]}) {option}')


def display_error_message(message):
    print(message)
