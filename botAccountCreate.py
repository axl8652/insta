from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
import Genertor as account

browser= webdriver.Chrome("C:/Project/Instacount/chromedriver.exe")
browser.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(8) #time.sleep count can be changed depending on the Internet speed.
name = account.username()
email = account.generatingEmail()
fullname = account.generatingName()
password = 'aa12345bb12345cc'+name
day =account.generatebirthday()
month =account.generatebirthmonth()
year=account.generatebirthyear()


print ('Name::' +name)
print ('Email::'+ email)
print ('Fullname::' + fullname)
print ('Password::'+ password)
print ('Birth Month::' + month)
print (day)
print ( year)



#Fill the email value
email_field = browser.find_element_by_name('emailOrPhone')
email_field.send_keys(email)

#Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(fullname)

#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)
#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys(password) #You can determine another password here.

#submit = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
submit = browser.find_element_by_xpath('//button[contains(text(),"Sign up")]')
submit.click()
time.sleep(8)

print('Registering....')

#drop_downs  = browser.find_element_by_xpath('//select[@class="h144Z  ""]')
#month_field=(browser.find_element_by_xpath('//*[@title="Month"]'))
#month_field.select_by_visible_text('January')
#month_field = drop_downs[0].click()
#month_field.send_keys(email)
#drop_down_month  = browser.find_element_by_xpath('//select[@title="Month:"]')
print('Selecting month....')
browser.find_element_by_xpath("//select[@title='Month:']/option[text()='"+month+"']").click()
browser.find_element_by_xpath("//select[@title='Day:']/option[text()='"+str(day)+"']").click()
browser.find_element_by_xpath("//select[@title='Year:']/option[text()='"+str(year)+"']").click()

browser.find_element_by_xpath("//button[contains(text(),'Next')]").click()