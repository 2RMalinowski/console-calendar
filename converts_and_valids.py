import ui
from storage import meetings

TITLE = 0
DURATION = 1
START_TIME = 2
HOUR_BEFORE_END = 17


def convert_duration_to_meeting_hours(meeting_list):
    interval_and_title_list = []
    for element in meeting_list:
        end_meeting_hour = element[START_TIME] + element[DURATION]
        interval_and_title_list.append((element[START_TIME], end_meeting_hour, element[TITLE]))
    # ui.display_schedule(interval_and_title_list)
    return interval_and_title_list


def check_meeting_in_working_hours(meeting):
    meeting_start_time = meeting[START_TIME]
    meeting_duration = meeting[DURATION]
    if meeting_start_time + meeting_duration > 18:
        return False
    else:
        return True


# def check_meeting_overlpas(meeting, meetings):
#     interval_and_title_list = convert_duration_to_meeting_hours(meetings)
#     # meeting_end_time = meeting[START_TIME] + meeting[DURATION]
#     start_time = meeting[START_TIME]
#     for hours in interval_and_title_list:
#         if start_time in range(hours[0], hours[1]):
#             return False
#         else:
#             return True


    # start_time_hours_list = [element[START_TIME] for element in meeting_list]
    # duration = ui.duration
    # for hour in start_time_hours_list:
    #     if hour + duration > HOUR_BEFORE_END


#     def check_meeting_in_working_hours(meeting):
#     meeting_start_time = meeting[START_TIME]
#     meeting_duration = meeting[DURATION]
#     if meeting_start_time + meeting_duration > 18:
#         return False
#     else:
#         return True


# def check_meeting_overlpas(meeting, meetings):
#     interval_and_title_list = convert_duration_to_meeting_hours(meetings)
#     # meeting_end_time = meeting[START_TIME] + meeting[DURATION]
#     start_time = meeting[START_TIME]
#     for hours in interval_and_title_list:
#         if start_time in range(hours[0], hours[1]):
#             return False
#         else:
#             return True

