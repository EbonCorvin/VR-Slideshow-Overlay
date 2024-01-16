import time
from output_ports import VRCOsc, FileOutput
import config;
from updateloop import LoadPlugins

config.add_general_setting_path("Slideshow", "updateloop.MainLoop")
config.addConfig("Slideshow", "SLIDESHOW_INTERVAL", "Interval between each slideshow", "num")
config.addConfig("Slideshow", "ONUPDATE_RETRY_COUNT", "Number of attempt before removing a failed plugin", "num")
config.addConfig("Slideshow", "SLIDESHOW_ALWAYS_ONTOP", "Slideshow that is always on the top of every update", "str")
config.addConfig("Slideshow", "SLIDESHOW_ALWAYS_ATBOTTOM", "Slideshow that is always at the bottom of every update", "str")

SLIDESHOW_INTERVAL = 7;
ONUPDATE_RETRY_COUNT = 3;
SLIDESHOW_ALWAYS_ONTOP = "";
SLIDESHOW_ALWAYS_ATBOTTOM = "";

def update_loop():
    disabledPlugin = [x for x in LoadPlugins.modules.keys() if not LoadPlugins.modules[x].PLUGIN_ENABLED];
    LoadPlugins.remove_unusable_plugin(disabledPlugin);
    LoadPlugins.init_plugins();
    plugins = LoadPlugins.plugins;
    plugins_error_count = {};

    if len(plugins)==0:
        print("No valid plugin found, the script can't run");
        return;

    outputs = [x for x in [VRCOsc, FileOutput] if getattr(x, "IS_ENABLED")];
    for output in outputs:
        output.init();
        
    scriptUpTime = 0;
    scriptStartTime = time.time();
    while True:
        for module in plugins:
            try:
                strText = plugins[module].onUpdate(scriptUpTime);
                print(strText);
                for output in outputs:
                    output.outputString([strText]);
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