import pyderman as dr
path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False, version=None, filename=None, return_info=False)
print('Installed chromedriver to path: %s' % path)

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

driver = webdriver.Chrome("./lib/chromedriver_81.0.4044.69.exe") #look in lib folder and use the exact name. Also ensure that right version of chrome browser is present
driver.get("http://www.instacart.com")

#instacart login details. PROVIDE YOUR INSTACART LOGIN DETAILS
instaLogin = 'venu.viyyapu@gmail.com' 
instaPas = '6winter7'

#which store do you want to check for delivery slot.
instacartStore = 'wegmans'

#number of secconds to refresh slot availability page
refreshSeconds = 20

#EMAIL, Password and Mobile SMS details
email = 'venugroceriesslotalert@gmail.com'
pas = 'LetsRock!'
smtp = 'smtp.gmail.com'
port = 587

#mobile details for sms. PROVIDE YOUR MOBILE DETAILS
sms_gateway = '4807172447@txt.att.net'
#Optional second mobile to send alert
sms_gateway2 = '4803291120@txt.att.net'

#Explicit Wait
wait = WebDriverWait(driver, 30)


#utility function for defining store delivery url
def store(storeName):
        switcher={
                'wegmans':'https://www.instacart.com/store/wegmans/info?tab=delivery',
                'costco':'https://www.instacart.com/store/costco/info?tab=delivery',
                'aldi':'https://www.instacart.com/store/aldi/info?tab=delivery',
                'acme':'https://www.instacart.com/store/acme/info?tab=delivery',
                'cvs':'https://www.instacart.com/store/cvs/info?tab=delivery',
                'shoprite':'https://www.instacart.com/store/shoprite/info?tab=delivery',
                'target':'https://www.instacart.com/store/target/info?tab=delivery',
                'petco':'https://www.instacart.com/store/petco/info?tab=delivery'
        }
        return switcher.get(storeName,"Invalid day of week")

deliverySlotUrl = store(instacartStore)

#MAIN CODE
try:
    # Wait until Login button is present, or maximum maximum wait time is passed
    condition = EC.visibility_of_element_located((By.XPATH,'//button[text()="Log in"]'))
    wait.until(condition)

    #first click on login button
    elem = driver.find_element_by_xpath('//button[text()="Log in"]')
    elem.click()

    #fill login details
    condition = EC.visibility_of_element_located((By.ID,'nextgen-authenticate.all.log_in_email'))
    wait.until(condition)

    elem1 = driver.find_element_by_id('nextgen-authenticate.all.log_in_email')
    elem1.send_keys(instaLogin)
    elem2 = driver.find_element_by_xpath('//input[@id="nextgen-authenticate.all.log_in_password"]')
    elem2.send_keys(instaPas)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    #After succeffully logged in (check for cart button), keep checking slot availability page every 20 secs until we have slot available
    condition = EC.visibility_of_element_located((By.XPATH,'//button[text()="Cart"]'))
    wait.until(condition)

    #REDUNDANT CODE - TO BE CLEANED UP (Efficient way is to check for delivery slot url)
    #Open Cart
    #elem = driver.find_element_by_xpath('//button[text()="Cart"]')
    #elem.click()

    #go to checkout page
    #condition = EC.visibility_of_element_located((By.XPATH,'//a[@href="checkout_v3"]'))
    #wait.until(condition)
    
    #elem2 = driver.find_element_by_xpath('//a[@href="checkout_v3"]')
    #driver.implicitly_wait(5)
    #elem2.click()

    #go to slot availability check url
    driver.get(deliverySlotUrl)
    time.sleep(10)
    count = 0
    url = driver.current_url
    while (True):
        try:
            count = count + 1
            print(str(count) + '. url:' + url + ' ... current_url:' + driver.current_url)
            elem2 = driver.find_elements_by_xpath('//div[text()="No delivery times available"] | //div[text() = "No service options found"]')
            if(url == driver.current_url) :
                driver.refresh()
            
            url = driver.current_url
            time.sleep(refreshSeconds)

        except (NoSuchElementException) as py_while_ex :
            print(py_while_ex)
            break

     
    #Send sms to mobile
    server = smtplib.SMTP(smtp,port)
    server.starttls()
    server.login(email,pas)
    print('logged into smtp server')

    #send alert
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    body = 'You have a delivery slot open for login: ' + instaLogin + ' for store ' + instacartStore
    
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)

    if (sms_gateway2 is not None) :
        server.sendmail(email,sms_gateway2,sms)

    print('sent mail')

except (TimeoutException) as py_ex:
    print (py_ex)
    print (py_ex.args)
finally:
    driver.quit()
    server.quit()




