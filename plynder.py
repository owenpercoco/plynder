import pynder
import time
import random
import FB
f_id2 = '1452759613'
f_token2='EAAGm0PX4ZCpsBADKRidAj2rFXQ9RZBcRzf39G6ys4LC124A2qIG8n3EXWH17GVlgSjovg5IfuJMuBWrsdcrA0exRpzgFPHOjHwmatIFSZCVYeG5Ss1cP2h2JCZAOixZCnIceu9Whz1DvZCBZB6mYl0VUz2OjkBPM3eIWppe6ZAMpJLm9mrNbBo0Po3wSHeVfYL3wmEmEpLrMgMErjRAEt9VG'
			

def like_everybody(sess):
        girls = session.nearby_users()
        chance_dislike = random.randrange(0, 50)
	for girl in girls:
        	d = random.randrange(0, 50)
                if d == chance_dislike:
			girl.dislike
                else:
			time.sleep(random.randrange(0, 3))
                        print girl.name
                        print girl.photos[0]
                        print girl.instagram_username
			print 'common friends: ' + str(girl.common_connections)
                        girl.like

session = pynder.Session(facebook_id = f_id, facebook_token = f_token)
session.matches() # get users you have already been matched with
print 'you have ' + str(len(session.matches())) +  ' matches'
for babes in session.matches():
        print babes

print session.likes_remaining
if session.likes_remaining > 0:
	like_everybody(session)

print 'finished'
