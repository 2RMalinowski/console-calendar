import ui

CONFIRM_COLOR = ui.GREEN


def import_data_from(source_file):
    list_of_meetings_str = []
    with open(source_file, 'r') as datafile:
        for line in datafile.readlines():
            list_of_meetings_str.append(line.strip().split(','))
    return list_of_meetings_str


def convert_to_tuples_of_ints(strings_list):
    list_of_meetings_int = []
    for meeting in strings_list:
        meeting_parameters_list = []
        for element in meeting:
            try:
                meeting_parameters_list.append(int(element))
            except ValueError:
                meeting_parameters_list.append(element)
        list_of_meetings_int.append(tuple(meeting_parameters_list))
    return list_of_meetings_int


def load_meetings(source_file='meetings.txt'):
    return convert_to_tuples_of_ints(import_data_from(source_file))


def convert_to_list_of_strigs_from(mixed_list):
    list_of_meetings_str = []
    for meeting in mixed_list:
        meeting_parameters_list = []
        for element in meeting:
            meeting_parameters_list.append(str(element))
        list_of_meetings_str.append(meeting_parameters_list)
    return list_of_meetings_str


def export_data_to(data_source, dest_file='meetings.txt'):
    list_of_meetings_str = convert_to_list_of_strigs_from(data_source)
    with open(dest_file, 'w') as destfile:
        for meeting in list_of_meetings_str:
            destfile.write(','.join(meeting) + '\n')
            print(','.join(meeting))
        ui.display_message(CONFIRM_COLOR, 'Meeting added')
