from os import path
import json
from time import sleep
from pynput.keyboard import Controller as KeyboardController, Key

keyboard = KeyboardController()


def finnish():
    print("finnish !!!")


def json_spam(file):
    fp = open(file, "r")
    data = json.load(fp)
    fp.close()

    sleep(10)

    for i in data:
        keyboard.type(i)

        keyboard.press(Key.enter)
        sleep(0.3)
        keyboard.release(Key.enter)

    finnish()


def use_json(json_file):

    permission = input("You have 10 seconds to click on the text box after press ENTER-button (type 'b' to turn back) "
                       ": ")

    if permission == "b":
        start()
    elif permission == "":
        json_spam(json_file)


def help_json_path(json_file, text):
    while not path.exists(json_file) and not path.splitext(json_file)[1] == ".json":
        json_file = str(input(text))

        if json_file == "h":
            print(" If the JSON file (in array type) is in the same folder as this python file is , Enter the name of "
                  "your JSON name file For example : (json_file.json).", "\r\n", "If it is in a directory as same as "
                  "this python python file you can type (./DIRECTORY-NAME/JSON-FILE.json)")
            help_json_path(json_file, "Try again : ")
            print(path.splitext(json_file))
            print(type(path.splitext(json_file)))
            continue


    use_json(json_file)



def get_json_path(text):
    text = text
    json_file = str(input("Enter json file path: "))
    help_json_path(json_file, text)




def text_spam(text, num):
    sleep(10)
    for i in range(num, 0, -1):
        keyboard.type(text)

        keyboard.press(Key.enter)
        sleep(0.3)
        keyboard.release(Key.enter)
    finnish()


def not_json(text_input, num_input):
    permission = input("You have 10 seconds to click on the text box after press ENTER-button (type 'b' to turn back) "
                       ": ")
    if permission == "b":
        start()
    elif permission == "":
        text_spam(text_input, num_input)


def if_int(num_input):
    try:
        int(num_input)
        return True
    except ValueError:
        return False


def get_number(text_input):
    text_input = text_input
    num_input = input("Number of message : ")
    if if_int(num_input):
        num_input = int(num_input)
        not_json(text_input, num_input)
    else:
        get_number(text_input)


def get_text():
    text_input = str(input("Enter your text : "))
    get_number(text_input)


def start():
    json_input = str(input("Do you want to use json ? (y/n) : "))

    if json_input == "n":
        get_text()
    elif json_input == "y":
        get_json_path("Not exist, Try again (type 'h' for help): ")
    else:
        start()


start()
