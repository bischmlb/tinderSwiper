from botBadoo import *
from botTinder import *

def setUser():
    print("\n\nIn order to log into your account, the program will need your login credentials.")
    print("The data input will NOT be recorded and is only used for this session.")
    print("Source code can be found at the github repository: \n > https://github.com/bischmlb/tinderSwiper.git ")
    print("\n-----------------")
    username = input("Username(Facebook email): ")
    return username

def setPass():
    password = input("Password(Facebook password): ")
    print("-----------------")
    return password


if __name__ == '__main__':
    username = setUser()
    password = setPass()
    print("\n\nActions:")
    print("\"Premium\" options are more ban secure as they add a chance to also swipe left once in a while. \nThis will reduce the chance of getting your account flagged as bot \nUse at OWN risk! :)")
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
        print("(1) Tinder..")
        print("-----------------")
        bot = TinderBot()
        bot.user = username
        bot.passw = password
        bot.login()
        bot.autoswipe()
    elif input == '2':
        print("-----------------")
        print("(2) Tinder - Premium..")
        print("-----------------")
        bot = TinderBot()
        bot.user = username
        bot.passw = password
        bot.login()
        bot.autoswipe_premium()
    elif input == '3':
        print("-----------------")
        print("(3) Badoo..")
        print("-----------------")
        bot = BadooBot()
        bot.user = username
        bot.passw = password
        bot.login()
        bot.autoswipe()
    elif input == '4':
        print("-----------------")
        print("(4) Badoo - Premium..")
        print("-----------------")
        bot = BadooBot()
        bot.user = username
        bot.passw = password
        bot.login()
        bot.autoswipe_premium()
    elif input == '0':
        sys.exit()
    else:
        print("InputError: Input not recognized")
