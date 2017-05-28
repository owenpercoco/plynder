import pynder
import time
import random
from FB import *
			

def like_everybody(sess):
        girls = session.nearby_users()
        chance_dislike = random.randrange(0, 12)
	for girl in girls:
        	d = random.randrange(0, 12)
                if d == chance_dislike:
			girl.dislike
                else:
			time.sleep(random.randrange(0, 2))
                        print girl.name
                        print girl.photos[0]
                        print girl.instagram_username
			girl.like

session = pynder.Session(facebook_id = f_id, facebook_token = f_token)
session.matches() # get users you have already been matched with
count = 0
babes = ""
for i in session.matches():
	count += 1
	babes = babes + str(i) + " \n"
print 'you have ' + str(count) +  ' matches'
print babes

print session.likes_remaining
if session.likes_remaining > 0:
	like_everybody(session)

print 'finished'
