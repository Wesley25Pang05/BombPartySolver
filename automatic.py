import time
from random import randint
import cv2
import numpy as np
import pyautogui
import pyperclip

def is_image_on_screen(target_image_path, threshold=0.8):
    screenshot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
    target_image = cv2.imread(target_image_path, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return True
    else:
        return False

def convert(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


# EDIT THESE SETTINGS
# MADE TO BE EASY TO CHANGE

# THE POSITION OF THE WORD TO COPY
x = 745
y = 585

# DELAY BETWEEN ACTIONS (SECONDS / ACTION)
action = 0.01

# DELAY IN TYPING (SECONDS / CHARACTER)
typing = 0.1

# DELAY BEFORE TYPING (SECONDS)
answer = 0

# DELAY ADDED BEFORE TYPING BASED ON LETTERS (SECONDS * LETTERS)
letterDelay = 0.05

# CHANCE FOR A RANDOM LETTER TO BE REMOVED AKA MAKE A MISTAKE, THEN REWRITTEN (1 / NUM)
messUp = 5

# THIS SHOULD BE YOUR TXT FILE FOR ALL THE WORDS, LIKE A DICTIONARY
dictionary = 'words.txt'

# TRUE IF YOU WANT TO USE LONG WORDS, FALSE IF YOU WANT TO USE SHORT WORDS
long = True
words = sorted(convert(dictionary), key=len, reverse=long) # DO NOT EDIT THIS LINE

# ENABLE TO RANDOMIZE THE WORDS INSTEAD, LONG WILL HAVE NO EFFECT
# random.shuffle(words)

print('Running!')
while True:
    isUP = not(is_image_on_screen('image.jpg'))
    isTyping = is_image_on_screen('type.jpg')
    if isUP and isTyping:
        pyautogui.moveTo(x, y)
        time.sleep(action)
        pyautogui.doubleClick()
        time.sleep(action)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(action)
        text = pyperclip.paste()
        print('Locating...')
        for word in words:
            if text in word.lower():
                pyautogui.moveTo(x, 980)
                time.sleep(action)
                pyautogui.click()
                time.sleep(answer + letterDelay * len(word))
                messedUp = 0
                while randint(1, messUp + messedUp) == 1:
                    random_index = randint(0, len(word)-1)
                    pyautogui.write(word[:random_index] + word[random_index + 1:], interval=typing)
                    pyautogui.keyDown('enter')
                    pyautogui.keyUp('enter')
                    messedUp = messedUp + 1
                    time.sleep(action)
                pyautogui.write(word, interval=typing)
                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')
                words.remove(word)
                print(text + " " + word)
                break