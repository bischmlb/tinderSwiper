from botBadoo import *
from botTinder import *

if __name__ == '__main__':
    print("Actions:")
    print("\"Premium\" options are more ban secure as they add a chance to also swipe left once in a while. \nThis will reduce the chance of getting your account marked as bot")
    print("-----------------")
    print("1: Tinder")
    print("2: Tinder - Premium")
    print("3: Badoo")
    print("4: Badoo - Premium")
    print("-----------------")
    print("0: Exit")
    print("-----------------")

    input = input()
    if input == '1':
        print("Tinder ..\n")
        bot = TinderBot()
        bot.login()
        bot.autoswipe()
    elif input == '2':
        print("Tinder - Premium ..\n")
        bot = TinderBot()
        bot.login()
        bot.autoswipe_premium()
    elif input == '3':
        print("Badoo ..\n")
        bot = BadooBot()
        bot.login()
        bot.autoswipe()
    elif input == '4':
        print("Badoo - Premium ..\n")
        bot = BadooBot()
        bot.login()
        bot.autoswipe_premium()
    elif input == '0':
        sys.exit()
    else:
        print("InputError: Input not recognized")
