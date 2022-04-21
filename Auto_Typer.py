#Config:
text_file = "clones.txt"
clones_at_once = 1
min_input_tim_per_clone = 136
max_input_time_per_clone = 1



#Code:
import os
from numpy import number
from pynput.keyboard import Key, Controller
import time
import random


keyboard = Controller()
clone_list = []


clones = open(text_file, 'r')
for line in clones:
    if "\n" in line:
        clone_list.append(line)
clones.close()

clone_list = [l.replace("\n", "") for l in clone_list]

minimum_time = (len(clone_list) * (min_input_tim_per_clone) / clones_at_once / 60)
maximum_time = (len(clone_list) * (max_input_time_per_clone) / clones_at_once / 60)

if min_input_tim_per_clone < 1:
    print("Minimum input time must be greater than 1s")
    time.sleep(1.5)
    exit()

seconds = 5
two_clones = []

print(f"Starting in {seconds} seconds\nNeeds {minimum_time} - {maximum_time} minutes to complete.")

time.sleep(seconds)
    
for i in range(0, len(clone_list)):
    point = 1 * i

    two_clones.append(clone_list[point])

    if (len(two_clones) % clones_at_once) == 0:
        string_two_clones = str(two_clones)
        if "[" or "]" or "'" in string_two_clones:
            string_two_clones = string_two_clones.replace("'", "").replace("[", "").replace("]", "")
        length_2 = True
    else:
        length_2 = False

    if length_2 == True:
        keyboard.type(string_two_clones)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        two_clones = []

    time.sleep(random.uniform((min_input_tim_per_clone), (max_input_time_per_clone)))

print("Done!")