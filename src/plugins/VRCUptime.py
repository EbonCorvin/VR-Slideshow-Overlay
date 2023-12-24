import psutil;
import datetime;

MODULE_NAME = "GetVRCUptime";
MODULE_DESC = "Show VRChat Uptime";
class VRCUptime:

    def __init__(self) -> None:
        pass;

    def onUpdate(self, scriptUpTime):
        processes = [p for p in psutil.process_iter(['name', 'username']) if p.info['name'] == "VRChat.exe"];
        if len(processes)>0:
            process = processes[0];
            startTimeTimtstamp = process.create_time();
            startTimeDt = datetime.datetime.fromtimestamp(startTimeTimtstamp)
            timespan = datetime.datetime.now() - startTimeDt;
            return 'VRChat uptime: %s hrs.' % round(timespan.total_seconds() / 60 / 60, 2);
        else:
            return "VRChat is not running";
