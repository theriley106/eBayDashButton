import requests
import bs4
import time
from selenium import webdriver
import sys

class eBay(object):
	def __init__(self, username=None, password=None):
				
		self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		self.driver = webdriver.PhantomJS()
		if username == None:
			self.username = None
			self.password = None
			self.guest = True
		else:
			self.username = username
			self.password = password
			self.guest = False

	def buyItem(self, itemNum=sys.argv[1]):
		self.driver.get("https://pay.ebay.com/gxo?action=create&rypsvc=true&pagename=ryp&item={}&quantity=1&transactionid=-1&rev=0".format(itemNum))
		if self.guest == False:
			print("Uncomment out lines 27-37 in main.py if you actually want to check out")
			#Uncomment the below section if you actually want it to check out :)
			'''self.driver.find_element_by_id("binBtn_btn").click()
			self.driver.find_element_by_xpath("//*[text()='No Thanks']")
			self.driver.save_screenshot('screen.png')
			if self.guest == False:
				self.driver.find_element_by_id("userid").clear()
				self.driver.find_element_by_id("userid").send_keys(self.username)
				self.driver.find_element_by_id("pass").clear()
				self.driver.find_element_by_id("pass").send_keys(self.password)
			else:
				self.driver.find_element_by_xpath("//*[text()='No Thanks']")'''
		self.driver.save_screenshot('screen.png')


	
		

if __name__ == "__main__":
	e = eBay()
	e.buyItem()

