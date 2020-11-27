import datetime
import time
import pyautogui
import random

orig_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
rock1_x_click = 988
rock1_y_click = 536
rock1_x_check = 999
rock1_y_check = 527
rock2_x_click = 967
rock2_y_click = 560
rock2_x_check = 972
rock2_y_check = 574
rock3_x_click = 930
rock3_y_click = 556
rock3_x_check = 962
rock3_y_check = 575
rock4_x_click = 958
rock4_y_click = 505
rock4_x_check = 966
rock4_y_check = 509
rock1_color = orig_img.getpixel((rock1_x_check, rock1_y_check))
rock2_color = orig_img.getpixel((rock2_x_check, rock2_y_check))
rock3_color = orig_img.getpixel((rock3_x_check, rock3_y_check))
rock4_color = orig_img.getpixel((rock4_x_check, rock4_y_check))
last_click = 1
perm_items = 8
items_in_invent = perm_items
checks_for_timer = 0


def click_rock(rock):
    global checks_for_timer
    global last_click
    if rock == 1:
        pyautogui.moveTo(rock1_x_click, rock1_y_click, .1)
        pyautogui.click()
        last_click = 1
    elif rock == 2:
        pyautogui.moveTo(rock2_x_click, rock2_y_click, .1)
        pyautogui.click()
        last_click = 2
    elif rock == 3:
        pyautogui.moveTo(rock3_x_click, rock3_y_click, .1)
        pyautogui.click()
        last_click = 3
    elif rock == 4:
        pyautogui.moveTo(rock4_x_click, rock4_y_click, .1)
        pyautogui.click()
        last_click = 4


def drop():
    print("dropping...")
    print(datetime.datetime.now())
    start_pos_x = 1711
    start_pos_y = 725
    pyautogui.moveTo(start_pos_x, start_pos_y, .3)
    pyautogui.keyDown("shift")
    curr_pos_x = start_pos_x
    curr_pos_y = start_pos_y
    for i in range(0, 4):
        curr_pos_x += 42
        for j in range (0, 6):
            curr_pos_y += 34
            pyautogui.moveTo(curr_pos_x, curr_pos_y, .3)
            pyautogui.click()
        curr_pos_y = start_pos_y
    pyautogui.keyUp("shift")
    global items_in_invent
    items_in_invent = perm_items


def click_timer():
    global last_click
    global checks_for_timer
    checks_for_timer = + 1
    if checks_for_timer > 10:
        if last_click == 1:
            click_rock(2)
        elif last_click == 2:
            click_rock(1)


def main():
    global checks_for_timer
    global items_in_invent
    print("Beginning script")
    click_rock(1)
    while 1:
        print("entering loop...")
        click_timer()
        print("check click timer")
        print("entering sleep")
        time.sleep(.1)
        main_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        if last_click == 1:
            print("Working on rock 1...")
            print(datetime.datetime.now())
            if main_img.getpixel((rock1_x_check, rock1_y_check)) != rock1_color:
                print(main_img.getpixel((rock1_x_check, rock1_y_check)))
                print(rock1_color)
                print("Mined rock 1")
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(2)
        elif last_click == 2:
            print("Working on rock 2...")
            print(datetime.datetime.now())
            print(main_img.getpixel((rock2_x_check, rock2_y_check)))
            print(rock2_color)
            if main_img.getpixel((rock2_x_check, rock2_y_check)) != rock2_color:
                print(main_img.getpixel((rock2_x_check, rock2_y_check)))
                print(rock2_color)
                print("Mined rock 2")
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(3)
        elif last_click == 3:
            print("Working on rock 3...")
            print(datetime.datetime.now())
            if main_img.getpixel((rock3_x_check, rock3_y_check)) != rock3_color:
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(4)
        elif last_click == 4:
            print("Working on rock 4...")
            print(datetime.datetime.now())
            if main_img.getpixel((rock4_x_check, rock4_y_check)) != rock4_color:
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(1)


if __name__ == '__main__':
    main()

