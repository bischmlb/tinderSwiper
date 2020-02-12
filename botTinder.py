from selenium import webdriver
from time import sleep
from secrets import username, password

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

    def login(self):
        url = self.driver.current_url
        if url != 'https://tinder.com':
            self.driver.get('https://tinder.com')
            ## Give browser time to navigate and give login popup
            sleep(3)
            ## Login
            login_facebook = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
            login_facebook.click()
            ## We will be prompted to enter login-information in new window, so we need to switch from base window to popup-window.
            ## Initialize base window
            base_window = self.driver.window_handles[0]
            ## Switching
            self.driver.switch_to_window(self.driver.window_handles[1])
            ## Selecting email, password, and logging in
            ## Handle email
            email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_input.send_keys(username)
            ## Handle password
            pass_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pass_input.send_keys(password)
            ## Click login
            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()
            ## Now logged in, switch back to main window.
            self.driver.switch_to_window(base_window)
            ## Handle location popups .. allow all'
            sleep(2) # Wait for browser ..
            popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup1.click()
            popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup2.click()

    def swipe_right(self):
        sleep(0.5)
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def swipe_left(self):
        sleep(0.5)
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

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
                        print("\n" + "Error: Something happened - You are probably out of likes for today.")
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
                        print("\n" + "Error: Something happened - You are probably out of likes for today.")
                        sys.exit()



    ## functions for handling popups
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        popup_match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popup_match.click()
