from steam import Steam


key = '69C2F23F1269D7B7E449A7FE4D27812B'
steam = Steam(key)


IDD=input('Type your steam  ID,If you have no steam id you can use mine: 76561198970705205 : ')
request=int(input('Type any number from 1 to 5: '))

if request == 1 :
    user = steam.users.get_owned_games(IDD)
    print(user)
    
if request == 2 :
    id= steam.users.get_steamid (IDD)
    print (id)

if request == 3 :
    info= steam.users.get_account_public_info (IDD)
    print (info)
if request == 4 :
    friends= steam.users.get_user_friends_list(IDD)
    print (friends)
if request == 5 :
    lvl= steam.users.get_user_steam_level (IDD)
    print (lvl)
    
    
