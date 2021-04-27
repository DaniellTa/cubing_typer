from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pynput.keyboard import Key, Controller


def press(button):
    keyboard.press(button)
    keyboard.release(button)


def replace_move(move: str):
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    best layers:
        R, R', U, U', D', D, L', L, F, F', B', B
    common letters:
        e, a, r, i, o, t, n, s, l, c
    """
    move_to_letter = {
        "R": "e",
        "R'": "a",
        "U": "r",
        "U'": "i",
        "L": "o",
        "L'": "t",
        "F": "n",
        "F'": "s",
        "D'": Key.enter,
        "D": Key.space,
        "B'": 1,
        "B": -1,
    }
    return move_to_letter[move]

def replace_move_left(move: str):
    move_to_letter_left = {
        "R": "u",
        "R'": "g",
        "U": "h",
        "U'": "m",
        "L": "p",
        "L'": "l",
        "F": "c",
        "F'": "q",
        "D'": Key.enter,
        "D": Key.space,
        "B'": 0,
        "B": "z",
    }
    return move_to_letter_left[move]

def replace_move_right(move: str):
    move_to_letter_right = {
        "R": "d",
        "R'": "b",
        "U": "k",
        "U'": "x",
        "L": "v",
        "L'": "w",
        "F": "y",
        "F'": "f",
        "D'": Key.enter,
        "D": Key.space,
        "B'": "j",
        "B": 0,
    }
    return move_to_letter_right[move]



def press_arrow(move: str):
    arrows = {
        "R": Key.up,
        "R'": Key.down,
        "U": Key.left,
        "U'": Key.right
    }
    return arrows[move]


def release_arrow(move: str):
    arrows = {
        "R": Key.down,
        "R'": Key.up,
        "U": Key.right,
        "U'": Key.left
    }
    return arrows[move]


opt = Options()
opt.add_argument("--window-size=950,1100")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
driver.implicitly_wait(10)

driver.get("https://twizzle.net/play/")
keyboard = Controller()

check = ""
is_moving = False
state = 0
while True:
    link = driver.find_element_by_xpath(
        "/html/body/div/div/a").get_attribute("href")
    if link != check:
        check = link

        try:
            last = link.rfind("=") + 1
            turn = link[last:].replace("-", "'")
            
            if state == -1:
                if isinstance(replace_move_left(turn), int):
                    state = replace_move_left(turn)
                else:
                    keyboard.press(replace_move_left(turn))
                    if replace_move_left(turn) == Key.enter:
                        state = 0
            elif state == 0:
                if isinstance(replace_move(turn), int):
                    state = replace_move(turn)
                else:
                    keyboard.press(replace_move(turn))
            elif state == 1:
                if isinstance(replace_move_right(turn), int):
                    state = replace_move_right(turn)
                else:
                    keyboard.press(replace_move_right(turn))
                    if replace_move_right(turn) == Key.enter:
                        state = 0
            driver.find_element_by_xpath(
                '/html/body/div/div/button[1]').click()
        except:
            driver.find_element_by_xpath(
                '/html/body/div/div/button[1]').click()


