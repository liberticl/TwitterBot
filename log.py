#!/usr/bin/python3

import os
import pytz
from datetime import datetime

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
tz = pytz.timezone('America/Santiago')
year = datetime.now(tz).strftime("%Y") 
month = datetime.now(tz).strftime("%B")
log = month + '/' + datetime.now(tz).strftime("%d")

def init():
	# Revisa directorio log y lo crea si es necesario
	if not os.path.isdir(PATH + 'log/'):
		os.mkdir(PATH + 'log')
	
	# Revisa directorio anual y lo crea si es necesario
	if not os.path.isdir(PATH + 'log/' + year + '/'):
		os.mkdir(PATH + 'log/' + year)

	# Revisa directorio mensual y lo crea si es necesario
	if not os.path.isdir(PATH + 'log/' + year + '/' + month + '/'):
		os.mkdir(PATH + 'log/' + year + '/' + month)

	# Revisa archivo y lo crea si es necesario
	if not os.path.isfile(PATH + 'log/' + year + '/' + log + '.log'):
		startlog = datetime.now(tz).strftime("%d/%m/%Y")
		logfile = open(PATH + 'log/' + year + '/' + log + '.log','w')
		logfile.write("Inicia registro de actividades en Twitter: " + startlog + "\n")
		logfile.close()

def favorite(user,tweet_id):
	now = datetime.now(tz)
	logfile = open(PATH + 'log/' + year + '/' + log + '.log','a')
	logfile.write("[LIKE    - " + now.strftime("%H:%M:%S") + "] Se dio like al post con ID:" + str(tweet_id) + " de " + user + "\n")
	logfile.close()
		
def retweet(user,tweet_id):
	now = datetime.now(tz)
	logfile = open(PATH + 'log/' + year + '/' + log + '.log','a')
	logfile.write("[RETWEET - " + now.strftime("%H:%M:%S") + "] Se hizo retweet al post con ID:" + str(tweet_id) + " de " + user + "\n")
	logfile.close()

def follow(username,screen_name):
	now = datetime.now(tz)
	logfile = open(PATH + 'log/' + year + '/' + log + '.log','a')
	logfile.write("[FOLLOW  - " + now.strftime("%H:%M:%S") + "] Ahora se sigue a " + username + " (@" + screen_name + ")\n")
	logfile.close()

def get_ht():
	to_return = []
	hfile = open(PATH + 'hashtags.txt','r')
	for hashtag in hfile:
		to_return.append(hashtag)
	hfile.close()
	return to_return

def hashtag(hlist):
	hfile = open(PATH + 'hashtags.txt','w')
	for hashtag in hlist:
		hfile.write(hashtag + "\n")
	hfile.close()

def save_rt(username,status_id):
	if not os.path.isfile(PATH + 'db/' + username):
		userfile = open(PATH + 'db/' + username,'w')
		userfile.write(status_id)
		userfile.close()
	else:
		userfile = open(PATH + 'db/' + username,'w')
		userfile.write(str(status_id))
		userfile.close()

def get_last_rt(username):
	if not os.path.isfile(PATH + 'db/' + username):
		return None
	else:
		userfile = open(PATH + 'db/' + username,'r')
		last = userfile.readline()
		userfile.close()
		return last
