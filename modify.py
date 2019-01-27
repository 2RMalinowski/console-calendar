import ui
import converts_and_valids


# def add_new_meeting_to(meeting_list):
#     new_meeting = (ui.title('Enter meeting title: '),
#                    ui.duration('Enter duration in hours (1 or 2): '),
#                    ui.start_time('Enter start time: '))
#     # and converts_and_valids.check_meeting_overlpas(ui.start_time, ui.duration):
#     if converts_and_valids.check_meeting_in_working_hours(new_meeting):
#         meeting_list.append(new_meeting)
#         ui.display_message('Meeting added')
#     else:
#         ui.display_error_message('Meeting is outside of your working hours (8 to 18)!')


def add_new_meeting_to(meeting_list):
    title = ui.title('Enter meeting title: ')
    duration = ui.duration('Enter duration in hours (1 or 2): ')
    while True:
        start_time = ui.start_time('Enter start time: ')
        end_time = start_time + duration
        if converts_and_valids.check_meeting_in_working_hours(duration, start_time):
            new_meeting = (start_time, end_time, title)
            meeting_list.append(new_meeting)
            break
        else:
            ui.display_error_message('Meeting is outside of your working hours (8 to 18)!')














def cancel_meeting_in(meeting_list):
    start_time = ui.start_time_of_meeting_to_remove('Enter the start time: ')
    for meeting in meeting_list:
        if int(start_time) == meeting[2]:  # '2' means start time hour index
            meeting_list.remove(meeting)
            ui.display_message('Meeting canceled')
        else:
            ui.display_error_message('There is no meeting starting at that time!')
