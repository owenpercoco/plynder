import pynder
import time
import random
from FB import *
			

def like_everybody(sess):
        girls = session.nearby_users()
        chance_dislike = random.randrange(0, 50)
	for girl in girls:
        	d = random.randrange(0, 50)
                if d == chance_dislike:
			girl.dislike
                else:
			time.sleep(random.randrange(0, 1))
                        print girl.name
                        print girl.photos[0]
                        print girl.instagram_username
			girl.like

session = pynder.Session(facebook_id = f_id, facebook_token = f_token)
session.matches() # get users you have already been matched with
print 'you have ' + str(len([i for i in session.matches()])) +  ' matches'
for babes in session.matches():
        print babes

print session.likes_remaining
if session.likes_remaining > 0:
	like_everybody(session)

print 'finished'
