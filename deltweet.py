import tweepy
import os

info = """
$ You Can find consumer_key and consumer_sercret in this like
$++[https://apps.twitter.com/app]
$ put your username and passwoed
$ and login click Create New App
$ in Name put any thing Example [ delete tweet21 ]
$ decription put any thing info 
$ website [https://ww.twiiter.com/yourusername
$ click true [ Yes, I have read and agree to the Twitter Developer Agreement.]
$ and create your ...
Go Down and see manage keys you will see  CONSUMER_KEY && CONSUMER_SECRET!
"""
SP = "\n"
Noothing = " CONSUMER_SECRET is empty"
print info
CONSUMER_KEY = raw_input("put your consumer_secret:")
print SP
if CONSUMER_KEY == "":
    CONSUMER_KEY = raw_input("Your are Not put anything please put your CONSUMER_KEY:")
print SP
if CONSUMER_KEY == "":
	print "Bey Bey script will close try agine"


	os._exit(1)


CONSUMER_SECRET = raw_input("put your consumer_secret:")





def oauth_login(consumer_key, consumer_secret):
    
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    
    verify_code = raw_input("Authenticate at \n %s \n and then enter you verification code here >"  % auth_url) 
    auth.get_access_token(verify_code)
    
    return tweepy.API(auth)

def batch_delete(api):
    print "You are about to Delete all tweets from the account @%s.   \n=" % api.verify_credentials().screen_name
    print "put [yes] and click Enter\n"
    do_delete = raw_input(">")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print "Deleted...:", status.id
            except:
                print "Failed to delete...:", status.id

if __name__ == "__main__":
    api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)
    print "Authenticated as: %s" % api.me().screen_name
    
    batch_delete(api)
