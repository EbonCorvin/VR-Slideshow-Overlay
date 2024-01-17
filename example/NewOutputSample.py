# The config file of OSC Chatbox, you will need it if you want to provide configuration option to the user
import config;

# Register the module of this output location. The second parameter is the path of the module, just follow the folder structure.
config.add_general_setting_path("NewOutput", "output_ports.NewOutput")
# IS_ENABLED is a manatory attribute for the application to determine if the user want to enable it or not
config.addConfig("NewOutput", "IS_ENABLED", "Enable outputting?", "bool")
config.addConfig("NewOutput", "OTHER_CONFIG", "Other configuration", "str")

IS_ENABLED = False;
OTHER_CONFIG = "";

def init():
    # Initialize your output location here
    pass;

def outputString(text):
    # Be called when new output string is available. The parameter "text" is a list. 
    # The first and the last item is the "always top" and "always bottom" plugin output, and the middle one is the output of the current slideshow
    pass;

# The last step to do before the output location can be used is to import the module in MainLoop.py
# Then add it to the "outputs" line in update_loop() (At the first time of the function)
# I may simplify the process by treating them like slideshow plugins in the future