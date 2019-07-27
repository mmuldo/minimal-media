from InstagramAPI import InstagramAPI
from operator import itemgetter

def getFeed(username, password):
    feed = []

    api = InstagramAPI(username, password)
    api.login()

    api.getSelfUsersFollowing()
    for user in api.LastJson["users"]:
        api.getUserFeed(user["pk"])
        feed += api.LastJson["items"]

    feed = sorted(feed, key=itemgetter('taken_at'), reverse=True)
    return feed

def getLinks(feed):
    return ["https://instagram.com/p/" + post["code"] for post in feed]
