import json;
import os;
import sys;
from updateloop import LoadPlugins;
# { 
#     module: {
#         key: (description, type)
#     }
# }

CONFIG = {}
CONFIG_FILENAME = "config.json"
CONFIG_GENERAL_MODULE = {};
def addConfig(module, key, description, valueType):
    if module not in CONFIG:
        CONFIG[module] = {};
    CONFIG[module][key] = (description, valueType);

def saveConfig():
    configToSave = {};
    for key in CONFIG:
        configToSave[key] = {};
        for configkey in CONFIG[key]:
            module = LoadPlugins.modules.get(key, CONFIG_GENERAL_MODULE.get(key, None));
            configToSave[key][configkey] = getattr(module,configkey);
    for key in LoadPlugins.modules:
        if not key in configToSave:
            configToSave[key] = {};
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
                    try:
                        module = LoadPlugins.modules.get(plugin, CONFIG_GENERAL_MODULE.get(plugin, None));
                        if key in setting[plugin]:
                            setattr(module,key,setting[plugin][key]);
                    except Exception as ex:
                        print(ex, plugin, key);
        for plugin in LoadPlugins.modules:
            if plugin in setting:
                setattr(LoadPlugins.modules[plugin],"PLUGIN_ENABLED",setting[plugin]["PLUGIN_ENABLED"]);
    except Exception as ex:
        print(ex);

def add_general_setting_path(section, path):
    CONFIG_GENERAL_MODULE[section] = path;

def register_general_setting():
    for key in CONFIG_GENERAL_MODULE:
        path = CONFIG_GENERAL_MODULE[key]
        pathpart = path.split(".");
        cur_module = sys.modules[pathpart[0]];
        for attrName in pathpart[1:]:
            cur_module = getattr(cur_module, attrName);
        CONFIG_GENERAL_MODULE[key] = cur_module;