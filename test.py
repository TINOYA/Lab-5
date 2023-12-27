from steam import Steam
from decouple import config
import os

key = config(os.environ.get('STEAM_API_KEY'))

steam = Steam(key)

# arguments: steamid
user = steam.users.get_user_friends_list("76561198995017863")
print(user)
