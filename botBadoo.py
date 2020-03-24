from selenium import webdriver
from time import sleep
import sys



class BadooBot():

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.like_count = 0
        self.user = ""
        self.passw = ""
        self.dislike_count = 0
        self.match_count = 0

    def login(self):
        url = self.driver.current_url
        if url != 'https://badoo.com':
            self.driver.get('https://badoo.com')
            ## Give browser time to navigate and give login popup
            ## Login
            login_facebook = self.driver.find_element_by_xpath('//*[@id="page"]/div[2]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
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
            ## Wait for site load
            sleep(8)

    def swipe_right(self):
        sleep(0.5)
        like_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()
        self.like_count += 1
        if self.like_count % 5 == 0:
            print("_Likes: " + str(self.like_count))

    def swipe_left(self):
        sleep(0.5)
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
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
                        try:
                            close_popup2()
                        except:
                            print("\n" + "Error: Something happened - You are probably out of likes for today.\n")
                            print("_Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count) + "\n")
                            print("_Total matches: " + str(self.match_count) + "\n")
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
                            close_popup2()
                        except:
                            print("\n" + "Error: Something happened - You are probably out of likes for today.\n")
                            print("_Total likes/dislikes: " + str(self.like_count) + "/" + str(self.dislike_count) + "\n")
                            print("_Total matches: " + str(self.match_count) + "\n")
                            sys.exit()

    ## functions for handling popups
    def close_popup(self):
        popup = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/div/div[1]')
        popup.click()
        sleep(1)

    def close_popup2(self):
        popup = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[3]/div[2]/span')
        popup.click()
        sleep(1)

    def close_match(self):
        popup_match = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/div[4]')
        popup_match.click()
        self.match_count += 1
        sleep(1)
