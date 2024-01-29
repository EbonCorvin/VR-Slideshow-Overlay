import datetime;
import config;

MODULE_NAME = "LocalTime";
MODULE_DESC = "Show your local time"

TWENTYFOUR_FORMAT = True;
CAPTION = "Local time - ";
config.addConfig(__name__, "TWENTYFOUR_FORMAT", "Use 24-hour format (military time) format?", "bool")
config.addConfig(__name__, "CAPTION", "Text to be displayed before the time", "str")

class LocalTime:
    def init(self):
        if TWENTYFOUR_FORMAT:
            self.timeFormat = "%H:%M";
        else:
            self.timeFormat = "%I:%M %p";

    def onUpdate(self, scriptUpTime):
        return "%s%s" % (CAPTION, datetime.datetime.now().strftime(self.timeFormat));