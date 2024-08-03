from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By


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
        "B": "r",
        "B'": "i",
        "L": "o",
        "L'": "t",
        "F": "n",
        "F'": "s",
        "D'": Key.enter,
        "D": Key.space,
        "U'": 1,
        "U": -1,
    }
    return move_to_letter[move]

def replace_move_left(move: str):
    move_to_letter_left = {
        "R": "u",
        "R'": "g",
        "B": "h",
        "B'": "m",
        "L": "p",
        "L'": "l",
        "F": "c",
        "F'": "q",
        "D'": Key.enter,
        "D": Key.space,
        "U'": 0,
        "U": "z",
    }
    return move_to_letter_left[move]

def replace_move_right(move: str):
    move_to_letter_right = {
        "R": "d",
        "R'": "b",
        "B": "k",
        "B'": "x",
        "L": "v",
        "L'": "w",
        "F": "y",
        "F'": "f",
        "D'": Key.enter,
        "D": Key.space,
        "U'": "j",
        "U": 0,
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


def inverse_move(move: str):
    return f"{move}'" if "'" not in move else f"{move}".replace("'", "")

opt = Options()
opt.add_argument("--window-size=950,1100")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
driver.implicitly_wait(10)

driver.get("https://twizzle.net/play/") #consider using https://alpha.twizzle.net/explore/
keyboard = Controller()

check = ""
is_moving = False
state = 0
stack_of_algs = ['']
while True:
    link = driver.find_element(By.XPATH, "/html/body/div/div/a").text

    if link != check:
        check = link

        try:
            if 'moves' not in check:
                last_letter = check.split(" ")[-1]
                prev_last_letter = stack_of_algs[-1].split(" ")[-1]

                if len(check.split(" ")) < len(stack_of_algs[-1].split(" ")):
                    if last_letter == prev_last_letter:
                        turn = inverse_move(stack_of_algs[-1].split(" ")[-2])
                    else:
                        turn = inverse_move(prev_last_letter)
                elif "2" in last_letter:
                    turn = last_letter.replace("2", "")
                elif "2" in prev_last_letter and last_letter in prev_last_letter:
                    turn = inverse_move(last_letter)
                else:
                    turn = last_letter
                stack_of_algs.append(check)


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
        except:
            print("something didn't work")
