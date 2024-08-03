def text_to_move(text: str) -> str:
    res = ""
    move_to_letter = {
        "R": "e",
        "R'": "a",
        "B": "r",
        "B'": "i",
        "L": "o",
        "L'": "t",
        "F": "n",
        "F'": "s",
        "D'": "\n",
        "D": " ",
        "U'": 1,
        "U": -1,
    }
    move_to_letter_left = {
        "R": "u",
        "R'": "g",
        "B": "h",
        "B'": "m",
        "L": "p",
        "L'": "l",
        "F": "c",
        "F'": "q",
        "D'": "\n",
        "D": " ",
        "U'": 0,
        "U": "z",
    }
    move_to_letter_right = {
        "R": "d",
        "R'": "b",
        "B": "k",
        "B'": "x",
        "L": "v",
        "L'": "w",
        "F": "y",
        "F'": "f",
        "D'": "\n",
        "D": " ",
        "U'": "j",
        "U": 0,
    }
    state = 0
    for letter in text:
        if state == 0:
            if get_key(letter, move_to_letter): #could be bad
                res += get_key(letter, move_to_letter) + " "
            elif get_key(letter, move_to_letter_left):
                state = -1
                res += "U " + get_key(letter, move_to_letter_left) + " "
            else:
                state = 1
                res += "U' " + get_key(letter, move_to_letter_right) + " "

        elif state == -1:
            if get_key(letter, move_to_letter_left):
                res += get_key(letter, move_to_letter_left) + " "
            elif get_key(letter, move_to_letter):
                res += "U' " + get_key(letter, move_to_letter) + " "
                state = 0
            else:
                state = 1
                res += "U2' " + get_key(letter, move_to_letter_right) + " "

        elif state == 1:
            if get_key(letter, move_to_letter_right):
                res += get_key(letter, move_to_letter_right) + " "
            elif get_key(letter, move_to_letter):
                state = 0
                res += "U " + get_key(letter, move_to_letter) + " "
            else:
                state = -1
                res += "U2 " + get_key(letter, move_to_letter_left) + " "

    return res + "D'"

def get_key(value, dic):
    for key, v in dic.items():
        if value == v:
            return key
    return False

while True:
    text = input("Enter text: ")
    print(text_to_move(text))
