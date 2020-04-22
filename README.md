# Instacart Delivery Slot Finder

This program is created to find next available instacart delivery slot. This is a utility program to help people find instacart slots during Covid 19 time. 

findInstacartDeliverySlot.py is the core python file. It takes instacart login id/password as parameters and will login to instacart. Once logged in, the program periodically checks for available delivery times in checkout page (period is configurable - default is every 20 seconds). If a slot opens up, the program will alert users on their mobile phone through sms message. Mobile numbers of users can be configured (this program will currently send alerts to up to 2 mobile phones)

This is version 1.2. Major bug fixes added and ability to find slot from checkout page is added. This program is tested for 5 days, more changes might be required

## Prerequisites

Before running findInstacartDeliverySlot.py python file, please ensure the following prerequisites are completed

1. install Python 3 (you can download latest version of Python)
2. Add Python to your PATH variable if it is not already added (by default, python is added to PATH variable during installation)
3. Install selenium and pyderman packages (use pip commands below in terminal/command prompt)
    a. pip install -U selenium
    b. pip install pyderman
4. Upgrade chrome to version 81. This program will run on Chrome version 81 (latest version as of now)
5. PLEASE MAKE SURE THAT INSTACART HAS YOUR LIST OF GROCERIES ADDED TO CART BEFORE RUNNING THE PROGRAM. This program is meant to provide alerts when delivery slots open up. Due to the extremely busy nature of instacart delivery service at this time, slots will close out quickly. This program is made for quick checkout and not to add groceries. Please ensure that your groceries are added to cart already before running this program.
6. Please keep your PC/laptop in "sleep = NEVER" mode. Sometimes it takes days to find a slot!!

## Executing findInstacartDeliverySlot
1. clone this git program onto your local machine
2. open findInstacartDeliverySlot.py file in any editor and update the following parameters
    a. instaLogin = #YOUR INSTACART LOGIN
    b. instaPas = #YOUR INSTACART PASSWORD
    c. instacartStore = #INSTACART STORE THAT YOU WANT TO FIND SLOT. Default this parameter to '' if you don't want to specify a particular store. Default behavior will identify store from checkout page. Currently only 'wegmans', 'costco', 'aldi', 'acme', 'cvs', 'shoprite', 'target' and 'petco' are supported
    d. sms_gateway = # YOUR MOBILE SMS GATEWAY FOR THE PHONE YOU WANT TO REE (You can find your carrier's sms gateway address on web. For eg., if your carrier is AT&T and your number is 123456789, sms gateway will be '123456789@txt.att.net'
    e. sms_gateway2 = #Optional second mobile phone. leave it as None if you don't want to add 2nd mobile
2. Navigate to local folder in terminal or command prompt and run "python findInstacartDeliverySlot.py".

When running for the first time, the code will create a subfolder (lib) inside the local folder. latest version of chrome webdriver will be installed in the lib folder.
