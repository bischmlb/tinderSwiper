from botBadoo import *
from botTinder import *

if __name__ == '__main__':
    print("\n\nActions:")
    print("\"Premium\" options are more ban secure as they add a chance to also swipe left once in a while. \nThis will reduce the chance of getting your account marked as bot")
    print("-----------------")
    print("1: Tinder")
    print("2: Tinder - Premium")
    print("3: Badoo")
    print("4: Badoo - Premium")
    print("-----------------")
    print("0: Exit")
    print("-----------------\n\n")

    input = input("Choice: ")
    if input == '1':
        print("-----------------")
        print("Tinder..")
        print("-----------------")
        bot = TinderBot()
        bot.login()
        bot.autoswipe()
    elif input == '2':
        print("-----------------")
        print("Tinder - Premium..")
        print("-----------------")
        bot = TinderBot()
        bot.login()
        bot.autoswipe_premium()
    elif input == '3':
        print("-----------------")
        print("Badoo..")
        print("-----------------")
        bot = BadooBot()
        bot.login()
        bot.autoswipe()
    elif input == '4':
        print("-----------------")
        print("Badoo - Premium..")
        print("-----------------")
        bot = BadooBot()
        bot.login()
        bot.autoswipe_premium()
    elif input == '0':
        sys.exit()
    else:
        print("InputError: Input not recognized")
