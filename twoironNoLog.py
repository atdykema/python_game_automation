import pyautogui
import time
import datetime
import random

orig_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))

rock1_x_click = 932

rock1_y_click = 535

rock1_x_check = 939

rock1_y_check = 541

rock2_x_click = 965

rock2_y_click = 565

rock2_x_check = 977

rock2_y_check = 565

rock1_color = orig_img.getpixel((rock1_x_check, rock1_y_check))
rock2_color = orig_img.getpixel((rock2_x_check, rock2_y_check))
last_click = 1
perm_items = 8
items_in_invent = perm_items
checks_for_timer = 0


def get_rand_click():
    return random.randrange(-5, 5, 1)


def get_rand_time():
    return random.randrange(-1000, 1000, 1) / 10000


def click_rock(rock):
    global checks_for_timer
    global last_click
    checks_for_timer = 0
    if rock == 1:
        pyautogui.moveTo(rock1_x_click + get_rand_click(), rock1_y_click + get_rand_click(), .1 + get_rand_time())
        get_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        while get_img.getpixel((rock1_x_check, rock1_y_check)) != rock1_color:
            time.sleep(.25)
            print("rock 1 sleeping")
            print(datetime.datetime.now())
            get_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        pyautogui.click()
        last_click = 1
    elif rock == 2:
        pyautogui.moveTo(rock2_x_click + get_rand_click(), rock2_y_click + get_rand_click(), .1 + get_rand_time())
        get_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        while get_img.getpixel((rock2_x_check, rock2_y_check)) != rock2_color:
            time.sleep(.25)
            print("rock 2 sleeping")
            print(datetime.datetime.now())
            get_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        pyautogui.click()
        last_click = 2


def drop():
    print("dropping...")
    print(datetime.datetime.now())
    start_pos_x = 1711
    start_pos_y = 725
    pyautogui.moveTo(start_pos_x, start_pos_y, .005 + get_rand_time()/10)
    pyautogui.keyDown('shift')
    curr_pos_x = start_pos_x
    curr_pos_y = start_pos_y
    for i in range(0, 4):
        curr_pos_x += 42
        for j in range(0, 6):
            curr_pos_y += 34
            pyautogui.moveTo(curr_pos_x, curr_pos_y, .01 + get_rand_time()/100)
            pyautogui.click()
        curr_pos_y = start_pos_y
    pyautogui.keyUp('shift')
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


def log():
    pyautogui.moveTo(1904, 36, 1)
    pyautogui.click()
    pyautogui.moveTo(1902, 747, 1)
    pyautogui.click()
    pyautogui.moveTo(1820, 958, 1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1033, 314, 1)
    pyautogui.click()
    #[CODE REMOVED TO PROTECT SECURITY, CONTAINED LOGIN INFORMATION]
    pyautogui.moveTo(879, 343, 1)
    pyautogui.click()
    time.sleep(15)
    pyautogui.click()
    pyautogui.moveTo(1607, 1019, 1)
    pyautogui.click()
    click_rock(1)


def main():
    global checks_for_timer
    global items_in_invent
    global last_click
    #drop()
    #log()
    click_rock(1)
    i = 0
    while 1:
        i += 1
        print("loops: ")
        print(i)
        if i % 10000 == 0:
            drop()
            log()
        print("entering loop")
        click_timer()
        time.sleep(.3)
        curr_img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        print("last click: ")
        print(last_click)
        if last_click == 1:
            print("working on rock 1")
            print(datetime.datetime.now())
            print(curr_img.getpixel((rock1_x_check, rock1_y_check)))
            print(rock1_color)
            if curr_img.getpixel((rock1_x_check, rock1_y_check)) != rock1_color:
                print("rock 1 is mined")
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(2)
        elif last_click == 2:
            print("working on rock 2")
            print(datetime.datetime.now())
            if curr_img.getpixel((rock2_x_check, rock2_y_check)) != rock2_color:
                print("rock 2 is mined")
                print(datetime.datetime.now())
                checks_for_timer = 0
                items_in_invent += 1
                if items_in_invent == 28:
                    drop()
                click_rock(1)


if __name__ == '__main__':
    main()
