import time
import pyautogui
import keyboard
import pyperclip
import random

def convert(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# EDIT THESE SETTINGS
# THESE SETTINGS ARE MADE TO BE EASY TO CHANGE

# THE POSITION OF THE WORD TO COPY
x = 745
y = 585

# TRUE IF YOU WANT TO USE LONG WORDS, FALSE IF YOU WANT TO USE SHORT WORDS
long = True

# THIS SHOULD BE YOUR TXT FILE FOR ALL THE WORDS, LIKE A DICTIONARY
dictionary = 'words.txt'

# ENABLE TO RANDOMIZE THE WORDS INSTEAD, LONG WILL HAVE NO EFFECT
# random.shuffle(words)

words = sorted(convert(dictionary), key=len, reverse=long)

while True:
    if keyboard.is_pressed('insert'):
        pyautogui.moveTo(x, y)
        time.sleep(10)
        pyautogui.doubleClick()
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(10)
        text = pyperclip.paste()
        print('Locating...')
        for word in words:
            if text in word.lower() and True:
                pyautogui.moveTo(x, 1000)
                time.sleep(10)
                pyautogui.click()
                time.sleep(10)
                pyautogui.write(word, interval=0.1)
                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')
                words.remove(word)
                print(text + " " + word)
                break