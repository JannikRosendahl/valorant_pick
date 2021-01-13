import sys
import mouse
import keyboard
import time

lock_in_coords = {'x': 959, 'y': 814}
# champion_icon_start_coords = {'x': 668, 'y': 885}
champion_icon_start_coords = {'x': 662, 'y': 898}
champion_icon_size = {'x': 80, 'y': 80}
champion_icon_border = {'x': 4, 'y': 4}

champion_list = ['Brimstone', 'Jett', 'Omen', 'Phoenix', 'Reyna', 'Sage', 'Sova', 'Breach', 'Cypher', 'Killjoy', 'Raze',
                 'Skye', 'Viper', 'Yoru']
# top left corner of the top left champion
champion_coords = {}

# calculate champion icon positions
for champion in champion_list:
    # 'spacer', we dont want to click the top left corner
    x_offset = champion_icon_size['x'] / 2
    y_offset = champion_icon_size['y'] / 2

    x_offset += ((champion_icon_size['x'] + champion_icon_border['x']) * (
            champion_list.index(champion) % ((len(champion_list) + 2 // 2) // 2)))
    y_offset += champion_icon_size['y'] + champion_icon_border['y'] if champion_list.index(
        champion) >= len(champion_list) / 2 else 0

    champion_coords[champion] = {'x': champion_icon_start_coords['x'] + x_offset,
                                 'y': champion_icon_start_coords['y'] + y_offset}

# check if command line argument is given
manual_input_required = False
if len(sys.argv) > 1:
    if champion_list.count(sys.argv[1].capitalize()) > 0:
        print('valid command line argument found: ' + sys.argv[1])
        champion_selection = sys.argv[1].capitalize()
    else:
        manual_input_required = True
else:
    manual_input_required = True

# if no valid command line argument was found, get input manually
if manual_input_required:
    print('enter champion choice as number:')
    for champion in champion_list:
        print((str(champion_list.index(champion) + 1) + ':').rjust(3, ' '), champion)
    choice = int(input())
    champion_selection = champion_list[choice - 1]

print('selected champion: ' + champion_selection)


# toggle mechanism
active = True


def flip_active():
    global active
    active = not active


print('standby, press ''esc'' to start')
keyboard.wait('esc')
keyboard.add_hotkey('esc', flip_active)

print('picking, press ''esc'' again to cancel')
while active:
    mouse.move(champion_coords[champion_selection]['x'], champion_coords[champion_selection]['y'])
    time.sleep(.05)
    mouse.click('left')
    mouse.move(lock_in_coords['x'], lock_in_coords['y'])
    time.sleep(.05)
    mouse.click('left')
print('terminating...')

