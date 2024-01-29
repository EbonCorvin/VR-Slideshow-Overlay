from plugins.lib import GPUtil

MODULE_NAME = "GetGPUUsage";
MODULE_DESC = "Show your nvidia GPU Usage"
class GPUUsage:

    def __init__(self) -> None:
        self.myGpu = None;

    def onUpdate(self, scriptUpTime):
        myGpu = self.myGpu;
        GPUs = GPUtil.getGPUs()
        if len(GPUs) > 0:
            myGpu = GPUs[0];
        if myGpu is not None:
            memoryUsagePercent = round(myGpu.memoryUsed / myGpu.memoryTotal * 100)
            gpuNumber = (round(myGpu.load * 100), memoryUsagePercent , round(myGpu.temperature), round(myGpu.power_draw));
            return 'GPU Load: %s%%\tVRAM: %s%%\vTemp: %s°C\tPower: %sW' % gpuNumber
        else:
            raise Exception("Error getting GPUs");
