#!/usr/bin/python3

import log,sys
import tools
import twitter
import pytz
from time import sleep
from datetime import datetime

log.init()

api_data = tools.get_credentials()
api = twitter.Api(consumer_key = api_data['consumer_key'],
                      consumer_secret = api_data['consumer_secret'],
                      access_token_key = api_data['access_token_key'],
                      access_token_secret = api_data['access_token_secret'],)

# Listado de usuarios a retweetear!
to_retweet = tools.get_usernames()

for friend in to_retweet:

	# BLOQUE OBTENER ULTIMO TWEET REVISADO DE user DE LO CONTRARIO 
	last_retweeted = tools.get_last_rt(friend)
	last = api.GetUserTimeline(screen_name = friend, since_id = last_retweeted, include_rts = False, trim_user = True, exclude_replies = True)
	last.reverse()

	# Revisión de cada tweet del usuario
	for tweet in last:

		# Like y registro de acción
		if(tweet.favorited == False):
			if(friend == 'sitiodelsuceso'):
				if(tools.in_d7(tweet.text)):
					api.CreateFavorite(status_id = tweet.id)
					log.favorite(friend,tweet.id)
				else:
					continue
			else:
				api.CreateFavorite(status_id = tweet.id)
				log.favorite(friend,tweet.id)
			sleep(1)

		# Retweet y registro de acción
		if(tweet.retweeted == False):
			if(friend == 'sitiodelsuceso'):
				if(tools.in_d7(tweet.text)):
					api.PostRetweet(status_id = tweet.id)
					log.retweet(friend,tweet.id)
				else:
					continue
			else:
				api.PostRetweet(status_id = tweet.id)
				log.retweet(friend,tweet.id)
			sleep(3)

		tools.save_rt(friend,tweet.id)

		
		# Sigue a los usuarios mencionados y registro de acción (siempre y cuando no sea yo mismo)
		if(len(tweet.user_mentions) > 0):
			for mentioned in tweet.user_mentions:
				relation = api.LookupFriendship(user_id = mentioned.id)
				if(relation[0].following == False and mentioned.screen_name != 'fco_vergara12'):
					api.CreateFriendship(user_id = mentioned.id)
					log.follow(mentioned.name,mentioned.screen_name)
					sleep(5)

tz = pytz.timezone('America/Santiago')
time = datetime.now(tz).strftime("%H:%M:%S") 
print("Ejecutado por última vez a las " + time)