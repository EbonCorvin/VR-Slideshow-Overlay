import os;
import config;

config.add_general_setting_path("FileOutput", "updateloop.MainLoop.FileOutput")
config.addConfig("FileOutput", "IS_ENABLED", "Enable outputting to a text file?", "bool")
config.addConfig("FileOutput", "OUTPUT_FILENAME", "Output File name", "str")

IS_ENABLED = False;
OUTPUT_FILENAME = "output.txt";

outputfile = None;

def init():
    global outputfile;
    filepath = os.path.join(os.getcwd(),OUTPUT_FILENAME);
    outputfile = open(filepath, mode="w+", buffering=1024, encoding="utf8");

def outputString(text):
    text = "\r\n".join(text);
    outputfile.seek(0);
    outputfile.truncate(0);
    outputfile.write(text.replace("\v", "\r\n"));
    outputfile.flush();