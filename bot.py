from tinderBot import *
from badooBot import *

if __name__ == '__main__':
    print("Actions:")
    print("_________________")
    print("autoswipe:")
    print("1 - Tinder")
    print("2 - Badoo")

    input = input()
    if input == '1':
        bot = TinderBot()
        bot.login()
        bot.autoswipe()
    elif input == '2':
        bot = BadooBot()
        bot.login()
        bot.autoswipe()
    else:
        print("input not recognized")
