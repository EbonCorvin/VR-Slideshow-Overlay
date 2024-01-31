import psutil;

MODULE_NAME = "PCUsage";
MODULE_DESC = "Show PC Usage"
class PCUsage:

    def onUpdate(self, scriptUpTime):
        psutil.cpu_stats
        return 'CPU Load: %s%%\tRAM: %s%%' % (int(psutil.cpu_percent()),psutil.virtual_memory()[2]);
