from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys
import random

### Webscraper User Actions ###
# Click Login with facebook
# Fill out email
# Fill out password
# Click Log in

class TinderBot():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.user = ""
        self.passw = ""
        self.sendMatchMsg = False
        self.matchName = ""
        self.matchBesked = "Hej " + self.matchName + " =) " + "Du ser sød ud!"
        self.like_count = 0
        self.dislike_count = 0
        self.match_count = 0
        self.speed = 0.5

    def login(self):
        url = self.driver.current_url
        if url != 'https://tinder.com':
            self.driver.get('https://tinder.com')
            self.driver.maximize_window()
            ## Give browser time to navigate and give login popup
            sleep(3)
            ## Login
            loginBtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            loginBtn.click()
            sleep(3)
            login_facebook = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
            login_facebook.click()
            ## We will be prompted to enter login-information in new window, so we need to switch from base window to popup-window.
            ## Initialize base window
            base_window = self.driver.window_handles[0]
            ## Switching
            self.driver.switch_to_window(self.driver.window_handles[1])
            ## Selecting email, password, and logging in
            ## Handle email
            email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_input.send_keys(self.user)
            ## Handle password
            pass_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pass_input.send_keys(self.passw)
            ## Click login
            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()
            ## Now logged in, switch back to main window.
            self.driver.switch_to_window(base_window)
            ## Handle location popups .. allow all'
            sleep(8) # Wait for browser ..
            popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup1.click()
            popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup2.click()
            sleep(7)

    def more_options_exist(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
        except Exception:
            return False
        return True

    def swipe_right(self):
        sleep(self.speed)
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        self.like_count += 1
        if self.like_count % 5 == 0:
            print("> Likes: " + str(self.like_count))

    def swipe_left(self):
        sleep(self.speed)
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
        self.dislike_count += 1

    def autoswipe(self):
        while True:
            ## swipes right and closes popups on exceptions
            try:
                self.swipe_right()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    try:
                        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]').click() #antal nye likes
                    except Exception:
                            try:
                                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click() #føj tinder til startskærm
                            except Exception:
                                try:
                                    self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/button')
                                except Exception:
                                    print("\n" + "> INFO: Something happened - You are probably out of likes for today.\n")
                                    print("> Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count))
                                    print("> Total matches: " + str(self.match_count) + "\n")
                                    if self.match_count == 0:
                                        print("> Match/Like ratio: " + str(0) + "%\n")
                                    else:
                                        print("> Match/Like ratio: " + str(self.like_count/self.match_count) + "%\n")

                                    sys.exit()

    def autoswipe_premium(self):
        while True:
            try:
                value = int(round(random.random(),2)*100) # roll value
                if value < 23:
                    self.swipe_left()
                else:
                    self.swipe_right()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        try:
                            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]').click()
                        except Exception:
                            try:
                                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
                            except Exception:
                                print("\n" + "> INFO: Something happened - You are probably out of likes for today.\n")
                                print("> Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count))
                                print("> Total matches: " + str(self.match_count) + "\n")
                                if self.match_count == 0:
                                    print("> Match/Like ratio: " + str(0) + "%\n")
                                else:
                                    print("> Match/Like ratio: " + str(self.like_count/self.match_count) + "%\n")
                                sys.exit()


    ## functions for handling popups
    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        nameString = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[2]').getText()
        self.matchName = nameString.split()[0]
        if self.sendMatchMsg == True:
            ## Hvis der er sat en matchMsg sender vi beskeden ved tilfælde af match;
            stringBox = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            stringBox.send_keys(self.matchBesked)
            submitMsg = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
            submitMsg.click()

        popup_match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popup_match.click()
        self.match_count += 1
