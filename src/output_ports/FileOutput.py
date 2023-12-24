import os;

OUTPUT_FILENAME = "output.txt";

outputfile = None;

def init():
    global outputfile;
    filepath = os.path.join(os.getcwd(),OUTPUT_FILENAME);
    outputfile = open(filepath, mode="w+", buffering=1024, encoding="utf8");

def outputString(text):
    outputfile.seek(0);
    outputfile.truncate(0);
    outputfile.write(text.replace("\v", "\r\n"));
    outputfile.flush();