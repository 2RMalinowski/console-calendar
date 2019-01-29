def import_data_from(source_file='meetings.txt'):
    list_of_meetings_str = []
    with open(source_file, 'r') as datafile:
        for line in datafile.readlines():
            list_of_meetings_str.append(line.strip().split(','))
    return list_of_meetings_str


def convert_to_tuples_of_ints():
    converted_list = []
    meeting_list = import_data_from('meetings.txt')
    for meeting in meeting_list:
        new_list = []
        for element in meeting:
            try:
                new_list.append(int(element))
            except ValueError:
                new_list.append(element)
        converted_list.append(tuple(new_list))
    return converted_list


def export_data_to(data_source, dest_file='meetings.txt'):
    with open(dest_file, 'a') as destfile:
        print(data_source)
        for meeting in data_source:
            # destfile.write(','.join(meeting))
            print(','.join(meeting))

    # TypeError: sequence item 0: expected str instance, int found
