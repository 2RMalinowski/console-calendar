import modify


def import_data_from(source_file='meetings.txt'):
    list_of_meetings = []
    with open(source_file, 'r') as datafile:
        for line in datafile.readlines():
            list_of_meetings.append(tuple(line.strip().split(',')))
    return list_of_meetings


def export_data_to(data_source, dest_file='meetings.txt'):
    with open(dest_file, 'a') as destfile:
        destfile.write(''.join(modify.add_new_meeting_to(meeting_list)))
