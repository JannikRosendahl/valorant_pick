import mouse
import time
import keyboard
import sys


class Point:
    x = 0
    y = 0


def new_point(x, y):
    p = Point()
    p.x = x
    p.y = y
    return p


def get_champion_point(champ_choice):
    if champ_choice == 1:
        return new_point(710, 930)
    elif champ_choice == 2:
        return new_point(795, 930)
    elif champ_choice == 3:
        return new_point(880, 930)
    elif champ_choice == 4:
        return new_point(965, 930)
    elif champ_choice == 5:
        return new_point(1050, 930)
    elif champ_choice == 6:
        return new_point(1135, 930)
    elif champ_choice == 7:
        return new_point(1220, 930)
    elif champ_choice == 8:
        return new_point(710, 1000)
    elif champ_choice == 9:
        return new_point(795, 1000)
    elif champ_choice == 10:
        return new_point(880, 1000)
    elif champ_choice == 11:
        return new_point(965, 1000)
    elif champ_choice == 12:
        return new_point(1050, 1000)
    elif champ_choice == 13:
        return new_point(1135, 1000)
    else:
        return new_point(0, 0)


# toggle mechanism
active = False


def flip_active():
    global active
    active = not active


keyboard.add_hotkey('esc', flip_active)

print('enter champion choice as number:')
print('1: Brimstone')
print('2: Jett')
print('3: Omen')
print('4: Phoenix')
print('5: Reyna')
print('6: Sage')
print('7: Hanzo')
print('8: Breach')
print('9: Cypher')
print('10: Killjoy')
print('11: Raze')
print('12: Illaoi')
print('13: Akali')
choice = int(input())
print('standby, press ''esc'' to start')

champion_point = get_champion_point(choice)
lock_in = new_point(1000, 800)

''' test
for i in range(13):
    champ = get_champion_point(i)
    mouse.move(champ.x, champ.y)
    time.sleep(.25)
    mouse.move(lock_in.x, lock_in.y)
    time.sleep(.25)
'''

champ = get_champion_point(choice)
keyboard.wait('esc')
print('picking, press ''esc'' again to cancel')
while active:
    mouse.move(champ.x, champ.y)
    time.sleep(.05)
    mouse.click('left')
    mouse.move(lock_in.x, lock_in.y)
    time.sleep(.05)
    mouse.click('left')
print('terminating...')
