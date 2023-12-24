# The config file of OSC Chatbox, you will need it if you want to provide configuration option to the user
import config;
# Any other module importing...

# The name of the plugin, it must matches with the class name of the plugin
MODULE_NAME = "MyNewPlugin";
# The description of the plugin, the user can see it in the configuration page
MODULE_DESC = "It's my new plugin for osc chatbox slideshow!"

CONFIG_1 = "Value of config 1"
CONFIG_2 = 1234
CONFIG_3 = True

# Example for checking if it's time to refresh data
REFRESH_RATE = 10;

config.addConfig(__name__, "CONFIG_1", "Label for the control in the configuration screen", "str")
config.addConfig(__name__, "CONFIG_2", "Label for the control in the configuration screen", "num")
config.addConfig(__name__, "CONFIG_3", "Label for the control in the configuration screen", "bool")

class MyNewPlugin:
    # Example of checking if it's time to refresh data
    ranCount = 0;

    def init(self):
        # Be called when the application is initializing the plugin. Any except raised will remove this plugin from the update loop.
        # This function should only do stuff that initialize the plugin
        pass;

    def onUpdate(self,scriptUpTime):
        # Be called when the application is trying to request text to display in the OSC chatbox
        # scriptUpTime is to get the time passed since the script started.
        # You can use this value to determine if it's time to refresh data
        if int(scriptUpTime/REFRESH_RATE) >= self.ranCount:
            pass;