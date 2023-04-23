from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import creds

class TinderBot():
    def __init__(self):
        self.browser = webdriver.Firefox()
    
    # Anytime that sleep() is envoked is simply due to latency conflict. Sometimes the page might not finish loading and be able to process the next step, sleep lets our app maintain flow of automated steps and NOT break.
    def login(self):
        self.browser.get("https://www.tinder.com")

        sleep(2)
        
        loginButton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
        loginButton.click()

        facebookButton = self.browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div")
        facebookButton.click()

        baseWindow = self.browser.window_handles[0]

        sleep(3)

        #switch to facebook login window
        self.browser.switch_to.window(self.browser.window_handles[1])
        
        facebookUsername = self.browser.find_element(By.XPATH, '//*[@id="email"]')
        facebookUsername.send_keys(creds.username + Keys.TAB)
        
        facebookPassword = self.browser.find_element(By.XPATH, '//*[@id="pass"]')
        facebookPassword.send_keys(creds.password + Keys.TAB)

        facebookLoginButton = self.browser.find_element(By.ID, 'loginbutton')

        facebookLoginButton.click()

bot = TinderBot()
bot.login()



        



    
            

