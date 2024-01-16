import importlib.util
import os,sys;

modules = {};
plugins = {};
plugins_error_count = {};
plugin_descriptive_text = {};

def read_plugins(plugin_dir):
    sys.path.append(os.path.join(plugin_dir, "lib"));
    for path, subfolders, files in os.walk(plugin_dir):
        for file in files:
            if file[-3:]!=".py":
                continue;
            moduleName = file[:-3];
            try:
                spec = importlib.util.spec_from_file_location(moduleName, os.path.join(plugin_dir,file));
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module);
                if hasattr(module, "MODULE_NAME"):
                    obj = getattr(module,moduleName)();
                    plugins[moduleName] = obj;
                    modules[moduleName] = module;
                    plugin_descriptive_text[moduleName] = (module.MODULE_NAME, module.MODULE_DESC);
                    if not hasattr(module, "PLUGIN_ENABLED"):
                        # Enable plugin by default except these which has "PLUGIN_ENABLED" set already
                        module.PLUGIN_ENABLED = True;
            except Exception as e:
                print("Error loading this plugin file:",file)
                print(e);
        break;
    print("Loaded plugins: ",[x for x in plugins])

def init_plugins():
    pluginFailed = [];
    for plugin in plugins:
        obj = plugins[plugin]
        if hasattr(obj, "init"):
            try:
                obj.init();
            except Exception as ex:
                print("Unable to initialize plugin",plugin);
                print(ex);
                pluginFailed.append(plugin);
    remove_unusable_plugin(pluginFailed);

def remove_unusable_plugin(list):
    for plugin in list:
        del plugins[plugin];    
