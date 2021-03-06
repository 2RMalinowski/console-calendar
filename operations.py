import ui
import storage


START_TIME = 0
END_TIME = 1
TITLE = 2
MESSAGE_COLOR = ui.ORANGE


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


def count_total_meetings_duration_in(meeting_list):
    meeting_duration_list = [meeting[END_TIME] - meeting[START_TIME] for meeting in meeting_list]
    ui.display_message(MESSAGE_COLOR, f'Total meeting duration: {sum(meeting_duration_list)}')

# def compact(meetings):
#     pass
