import instaloader
from instaloader.structures import Profile
from instalooter.looters import *

L=instaloader.Instaloader()

L.login('zeldon.zoom','Zeldon@201203')

profile=instaloader.Profile.from_username(L.context,'zeldon.zoom')
followees=profile.get_followees()

users=[]
for i in followees:
    Usr=ProfileLooter('%s'% i.username, videos_only=True, template='{username}-{id}')
    Usr.download('%s'%i.username, media_count=6)
    print()
    print('--------Media from %s downloaded!!--------' %i.username)
    print()
    users+=[i.username]



'''
for user in followees:
    Usr=ProfileLooter('%s' % user, videos_only=True, template='{username}-{id}')
    Usr.download('ScrapedVids', media_count=10)
    '''