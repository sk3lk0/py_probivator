import time
import os
import re
import requests
import cfscrape
clear = lambda: os.system('cls')

clear()
time.sleep(0.5)
##
##сюда
##
time.sleep(0.5)
clear()
mail = " "
xaker_result = " "
def email():
	#while True:
		print("BBEDITE EMAIL")
		global mail
		mail = input()
		#if mail.find("@") == -1:
		#	print ("NE CORRECTNO")
		#else:
		#	print ("PRINYATO")
		#	break

email()
def xakername():
	temp_string = requests.post('http://xaker.name/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global xaker_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		xaker_result = '"xaker.name" = [-]'
	else:
		print ("+")
		xaker_result = '"xaker.name" = [+]'
#xakername() rabotaet

def prologic():
	temp_string = requests.post('https://prologic.su/index.php?app=core&module=global&section=lostpass', data = {'email_addy': mail})
	temp_data = temp_string.text
	global prologic_result
	if temp_data.find("К сожалению нам не удалось найти пользователя с такими данными.") != -1:
		print ("-")
		prologic_result = '"prologic.su" = [-]'
	else:
		print ("+")
		prologic_result = '"prologic.su" = [+]'
		
#prologic() не работает

def xaker26():
	temp_string = requests.post('http://xaker26.info/login.php?action=forget_2', data = {'form_sent': '1','req_email': mail})
	temp_data = temp_string.text
	global xaker26_result
	if temp_data.find("Зарегистрированного пользователя с таким e-mail адресом не существует") != -1:
		print ("-")
		xaker26_result = '"xaker26.info" = [-]'
	else:
		print ("+")
		xaker26_result = '"xaker26.info" = [+]'
		
#xaker26() наверное работает, нету акка чтобы проверить

def xakfor():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://xakfor.net/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	#temp_data = scraper.get(temp_string).content
	global xakfor_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		xakfor_result = '"xakfor.net" = [-]'
	else:
		print ("+")
		xakfor_result = '"xakfor.net" = [+]'
		
#xakfor() rabotaet

#print(mail)