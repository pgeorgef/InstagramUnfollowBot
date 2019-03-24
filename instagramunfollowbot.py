from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramUnfollowBot():
    def __init__(self,username,password):
        self.profile = webdriver.FirefoxProfile()
        self.driver_locale='en'
        self.profile.set_preference('intl.accept_languages', self.driver_locale)
        self.driver =  webdriver.Firefox(firefox_profile=self.profile)
        self.username = username
        self.password = password

    def signIn(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.driver.find_element_by_name('username')
        usernameInput.send_keys(self.username)
        passwordInput = self.driver.find_element_by_name('password')
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.get('https://www.instagram.com/'+self.username)

    def openfollowerslist(self):
        following = self.driver.find_elements_by_css_selector('a ')
        following[2].click()
        time.sleep(5)

    def scroll(self):
        body = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', body)

    def pressunfollow(self):
        unfollow = self.driver.find_elements_by_css_selector('button')
        for button_search in unfollow:
            if(button_search.text == 'Unfollow'):
                button_search.click()
                break

    def unfollow(self):
        follower_list = self.driver.find_elements_by_css_selector('button') # get the list of followers
        cnt = 0
        for people in range( 1 , len(follower_list) ):
            if( follower_list[people].text == 'Following' ):
                cnt = cnt + 1
                follower_list[people].click()
                bot.pressunfollow()
                if(cnt%5==0):
                    bot.scroll()
                    time.sleep(2)
                    follower_list = self.driver.find_elements_by_css_selector('button') #update follower list after scroll
                    people = 1 # update people number
                print("Unfollowed "+str(cnt)+" people")
                time.sleep(60) # you can change it, but it should better be a high value


bot = InstagramUnfollowBot('yourusername' , 'yourpassword')
bot.signIn()
bot.openfollowerslist()
bot.unfollow()
