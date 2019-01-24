import ui
# from storage import meetings as meeting_list


def add_new_meeting_to(meeting_list):
    new_meeting = (ui.title('Enter meeting title: '),
                   ui.duration('Enter duration in hours (1 or 2): '),
                   ui.start_time('Enter start time: '))
    meeting_list.append(new_meeting)
    ui.display_message('Meeting added')


def cancel_meeting_in(meeting_list):
    start_time = input('Enter the start time: ')
    for meeting in meeting_list:
        if start_time in meeting:
            meeting_list.remove(meeting_list)
            ui.display_message('Meeting canceled')
