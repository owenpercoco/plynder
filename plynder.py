import pynder
f_id = '1452759613'

f_token='EAAGm0PX4ZCpsBADKRidAj2rFXQ9RZBcRzf39G6ys4LC124A2qIG8n3EXWH17GVlgSjovg5IfuJMuBWrsdcrA0exRpzgFPHOjHwmatIFSZCVYeG5Ss1cP2h2JCZAOixZCnIceu9Whz1DvZCBZB6mYl0VUz2OjkBPM3eIWppe6ZAMpJLm9mrNbBo0Po3wSHeVfYL3wmEmEpLrMgMErjRAEt9VG'

session = pynder.Session(facebook_id = f_id, facebook_token = f_token)
session.matches() # get users you have already been matched with
def like_everybody(sess):
	girls = session.nearby_users()
	while sess.likes_remain > 0:
		for girl in girls:
			print girl.name
			print girl.photos[0]
			print girl.instagram_username
			girl.like



for babes in session.matches():
	print babes

print session.likes_remaining
if session.likes_remaining > 0:
	like_everybody()

print 'finished'
