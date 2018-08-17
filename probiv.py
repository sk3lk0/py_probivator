import time
import os
import re
import requests
import cfscrape
import sys

if __name__ == "__main__":
    if len (sys.argv) == 1:
        print ("1argument")
    else:
        if len (sys.argv) < 3:
            print ("Ошибка. Слишком мало параметров.")
            sys.exit (1)

        if len (sys.argv) > 3:
            print ("Ошибка. Слишком много параметров.")
            sys.exit (1)

    param_name = sys.argv[1]#email || nick
    param_value = sys.argv[2]#value
	
def xakername():# login & email
	
	#sys.exit (1)
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('http://xaker.name/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global xaker_result
	if temp_data.find("не найден.") != -1:
		xaker_result = '"xaker.name" = [-]'
	else:
		xaker_result = '"xaker.name" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
xakername()
#print(xaker_result)

def xakfor():
	
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://xakfor.net/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	
	global xakfor_result
	if temp_data.find("не найден.") != -1:
		xakfor_result = '"xakfor.net" = [-]'
	else:
		xakfor_result = '"xakfor.net" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
xakfor()
#print(xakfor_result)

def dublikat():

	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://dublik.at/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	
	global dublikat_result
	if temp_data.find("не найден.") != -1:
		dublikat_result = '"dublik.at" = [-]'
	else:
		dublikat_result = '"dublik.at" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
dublikat() #rabotaet
#print(dublikat_result)

def zblock():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://zblock.me/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global zblock_result
	if temp_data.find("не найден.") != -1:
		zblock_result = '"zblock.me" = [-]'
	else:
		zblock_result = '"zblock.me" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
zblock() #rabotaet
#print(zblock_result)

def wwh():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://wwh-club.net/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global wwh_result
	if temp_data.find("не найден.") != -1:
		wwh_result = '"wwh-club.net" = [-]'
	else:
		wwh_result = '"wwh-club.net" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
wwh() #rabotaet
#print(wwh_result)

def antichat():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://forum.antichat.ru/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global antichat_result
	if temp_data.find("could not be found.") != -1:
		antichat_result = '"forum.antichat.ru" = [-]'
	else:
		antichat_result = '"forum.antichat.ru" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
antichat()
#print(antichat_result)

def blackangels():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://blackangels.team/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global blackangels_result
	if temp_data.find("не найден.") != -1:
		blackangels_result = '"blackangels.team" = [-]'
	else:
		blackangels_result = '"blackangels.team" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
blackangels() #rabotaet
#print(blackangels_result)

def vlmi():
	scraper = cfscrape.create_scraper()
	temp_string = scraper.post('https://vlmi.su/login/login', data = {'login': param_value, 'register': '0', 'password': 'test'})
	temp_data = temp_string.text
	global vlmi_result
	if temp_data.find("не найден.") != -1:
		vlmi_result = '"vlmi.su" = [-]'
	else:
		vlmi_result = '"vlmi.su" = [+]'
	if (param_name == "-email"):
		time.sleep(0)
	elif (param_name == "-nickname"):
		time.sleep(0) #пробить members
	else:
		print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
vlmi()
#print(vlmi_result)
temp = param_value

f = open('C:\\'+temp,'w')
f.write(xaker_result+'\n')
f.write(xakfor_result+'\n')
f.write(dublikat_result+'\n')
f.write(zblock_result+'\n')
f.write(wwh_result+'\n')
f.write(antichat_result+'\n')
f.write(blackangels_result+'\n')
f.close()
