import ui
import storage
meetings = storage.import_data_from('meetings.txt')

START_TIME = 0
END_TIME = 1
TITLE = 2


def check_meeting_in_working_hours(duration, start_time):
    if start_time + duration > 18:
        return False
    else:
        return True


def check_meeting_overlpas(start_time, end_time, meeting_list):
    for hour in meeting_list:
        if start_time == int(hour[START_TIME]) or end_time > int(hour[START_TIME]):
            return False
        else:
            return True


def check_meeting_to_cancel(start_time, meeting_list):
    for meeting in meeting_list:
            if int(start_time) == meeting[0]:  # '0' means start time hour index
                return True
            else:
                return False
