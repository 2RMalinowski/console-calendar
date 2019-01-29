import ui
import storage
meetings = storage.convert_to_tuples_of_ints()


START_TIME = 0
END_TIME = 1
TITLE = 2


def check_meeting_in_working_hours(duration, start_time):
    if start_time + duration > 18:
        return False
    else:
        return True


def check_meeting_overlpas(start_time, end_time, meeting_list):
    for meeting in meeting_list:
        if start_time == meeting[START_TIME] or end_time > meeting[START_TIME]:
            return False
        else:
            return True


# def check_meeting_to_cancel(start_time, meeting_list):
#     for meeting in meeting_list:
#             if start_time == meeting[START_TIME]:
#                 else:
#                     return False


def count_total_meetings_duration_in(meetings):
    meeting_duration_list = [meeting[END_TIME] - meeting[START_TIME] for meeting in meetings]
    ui.display_command_result(sum(meeting_duration_list))


# def compact(meetings):
#     pass
