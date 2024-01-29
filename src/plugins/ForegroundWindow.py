from ctypes import *;

MODULE_NAME = "ForegroundWindow";
MODULE_DESC = "Show the title of the top window on your desktop"
PLUGIN_ENABLED = False;
class ForegroundWindow:
    def onUpdate(self, scriptUpTime):
        titleText = bytes(1024);
        topWindow = windll.user32.GetForegroundWindow();
        charNumber = windll.user32.GetWindowTextW(topWindow,titleText,1024);
        titleText = titleText.decode("utf-16");
        return "Current Active Window:\v%s" % (titleText[:charNumber])
