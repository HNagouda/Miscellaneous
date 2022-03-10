'''
Created on Feb 5, 2021

@author: kripatel9
'''
# ***Directions***
# install python in CMD
# install the following modules
    # pip install selenium
    # pip install webdrivermanager
    # pip install smtplib
# install exe from --> https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/

from selenium import webdriver  
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
# import smtplib                  #for email notifications only

# Initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://students.htps.us/genesis/sis/view?gohome=true')

user = "nagoudah@htps.us" #GENESIS USERNAME/EMAIL
passwd = "Lion76wind"      #GENESIS PASSWORD

browser.find_element_by_id('j_username').send_keys(user)
browser.find_element_by_id('j_password').send_keys(passwd)
browser.find_element_by_class_name('saveButton').click()
 
browser.find_element_by_id('__button1__').click();
 
select = Select(browser.find_element_by_id('attendanceType'))
select.select_by_value('Present')
 
browser.find_element_by_class_name('saveButton').click()
browser.quit()

# ***EMAIL NOTIFICATIONS***
# Note: *sent regardless if it worked or not
#       *Unsecure login must be turned on in google account

# fromAddress = "XXXX@gmail.com"      #EMAIL ADRESS THAT NOFICATION IS SENT FROM
# fromPswd = "abc123#"                #EMAIL PSWD THAT NOFICATION IS SENT FROM
# toAddress = "YYYY@htps.us"          #EMAIL ADRESS YOU WANT TO SEND NOTIFICATION TO
# emailMsg = "Attendance Completed!"  #EMAIL CONTENTS
#   
# conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
# conn.ehlo() # call this to start the connection
# conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
# conn.login(fromAddress, fromPswd)
# conn.sendmail(fromAddress, toAddress, emailMsg.encode('utf8'))
# conn.quit()