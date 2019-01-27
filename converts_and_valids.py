import ui
import storage
meetings = storage.meetings

START_TIME = 0
END_TIME = 1
TITLE = 2
HOUR_BEFORE_END = 17


def check_meeting_in_working_hours(duration, start_time):
    if start_time + duration > 18:
        return False
    else:
        return True


def check_meeting_overlpas(start_time, end_time, meeting_list):
    for hour in meeting_list:
        if start_time == hour[START_TIME] or end_time > hour[START_TIME]:
            return False
        else:
            return True
