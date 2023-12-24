import json;
import os;
from updateloop import LoadPlugins;
# { 
#     module: {
#         key: (description, type)
#     }
# }

CONFIG = {}
CONFIG_FILENAME = "config.json"
def addConfig(module, key, description, valueType):
    if module not in CONFIG:
        CONFIG[module] = {};
    CONFIG[module][key] = (description, valueType);

def saveConfig():
    configToSave = {};
    for key in LoadPlugins.modules:
        configToSave[key] = {};
        if key in CONFIG:
            for configkey in CONFIG[key]:
                configToSave[key][configkey] = getattr(LoadPlugins.modules[key],configkey);
        configToSave[key]["PLUGIN_ENABLED"] = getattr(LoadPlugins.modules[key],"PLUGIN_ENABLED");
    file = open(os.path.join(os.getcwd(),CONFIG_FILENAME), mode="w+", buffering=1024, encoding="utf8");
    file.write(json.dumps(configToSave));
    file.close();

def readConfig():
    try:
        file = open(os.path.join(os.getcwd(),CONFIG_FILENAME), mode="r+", buffering=1024, encoding="utf8");
        setting = file.readline();
        file.close();
        setting = json.loads(setting);
        for plugin in CONFIG:
            if plugin in setting:
                # Only process the config keys that are registered already
                for key in CONFIG[plugin]:
                    if key in setting[plugin]:
                        setattr(LoadPlugins.modules[plugin],key,setting[plugin][key]);
        for plugin in LoadPlugins.modules:
            if hasattr(LoadPlugins.modules[plugin], "PLUGIN_ENABLED"):
                setattr(LoadPlugins.modules[plugin],"PLUGIN_ENABLED",setting[plugin]["PLUGIN_ENABLED"]);
    except Exception as ex:
        print(ex);