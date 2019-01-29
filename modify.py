import ui
import converts_and_valids
CONFIRM_COLOR = ui.GREEN


def add_new_meeting_to(meeting_list):
    title = ui.title('Enter meeting title: ')
    duration = ui.duration('Enter duration in hours (1 or 2): ')
    while True:
        start_time = ui.start_time('Enter start time: ')
        if converts_and_valids.check_meeting_in_working_hours(duration, start_time):
            end_time = start_time + duration
            if converts_and_valids.check_meeting_overlpas(start_time, end_time, meeting_list):
                new_meeting = (start_time, end_time, title)
                meeting_list.append(new_meeting)
                ui.display_message(CONFIRM_COLOR, 'Meeting added')
                break
            else:
                ui.display_error_message('Meeting overlaps with existing meeting!')
        else:
            ui.display_error_message('Meeting is outside of your working hours (8 to 18)!')


def cancel_meeting_in(meeting_list):
    while True:
        start_time = ui.start_time('Enter the start time: ')
        for meeting in meeting_list:
            if int(start_time) == int(meeting[0]):
                # if converts_and_valids.check_meeting_to_cancel:
                meeting_list.remove(meeting)
                ui.display_message(CONFIRM_COLOR, 'Meeting canceled')
                break
            else:
                ui.display_error_message('There is no meeting starting at that time!')
