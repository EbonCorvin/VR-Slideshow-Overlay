import GPUtil

MODULE_NAME = "GetGPUUsage";
MODULE_DESC = "Show GPU Usage"
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
            gpuNumber = (round(myGpu.load * 100), memoryUsagePercent , round(myGpu.temperature));
            return 'GPU Load: %s%%\tVRAM: %s%%\vTemp: %s°C' % gpuNumber
        else:
            raise Exception("Error getting GPUs");
