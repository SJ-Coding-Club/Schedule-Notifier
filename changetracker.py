'''
This script will notify me when 2020-2021 schedules are posted
yeah ik this is pretty lame but I'm bored. I use heroku to run it
	
	author: Jack Donofrio
	date: 9:07 PM, July 11, 2020
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
import csv
from twilio.rest import Client

# sign into plusportals

USER = '' 
PASS = ''

TWILIO_SID = ''
AUTH_TOKEN = ''

twilio_client = Client(TWILIO_SID, AUTH_TOKEN)

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get('https://www.plusportals.com/sjhs')

username_element = driver.find_element_by_id('UserName')
password_element = driver.find_element_by_id('Password')

username_element.send_keys(USER)
password_element.send_keys(PASS)

driver.find_element_by_name('btnsumit').click()

time.sleep(6)


def check_grades():
	global driver
	global twilio_client
	table = driver.find_element_by_xpath('//*[@id="GridProgress"]/div[2]/table/tbody')
	if table.size['height'] > 0.0:
		# notify me
		message = twilio_client.messages.create(body='schedules posted.', from_='redacted',to='redacted')
		# this means an item has been added to the table
		# print('test')
	print('grades table')


def check_messages():
	global driver
	global twilio_client
	driver.find_element_by_xpath('//*[@id="top"]/nav/div/div/div/div/div/ul/li[5]/a').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="tabstripCommunication"]/ul/li[2]/span').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="btnNewMessage"]').click()
	time.sleep(1)

	#table containing list of teachers
	table = driver.find_element_by_xpath('//*[@id="gridMsgRecipient"]/div[2]/table/tbody')
	if len(table.text) > 50:
		message = twilio_clientclient.messages.create(body='schedules posted.', from_='+redacted',to='+redacted')
		# notify me
	print('messages table')
	#delet after test


check_grades()
check_messages()
