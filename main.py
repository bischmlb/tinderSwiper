from botBadoo import *
from botTinder import *
from getpass import getpass

def setUser():
    print("\n\nIn order to log into your account, the program will need your login credentials.")
    print("The data input will NOT be recorded and is only used for this session.")
    print("Source code can be found at the github repository: \n > https://github.com/bischmlb/tinderSwiper.git ")
    print("\n-----------------")
    username = input("Username(Facebook email): ")
    if ("@" in username):
        return username
    else:
        print("> ERROR: The given username is not an email address. Please try again. \n")
        sys.exit()

def setPass():
    password = getpass("Password(Facebook password): ")
    replacementPass = ''
    for i in password:
        replacementPass = '*' + replacementPass
    print(replacementPass)
    print("-----------------")
    return password


if __name__ == '__main__':
    ## User credentials to be used
    username = setUser()
    password = setPass()

    ## Actions
    print("\nActions:")
    print("\"Premium\" options are more ban secure as they add a chance to also swipe left once in a while. \nThis will reduce the chance of getting your account flagged as bot \nUse at OWN risk! :) \nProcess can be interrupted anytime with 'CTRL + C'")
    print("-----------------")
    print("1: Tinder")
    print("2: Tinder - Premium")
    print("3: Badoo")
    print("4: Badoo - Premium")
    print("-----------------")
    print("0: Exit")
    print("-----------------\n\n")

    inputChoice = input("Choice: ")
    swipeSpeed = input("Set swipe speed 1-9(default=5, higher=faster): ")
    swipeSD = (10-int(swipeSpeed))/10
    sendMsg = input("(**NOT YET IMPLEMENTED**)Do you want to send msg to new match in case of match? Y/N or y/n: ")
    if sendMsg == 'Y' or sendMsg == 'y':
        matchMsg = input("Set standard MATCH_message: ")

    if inputChoice == '1':
        print("-----------------")
        print("(1) Tinder..")
        print("-----------------")
        bot = TinderBot()

        if sendMsg == 'Y' or sendMsg == 'y':
            bot.sendMatchMsg = True
            bot.matchBesked = matchMsg
            print("Setting MATCH initial message to: \"" + bot.matchBesked + "\"")
        else:
            bot.sendMatchMsg = False
        bot.user = username
        bot.passw = password
        bot.speed = swipeSD
        try:
            bot.login()
        except Exception:
            print(" > ERROR: Login unsuccessful. Please try again.\n")
            sys.exit()
        bot.autoswipe()

    elif inputChoice == '2':
        print("-----------------")
        print("(2) Tinder - Premium..")
        print("-----------------")
        bot = TinderBot()
        if sendMsg == 'Y' or sendMsg == 'y':
            bot.sendMatchMsg = True
            bot.matchBesked = matchMsg
            print("Setting MATCH initial message to: \"" + bot.matchBesked + "\"")
        else:
            bot.sendMatchMsg = False
        bot.user = username
        bot.passw = password
        bot.speed = swipeSD
        try:
            bot.login()
        except Exception:
            print(" > ERROR: Login unsuccessful. Please try again.\n")
            sys.exit()
        bot.autoswipe_premium()

    elif inputChoice == '3':
        print("-----------------")
        print("(3) Badoo..")
        print("-----------------")
        bot = BadooBot()
        if sendMsg == 'Y' or sendMsg == 'y':
            bot.sendMatchMsg = True
            bot.matchBesked = matchMsg
            print("Setting MATCH initial message to: \"" + bot.matchBesked + "\"")
        else:
            bot.sendMatchMsg = False
        bot.user = username
        bot.passw = password
        bot.speed = swipeSD
        try:
            bot.login()
        except Exception:
            print(" > ERROR: Login unsuccessful. Please try again.\n")
            sys.exit()
        bot.autoswipe()

    elif inputChoice == '4':
        print("-----------------")
        print("(4) Badoo - Premium..")
        print("-----------------")
        bot = BadooBot()
        if sendMsg == 'Y' or sendMsg == 'y':
            bot.sendMatchMsg = True
            bot.matchBesked = matchMsg
            print("Setting MATCH initial message to: \"" + bot.matchBesked + "\"")
        else:
            bot.sendMatchMsg = False
        bot.user = username
        bot.passw = password
        bot.speed = swipeSD
        try:
            bot.login()
        except Exception:
            print(" > ERROR: Login unsuccessful. Please try again.\n")
            sys.exit()
        bot.autoswipe_premium()

    elif inputChoice == '0':
        sys.exit()
    else:
        print("InputError: Input not recognized")
