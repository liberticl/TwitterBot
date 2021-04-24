#!/usr/bin/python3

import os
import yaml


PATH = "/home/francisco/python_scripts/Twitter/fco_vergara12/"
DB_PATH = "/home/francisco/python_scripts/Twitter/fco_vergara12/db/"

# Obtiene el listado de hashtags desde el archivo 'hashtags.txt'
def get_ht():
	to_return = []
	hfile = open(PATH + 'hashtags.txt','r')
	for hashtag in hfile:
		to_return.append(hashtag)
	hfile.close()
	return to_return

# Reescribe el listado de hashtags con el contenido de la lista 'hlist'
def hashtag(hlist):
	hfile = open(PATH + 'hashtags.txt','w')
	for hashtag in hlist:
		hfile.write(hashtag + "\n")
	hfile.close()

# Reemplaza el último retweet en el archivo de la cuenta correspondiente
def save_rt(username,status_id):
	if not os.path.isfile(PATH + 'db/' + username):
		userfile = open(PATH + 'db/' + username,'w')
		userfile.write(status_id)
		userfile.close()
	else:
		userfile = open(PATH + 'db/' + username,'w')
		userfile.write(str(status_id))
		userfile.close()

# Obtiene el último retweet realizado de una cuenta específica
def get_last_rt(username):
    if not os.path.isfile(DB_PATH + username):
        return None
    else:
        userfile = open(DB_PATH + username,'r')
        last = userfile.readline()
        userfile.close()
        return last

# Obtiene una lista con los archivos en la carpeta 'db' (usuarios a considerar)
def get_usernames():
    return os.listdir(DB_PATH) 

# "Normaliza" palabras quitando tildes
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Revisa si un texto contiene una comuna del distrito 7
def in_d7(text):
    text = normalize(text).upper()
    d7 = ["Valparaiso","Juan Fernandez","Isla de Pascua","Viña del Mar","Concon","Algarrobo","Cartagena","Casablanca","El Quisco","El Tabo","San Antonio","Santo Domingo"]
    for city in d7:
        if city.upper() in text:
            return True
    return False

# Obtiene un dato específico de la API
def get_credentials():
    yml_file = open(PATH + '.api_data.yml')
    api_data = yaml.load(yml_file, Loader=yaml.FullLoader)
    return api_data