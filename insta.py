from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
my_username = 'my_username'
my_password = 'my_password'
usernames = ['warri_or62']
messages = ['Hey! Pls follow my page', 'Hey, how you doing?', 'Hey']
comments =['Good','Nice','Awesome','hi','hello']
between_messages = 2000
browser = webdriver.Chrome('C:/Users/UBAI/oo/chromedriver.exe')
browser.maximize_window()
def auth(username, password):
try:
browser.get('https://instagram.com')
time.sleep(random.randrange(2,4))
input_username = browser.find_element_by_name('username')
input_password = browser.find_element_by_name('password')
input_username.send_keys(username)
time.sleep(random.randrange(1,2))
input_password.send_keys(password)
time.sleep(random.randrange(1,2))
input_password.send_keys(Keys.ENTER)
time.sleep(random.randrange(3,5))
except Exception as err:
print(err)
browser.quit()
def send_message(users, messages):
try:
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/nav/div[2]/div
/div/div[3]/div/div[2]/a').click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').
click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/
div/div[2]/div/div[3]/div/button').click()
for user in users:
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/di
v/div[2]/input').send_keys(user)
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').f
ind_element_by_tag_name('button').click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2
]/div/button/div').click()
time.sleep(random.randrange(3,5))
text_area=browser.find_element_by_xpath('/html/body/div[1]/div/div/secti
on/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
text_area.send_keys(random.choice(messages))
time.sleep(random.randrange(3,5))
text_area.send_keys(Keys.ENTER)
print(f'Message successfully sent to {user}')
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[
2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]').click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('//div[@class="eLAPa"]').click()
for comment in comments:
time.sleep(random.randrange(3,5))
element = browser.find_element_by_class_name('_9AhH0')
actions=ActionChains(browser)
actions.double_click(element).perform()
print(f'successfully liked to {user}')
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article
/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
time.sleep(random.randrange(3,5))
text_area=browser.find_element_by_xpath('/html/body/div[6]/div[2]/
div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
text_area.send_keys(random.choice(comments))
time.sleep(random.randrange(3,5))
text_area.send_keys(Keys.ENTER)
print(f'comments successfully sent to {user}')
time.sleep(random.randrange(3,5))
actions = ActionChains(browser)
actions.send_keys(Keys.ARROW_RIGHT)
actions.perform()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/nav/div[
2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(random.randrange(3,5))
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[
2]/div/div/div[1]/div[1]/div/div[3]/button').click()
except Exception as err:
print(err)
browser.quit()
auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(usernames, messages)
browser.quit()