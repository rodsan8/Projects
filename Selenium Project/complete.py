from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from requests_html import HTMLSession, AsyncHTMLSession
import json
import requests
import webbrowser
import time



def selectProduct(key):
	url = 'https://www.supremenewyork.com/mobile_stock.json'
	driver.get(url)
	response = requests.get(url=url)
	data = json.loads(response.content.decode('utf-8'))
	mylist = []
	global mylists
	global link
	mylists = mylist
	for items in data['products_and_categories']:
		if items != 'new':
			categories = items
		for x in categories.split():
			for result in data['products_and_categories']['{}'.format(x)]:
				if keyword in result['name'].lower():
					print('Product Found!')
					name = result['name']
					id = result['id']
					link = 'https://www.supremenewyork.com/shop/{}'.format(id)
					mylist.append(id)
					driver.get(link)

def soldout(driver):
	try:
		driver.find_element_by_xpath("//*[contains(@class, 'button sold-out')]")
		print('SOLD OUT')
		seconditem(driver)
	except:
		driver.find_element_by_xpath("//*[contains(@value, 'add to cart')]")
		print('NOT SOLD OUT')

def soldout2(driver):
	try:
		driver.find_element_by_xpath("//*[contains(@class, 'button sold-out')]")
		print('SOLD OUT')
		thirditem(driver)
	except:
		driver.find_element_by_xpath("//*[contains(@value, 'add to cart')]")
		print('NOT SOLD OUT')

def seconditem(driver):
	driver.find_element_by_css_selector('.styles li:nth-of-type(2)').click()
	soldout2(driver)
	
def thirditem(driver):
	driver.find_element_by_css_selector('.styles li:nth-of-type(3)').click()
	soldout2(driver)

def selectSize(driver):
	try:
		driver.find_element_by_xpath("//select[@name='s']/option[text()='Small']").click()
		print('SMALL SELECTED')
	except:
		driver.find_element_by_xpath("//select[@name='s']/option[text()='Medium']").click()
		print('MEDIUM SELECTED')
	else:
		driver.find_element_by_xpath("//select[@name='s']/option[text()='Large']").click()
		print('LARGE SELECTED')
	
	add2cart = driver.find_element_by_xpath("//*[contains(@value, 'add to cart')]").click()
	print("ADDED TO CART")

	WebDriverWait(driver, 10)
	driver.find_element_by_xpath("//*[contains(@class, 'button checkout')]").click()
	

def billinginfo(driver):
	fullname = driver.find_element_by_xpath("//*[contains(@name, 'order[billing_name]')]")
	fullname.send_keys("name")
	email = driver.find_element_by_xpath("//*[contains(@name, 'order[email]')]")
	email.send_keys("email")
	tel = driver.find_element_by_xpath("//*[contains(@name, 'order[tel]')]")
	tel.send_keys("phone")
	addy = driver.find_element_by_xpath("//*[contains(@name, 'order[billing_address]')]")
	addy.send_keys("address")
	zipp = driver.find_element_by_xpath("//*[contains(@name, 'order[billing_zip]')]")
	zipp.send_keys("zip")
	city = driver.find_element_by_xpath("//*[contains(@name, 'order[billing_city]')]")
	city.send_keys("city")
	states = driver.find_element_by_xpath("//select[@name='order[billing_state]']/option[text()='FL']").click()

def cardinfo(driver):
	card = driver.find_element_by_id("rnsnckrn")
	card.send_keys("11111111111")
	cvv = driver.find_element_by_xpath("//*[contains(@id, 'orcer')]")
	cvv.send_keys("111")
	driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='12']").click()
	driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='2024']").click()
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()


options = Options()
driver = webdriver.Firefox(options = options)
print("\nHeadless Firefox browswer initiated.\n")

# Enter keyword here
keyword = ('Military Trench Coat').lower()
keylist = keyword.split(",")

for keyword in keylist:
    selectProduct(keyword)

for _ in range(240):
    try:
        if not mylists:
            print('Product Not Found, Will Look Again...')
            time.sleep(0.25)
            selectProduct(keyword)
    except Exception as e:
        print('{}: or Webstore Closed'.format(e))

start_time = time.time()
soldout(driver)

selectSize(driver)
try:
	WebDriverWait(driver, 2)
except:
	selectSize(driver)

billinginfo(driver)
try:
	WebDriverWait(driver, 50)
except:
	print("error in billing info")

cardinfo(driver)
try:
	WebDriverWait(driver, 10)
except:
	pass

print("--- %.4s seconds ---" % (time.time() - start_time))
print("PROJECT COMPLETE")


