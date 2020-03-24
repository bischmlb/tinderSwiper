from selenium import webdriver
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
        self.driver = webdriver.Chrome()
        self.user = ""
        self.passw = ""
        self.like_count = 0
        self.dislike_count = 0
        self.match_count = 0

    def login(self):
        url = self.driver.current_url
        if url != 'https://tinder.com':
            self.driver.get('https://tinder.com')
            ## Give browser time to navigate and give login popup
            sleep(5)
            ## Login
            login_facebook = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button')
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
        sleep(0.5)
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        self.like_count += 1
        if self.like_count % 5 == 0:
            print("> Likes: " + str(self.like_count))

    def swipe_left(self):
        sleep(0.5)
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
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        print("\n" + "> INFO: Something happened - You are probably out of likes for today.\n")
                        print("> Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count))
                        print("> Total matches: " + str(self.match_count) + "\n")
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
                        print("\n" + "> INFO: Something happened - You are probably out of likes for today.\n")
                        print("> Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count))
                        print("> Total matches: " + str(self.match_count) + "\n")
                        sys.exit()



    ## functions for handling popups
    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        popup_match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popup_match.click()
        self.match_count += 1
