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
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('http://xaker.name/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
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
	
	global xakfor_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		xakfor_result = '"xakfor.net" = [-]'
	else:
		print ("+")
		xakfor_result = '"xakfor.net" = [+]'
		
#xakfor() rabotaet

def dublikat():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://dublikat.info/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	
	global dublikat_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		dublikat_result = '"dublikat.net" = [-]'
	else:
		print ("+")
		dublikat_result = '"dublikat.net" = [+]'
		
#dublikat() rabotaet

def zblock():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://zblock.me/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global zblock_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		zblock_result = '"zblock.me" = [-]'
	else:
		print ("+")
		zblock_result = '"zblock.me" = [+]'
		
#zblock() rabotaet

def bhf():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://bhf.io/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global bhf_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		bhf_result = '"bhf.io" = [-]'
	else:
		print ("+")
		bhf_result = '"bhf.io" = [+]'
		
#bhf() #rabotaet

def wwh():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://wwh-club.net/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global wwh_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		wwh_result = '"wwh-club.net" = [-]'
	else:
		print ("+")
		wwh_result = '"wwh-club.net" = [+]'
		
#wwh() #rabotaet

def youhack():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://youhack.ru/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global youhack_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		youhack_result = '"youhack.ru" = [-]'
	else:
		print ("+")
		youhack_result = '"youhack.ru" = [+]'
		
#youhack() #dodelat, captcha

def lolzteam():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://lolzteam.net/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global lolzteam_result
	if temp_data.find("не найден.") != -1:
		print ("-")
		lolzteam_result = '"lolzteam.net" = [-]'
	else:
		print ("+")
		lolzteam_result = '"lolzteam.net" = [+]'
		
#lolzteam() #dodelat, captcha

def antichat():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://forum.antichat.ru/login/login', data = {'login': mail, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global antichat_result
	if temp_data.find("could not be found.") != -1:
		print ("-")
		antichat_result = '"forum.antichat.ru" = [-]'
	else:
		print ("+")
		antichat_result = '"forum.antichat.ru" = [+]'
		
#antichat() #rabotaet

def exploit():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://forum.exploit.in/index.php?act=Login&CODE=01', data = {'UserName': mail,'PassWord': 'test'})
	temp_data = temp_string.text
	global exploit_result
	if temp_data.find("Невозможно найти пользователя") != -1:
		print ("-")
		exploit_result = '"exploit.in" = [-]'
	else:
		print ("+")
		exploit_result = '"exploit.in" = [+]'
		
exploit() #rabotaet


#print(mail)
