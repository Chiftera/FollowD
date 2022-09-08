import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random as rd
from selenium.webdriver.support import expected_conditions as EC


class FollowD:

	def __init__(self):

		self.driver=uc.Chrome()

	def click_x(self,xpath):
	    
	    if "/"  in xpath:
	        method=By.XPATH
	    elif ">" in xpath:
	        method=By.CSS_SELECTOR
	    print(method)
	    obj=self.driver.find_element(method,xpath)
	    self.bsleep()
	    obj.click()
	def send_txt(self,obj,txt):
	    obj.click()
	    self.bsleep()
	    obj.send_keys(txt)


	def bsleep(self):
	    time.sleep(rd.randint(1,5))

	def follow(self,site):
		if site=='twitter':	
			self.driver.get("https://twitter.com/login")
			time.sleep(7)
			self.send_txt(self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'),'Aboujotaro')
			self.click_x('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
			time.sleep(2) 
			self.send_txt(self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'),'Badleroyal25*')
			self.click_x('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')


bot=FollowD()

bot.follow('twitter')
'''
send_txt(driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'),'Aboujotaro')
click_x('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
time.sleep(2) 
send_txt(driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'),'Badleroyal25*')
click_x('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
'''