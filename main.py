import tweepy
#this project was mainly to test calling an API 
# Authenticate to Twitter
auth = tweepy.OAuthHandler("SHvhBU7B0meKLTsR4IcLeBVhq", "Y1ddnvAlhxJ1GsPkjdL0MhYATfnpU9FHE9rlhbCgJgg8iPzMDm")
auth.set_access_token("1155451352-ypbhuYDq3tTNGUze2L1U268P0r2yyDyYXRWSYJL", "kP4zdXSSsfTBp1rZ84GIChMEi8iWYTnOSkx2fpiH99z99")

# Create API Object
api = tweepy.API(auth)

# check to authenticate the keys
# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

#create a tweet
#api.update_status("Hello World")
#test

