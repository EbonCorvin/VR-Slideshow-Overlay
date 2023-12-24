import requests;
import time;
import config;

# I don't wanna do the login thing, it could lead to a lot of security problem and trust issue
# So yeah, just grab the auth cookie from VRChat's homepage please
AUTH_COOKIE = "auth=GRAB_YOUR_OWN_COOKIE!";
VRCHAT_GET_FRIEND_URL = "https://api.vrchat.cloud/api/1/auth/user/friends?offline=false";
VRCHAT_GET_NOTIF_URL = "https://api.vrchat.cloud/api/1/auth/user/notifications?type=all";
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0. 4389.82 Safari/537.36";
OUTPUT_STRING = "Online Friends: %s\vFriends in Private: %s"
REFRESH_RATE = 60;

MODULE_NAME = "OnlineFriends";
MODULE_DESC = "Show the number of your online friends, and tell you why 'orange' is killing VRChat"

config.addConfig(__name__, "AUTH_COOKIE", "Your VRChat auth cookie. Grab it from VRChat's homepage", "str")
config.addConfig(__name__, "REFRESH_RATE", "Refresh interval in second. Don't update your friend list too frequently!", "num")

PLUGIN_ENABLED = False;
class OnlineFriends:
    cachedCount = None;
    ranCount = 0;

    def init(self):
        notifChk = requests.get(VRCHAT_GET_NOTIF_URL, headers={
            "Cookie": AUTH_COOKIE,
            "User-Agent": USER_AGENT
        });
        notifChk = notifChk.json();
        if "error" in notifChk:
            raise Exception("The auth cookie is not correct, please grab a new one from VRChat website!");
    
    def refreshFriendCount(self):
        # print("Refresh");
        friendListResult = requests.get(VRCHAT_GET_FRIEND_URL, headers={
            "Cookie": AUTH_COOKIE,
            "User-Agent": USER_AGENT
        });
        friendListResult = friendListResult.json();
        friendListResult = [(x["displayName"],x["status"],x["location"]) for x in friendListResult if x["location"]!="offline"];
        # print(friendListResult);
        totalOnline = len(friendListResult);
        inPrivateWorld = len([x for x in friendListResult if x[2]=="private"]); 
        # print(inPrivateWorld);
        self.cachedCount = (totalOnline, inPrivateWorld);
        self.lastRun = time.time();

    def onUpdate(self,scriptUpTime):
        if self.cachedCount is None or int(scriptUpTime/REFRESH_RATE) >= self.ranCount:
            self.refreshFriendCount();
            self.ranCount+=1;
        return OUTPUT_STRING % self.cachedCount;