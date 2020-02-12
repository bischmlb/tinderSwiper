from botBadoo import *
from botTinder import *

if __name__ == '__main__':
    print("Actions:")
    print("-----------------")
    print("1: Tinder")
    print("2: Badoo")
    print("-----------------")
    print("0: Exit")
    print("-----------------")

    input = input()
    if input == '1':
        bot = TinderBot()
        bot.login()
        bot.autoswipe()
    elif input == '2':
        bot = BadooBot()
        bot.login()
        bot.autoswipe()
    elif input == '0':
        sys.exit()
    else:
        print("InputError: Input not recognized")
