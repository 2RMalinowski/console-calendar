import ui
from storage import meetings

TITLE = 0
START_TIME = 1
DURATION = 2


def convert_duration_to_meeting_hours(meeting_list):
    interval_and_title_list = []
    for element in meeting_list:
        end_meeting_hour = element[DURATION] + element[START_TIME]
        interval_and_title_list.append((element[DURATION], end_meeting_hour, element[TITLE]))
    ui.display_schedule(interval_and_title_list)
    # return interval_and_title_list
