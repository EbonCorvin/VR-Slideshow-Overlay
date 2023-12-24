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

        row = 0;
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

    def addConfigControls(self, root, plugin):
        curRow = 3;
        if not plugin in config.CONFIG:
            label = tk.Label(root, text="No configuration available", font=tkFont.Font(family='Segoe UI',size=16));
            label.grid(row=curRow);
            return;
        configList = config.CONFIG[plugin];
        self.controls = {};
        for key in configList:
            curRow = self.createControl(key, plugin, configList, root, curRow);
        saveBtn=tk.Button(root, text="Save")
        saveBtn["command"] = functools.partial(self.saveSetting, configs=configList, plugin=plugin);
        saveBtn.grid(row=curRow,pady=10);
    
    def createControl(self, key, plugin, configList, root, curRow):
        configdesc, valuetype = configList[key];
        defaultValue = getattr(LoadPlugins.modules[plugin],key);
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
        self.controls[key] = var;
        control.grid(row=curRow);
        curRow+=1;
        return curRow;


    def saveSetting(self, configs, plugin):
        for key in self.controls:
            value = self.controls[key].get()
            print(key, value)
            if configs[key][1]=="bool":
                value = value==1;
            elif configs[key][1]=="num":
                value = int(value)
            setattr(LoadPlugins.modules[plugin], key, value);

    def togglePlugin(self, plugin, value):
        LoadPlugins.modules[plugin].PLUGIN_ENABLED = value.get()==1;

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
