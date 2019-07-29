from InstagramAPI import InstagramAPI
from operator import itemgetter
import requests

def getFeed(username, password):
    feed = []

    api = InstagramAPI(username, password)
    api.login()

    api.getSelfUsersFollowing()
    for user in api.LastJson["users"]:
        feed += api.getTotalUserFeed(user["pk"])

    feed = sorted(feed, key=itemgetter('taken_at'), reverse=True)
    return feed

# def getPicLinks(feed):
#     return [BeautifulSoup(urlopen('https://www.instagram.com/p/' + post["code"]).read(), 'html.parser').find("meta", property="og:image")["content"] for post in feed]
