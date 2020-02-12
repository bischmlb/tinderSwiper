from selenium import webdriver
from time import sleep
from secrets import username, password



class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

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
            sleep(5)

    def swipe_right(self):
        sleep(0.5)
        like_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()

    def swipe_left(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
        sleep(0.5)
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
                    self.close_match()

    ## functions for handling popups
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/div/div[1]')
        popup_3.click()
        sleep(1)

    def close_match(self):
        popup_match = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[1]/div[4]')
        popup_match.click()
