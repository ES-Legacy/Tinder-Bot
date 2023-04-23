from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import creds

class TinderBot():
    def __init__(self):
        self.firefoxOptions = webdriver.FirefoxOptions()
        self.firefoxOptions.set_preference("geo.prompt.testing", True)
        self.firefoxOptions.set_preference("geo.prompt.testing.allow", True)
        self.firefoxOptions.set_preference('geo.wifi.uri', 'data:application/json,{"location": {"lat": ' + creds.latitude + ', "lng": ' + creds.longitude + ', "accuracy": 2000}')
        self.firefoxOptions.set_preference('dom.webnotifications.enabled', False)


        self.browser = webdriver.Firefox(options=self.firefoxOptions)
    
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
        
        #this switches us back to the base window, rather the tinder webpage
        self.browser.switch_to.window(baseWindow)
    
    def handleAllowLocation(self):
        sleep(5)
        locationAllowButton = bot.browser.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
        locationAllowButton.click()


bot = TinderBot()
bot.login()
bot.handleAllowLocation()