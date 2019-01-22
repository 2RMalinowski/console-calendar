import ui
import storage
meeting_list = []


def add_new_meeting_to(meeting_list):
    new_meeting = [ui.get_input('Enter meeting title: '),
                   ui.get_input('Enter duration in hours (1 or 2): '),
                   ui.get_input('Enter start time: ')]
    meeting_list.append(new_meeting)
    ui.display_message('Meeting added')
    return meeting_list


def cancel_meeting_in(meeting_list):
    start_time = ui.get_input('Enter the start time: ')
    for meeting in meeting_list:
        if start_time in meeting:
            meeting_list.remove(meeting)
            ui.display_message('Meeting canceled')
            return meeting_list
