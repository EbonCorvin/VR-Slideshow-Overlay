import tkinter as tk
import tkinter.font as tkFont
from updateloop import LoadPlugins;
import functools;
import config;

class App:
    previousSettingFrame = None;
    controls = None;

    def __init__(self, root, commandCallback):
        self.commandCallback = commandCallback;
        root.protocol("WM_DELETE_WINDOW", lambda :(commandCallback("settingwinclose")));

        root.title("Setting Screen")
        root.resizable(width=False, height=False)

        btnFont = tkFont.Font(family='Segoe UI',size=12)
        self.labelFont = tkFont.Font(family='Segoe UI',size=10);

        settingFrameContainer = tk.Frame(root);

        if len(LoadPlugins.plugin_descriptive_text)==0:
            text = "No plugin found in the plugin folder!";
            label = tk.Label(settingFrameContainer, text=text, font=tkFont.Font(family='Segoe UI',size=16))
            label.grid(row=1,column=1,padx=5,pady=5);
            settingFrameContainer.grid(row=0, column=2, padx=5, sticky="N")
            return;
    
        btn=tk.Button(root, text="General Setting")
        btn["bg"] = "#f0f0f0"
        btn["font"] = btnFont
        btn["fg"] = "#000000"
        btn["justify"] = "center"
        btn.grid(row=0,column=0,columnspan=2, padx=5,pady=10);
        btn["command"] = functools.partial(self.buildGeneralSettingUi, root=settingFrameContainer);

        row = 1;
        for plugin in LoadPlugins.plugin_descriptive_text:
            attr = LoadPlugins.plugin_descriptive_text[plugin];
            chk = tk.Checkbutton(root,text=attr[0]);
            chk["justify"] = "left";
            chk["font"] = btnFont;
            enableStatus = tk.IntVar(root, 1 if LoadPlugins.modules[plugin].PLUGIN_ENABLED else 0);
            chk["variable"] = enableStatus;
            chk["command"] = functools.partial(self.togglePlugin, plugin=plugin, value=enableStatus);
            chk.grid(row=row,column=0,sticky="w",padx=5,pady=5);

            btn=tk.Button(root, text="Setting")
            btn["bg"] = "#f0f0f0"
            btn["font"] = btnFont
            btn["fg"] = "#000000"
            btn["justify"] = "center"
            btn.grid(row=row,column=1,padx=5,pady=5);
            btn["command"] = functools.partial(self.buildSettingUi, root=settingFrameContainer, plugin=plugin)
            row+=1;
        
        settingFrameContainer.grid(row=0, rowspan=row, column=2, padx=5, sticky="N")

    def buildSettingUi(self, root, plugin):
        if self.previousSettingFrame is not None:
            self.previousSettingFrame.destroy();
        frame = tk.Frame(root);
        frame.grid(row=0, column=2, padx=5)
        attr = LoadPlugins.plugin_descriptive_text[plugin];
        label = tk.Label(frame, text=attr[0], font=tkFont.Font(family='Segoe UI',size=16))
        label.grid(row=0, column=0, padx=5)
        label["justify"] = "center"
        labelDesc = tk.Label(frame, text=attr[1], font=tkFont.Font(family='Segoe UI',size=12))
        labelDesc.grid(row=1, column=0, padx=5)
        labelDesc["justify"] = "center"
        self.addConfigControls(frame, plugin)
        self.previousSettingFrame = frame;

    def buildGeneralSettingUi(self, root):
        if self.previousSettingFrame is not None:
            self.previousSettingFrame.destroy();
        frame = tk.Frame(root);
        frame.grid(row=0, column=2, padx=5)
        tk.Label(frame, justify="center", text="General Settings", font=tkFont.Font(family='Segoe UI',size=16)).grid(row=0, column=0, padx=5);
        curRow = 1;
        allControls = {};
        for section in config.CONFIG_GENERAL_MODULE:
            allControls[section] = {};
            tk.Label(frame, justify="center", text=section, font=tkFont.Font(family='Segoe UI',size=12)).grid(row=curRow, column=0, padx=0, pady=0)
            curRow+=1;
            configList = config.CONFIG[section];
            for key in configList:
                curRow, var = self.createControl(key, section, configList, frame, curRow);
                allControls[section][key] = var;
        saveBtn=tk.Button(frame, text="Save");
        saveBtn["command"] = functools.partial(self.saveGeneralSetting, controls=allControls);
        saveBtn.grid(row=curRow,pady=10);
        self.previousSettingFrame = frame;
 
    def addConfigControls(self, root, plugin):
        curRow = 3;
        if not plugin in config.CONFIG:
            label = tk.Label(root, text="No configuration available", font=tkFont.Font(family='Segoe UI',size=16));
            label.grid(row=curRow);
            return;
        configList = config.CONFIG[plugin];
        controls = {};
        for key in configList:
            curRow, var = self.createControl(key, plugin, configList, root, curRow);
            controls[key] = var;
        saveBtn=tk.Button(root, text="Save")
        saveBtn["command"] = functools.partial(self.saveSetting, configs=configList, controls=controls, plugin=plugin);
        saveBtn.grid(row=curRow,pady=10);
    
    def createControl(self, key, plugin, configList, root, curRow):
        configdesc, valuetype = configList[key];
        defaultValue = getattr(LoadPlugins.modules.get(plugin, config.CONFIG_GENERAL_MODULE.get(plugin)),key);
        var = None;
        if valuetype!="bool":
            label = tk.Label(root, text=configdesc, font=self.labelFont);
            label.grid(row=curRow);
            curRow+=1;
            var = tk.StringVar(root, defaultValue);
        else:
            var = tk.IntVar(root, value = 1 if defaultValue else 0);
        control = None;
        if valuetype=="str":
            control = tk.Entry(root);
            control["textvariable"] = var;
        elif valuetype=="num":
            control = tk.Spinbox(root, to=9999);
            control["textvariable"] = var;
        elif valuetype=="bool":
            control = tk.Checkbutton(root, text=configdesc, font=self.labelFont, variable=var, onvalue=True, offvalue=False);
        control.grid(row=curRow);
        curRow+=1;
        return curRow, var;

    def saveSetting(self, configs, controls, plugin, module = None):
        module = module if module is not None else LoadPlugins.modules[plugin];
        for key in controls:
            value = controls[key].get()
            if configs[key][1]=="bool":
                value = value==1;
            elif configs[key][1]=="num":
                value = int(value)
            setattr(module, key, value);

    def saveGeneralSetting(self, controls):
        for section in controls:
            self.saveSetting(config.CONFIG[section], controls[section], None, config.CONFIG_GENERAL_MODULE[section]);
    
    def togglePlugin(self, plugin, value):
        LoadPlugins.modules[plugin].PLUGIN_ENABLED = value.get()==1;

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
