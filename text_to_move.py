def text_to_move(text: str) -> str:
    res = ""
    move_to_letter = {
        "R": "e",
        "R'": "a",
        "U": "r",
        "U'": "i",
        "L": "o",
        "L'": "t",
        "F": "n",
        "F'": "s",
        "D'": "\n",
        "D": " ",
        "B'": 1,
        "B": -1,
    }
    move_to_letter_left = {
        "R": "u",
        "R'": "g",
        "U": "h",
        "U'": "m",
        "L": "p",
        "L'": "l",
        "F": "c",
        "F'": "q",
        "D'": "\n",
        "D": " ",
        "B'": 0,
        "B": "z",
    }
    move_to_letter_right = {
        "R": "d",
        "R'": "b",
        "U": "k",
        "U'": "x",
        "L": "v",
        "L'": "w",
        "F": "y",
        "F'": "f",
        "D'": "\n",
        "D": " ",
        "B'": "j",
        "B": 0,
    }
    state = 0
    for letter in text:
        if state == 0:
            if get_key(letter, move_to_letter): #could be bad
                res += get_key(letter, move_to_letter) + " "
            elif get_key(letter, move_to_letter_left):
                state = -1
                res += "B " + get_key(letter, move_to_letter_left) + " "
            else:
                state = 1
                res += "B' " + get_key(letter, move_to_letter_right) + " "

        elif state == -1:
            if get_key(letter, move_to_letter_left):
                res += get_key(letter, move_to_letter_left) + " "
            elif get_key(letter, move_to_letter):
                res += "B' " + get_key(letter, move_to_letter) + " "
                state = 0
            else:
                state = 1
                res += "B2' " + get_key(letter, move_to_letter_right) + " "

        elif state == 1:
            if get_key(letter, move_to_letter_right):
                res += get_key(letter, move_to_letter_right) + " "
            elif get_key(letter, move_to_letter):
                state = 0
                res += "B " + get_key(letter, move_to_letter) + " "
            else:
                state = -1
                res += "B2 " + get_key(letter, move_to_letter_left) + " "

    return res + "D'"

def get_key(value, dic):
    for key, v in dic.items():
        if value == v:
            return key
    return False

while True:
    text = input("Enter text: ")
    print(text_to_move(text))
