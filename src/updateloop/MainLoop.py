import time
from output_ports import VRCOsc
import config;
from updateloop import LoadPlugins

config.addConfig("General", "SLIDESHOW_INTERVAL", "Interval between each slideshow", "num")
config.addConfig("General", "ONUPDATE_RETRY_COUNT", "Number of attempt before removing a failed plugin", "num")

SLIDESHOW_INTERVAL = 7;
ONUPDATE_RETRY_COUNT = 3;

def update_loop():
    VRCOsc.init();
    disabledPlugin = [x for x in LoadPlugins.modules.keys() if not LoadPlugins.modules[x].PLUGIN_ENABLED];
    LoadPlugins.remove_unusable_plugin(disabledPlugin);
    LoadPlugins.init_plugins();
    plugins = LoadPlugins.plugins;
    plugins_error_count = {};

    if len(plugins)==0:
        print("No valid plugin found, the script can't run");
        return;
    scriptUpTime = 0;
    scriptStartTime = time.time();
    while True:
        for module in plugins:
            try:
                strText = plugins[module].onUpdate(scriptUpTime);
                print(strText);
                VRCOsc.outputString([strText]);
                time.sleep(SLIDESHOW_INTERVAL);
            except Exception as ex:
                print("Cannot get update from plugin",module);
                print(ex);
                plugins_error_count[module] = 0 if module not in plugins_error_count else plugins_error_count[module] + 1;
                if(plugins_error_count[module]==ONUPDATE_RETRY_COUNT):
                    print("Cannot get update for",ONUPDATE_RETRY_COUNT," times already, removing from update loop");
        deletingPlugins = [x for x in plugins_error_count if plugins_error_count[x]==ONUPDATE_RETRY_COUNT]
        if len(deletingPlugins) > 0:
            LoadPlugins.remove_unusable_plugin(deletingPlugins);
            for plugin in deletingPlugins:
                del plugins_error_count[plugin];
        scriptUpTime = time.time() - scriptStartTime;