from selenium import webdriver
from lxml import html
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import smtplib

options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

payload = {
	"username": "hmnufptcmeekukebpg@awdrt.com", 
	"password": "passwordabc", 
}

login_url = "https://www.bravopokerlive.com/login/"


driver.get (login_url)
driver.find_element_by_id("Email").send_keys(payload['username'])
driver.find_element_by_id ("Password").send_keys(payload['password'])
elem = driver.find_element_by_xpath('//*[@id="openid_form"]/p/button')

actions = ActionChains(driver)
actions.click(elem).perform()
mgmURL = "https://www.bravopokerlive.com/venues/mgm-national-harbor-casino-resort/"
driver.get(mgmURL)
if("5-10 NLH (600-2500)" in driver.page_source):
#if("10-25 NLH 1500-NoMax" in driver.page_source):	
	try:
		server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		print("server ssl setup")
		server_ssl.ehlo() 
		print("server ehlo")
		server_ssl.login("sendEmailToYuJie@gmail.com","hnghq45089q4h5")
		print("server login")
		server_ssl.sendmail("sendEmailToYuJie@gmail.com","aznhobo100@gmail.com","Call into 10/25 Phone number 3019715600")
		print("send mail")
		server_ssl.close()
		print("email sent")
	except:
		print('Something went wrong...')
else:
	print("doesn't work")
	

