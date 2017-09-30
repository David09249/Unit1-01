# Created by: David Wang
# Created on: 19-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit1-01
# This program displays school names and their mascot

import ui

def mother_teresa_touch_up_inside(sender):
    view['school_name_label'].text = 'Mother Teresa HS'
    view['mascot_label'].text = 'Titans'
    
def st_joe_touch_up_inside(sender):
    view['school_name_label'].text = 'St. Joe HS'
    view['mascot_label'].text = 'Jaguars'
    
def st_mark_touch_up_inside(sender):
    view['school_name_label'].text = 'St. Mark HS'
    view['mascot_label'].text = 'Lions'

view = ui.load_view()
view.present('full_screen')
