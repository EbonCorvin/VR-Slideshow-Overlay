import config;

config.addConfig(__name__, "MESSAGE", "Any message you want to show", "str")

MODULE_NAME = "MessageBubble";
MODULE_DESC = "Just a simple message bubble, nothing fancy";
MESSAGE = "Example message";
PLUGIN_ENABLED = False;
class MessageBubble:
    def onUpdate(self,scriptUpTime):
        return "💬 %s" % MESSAGE;