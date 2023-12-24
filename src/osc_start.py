from gui import S1_StartWindow, S2_SettingWindow;
import tkinter as tk;
from updateloop import MainLoop, LoadPlugins;
import config;

root = None;

def commandCallback(command):
    if command=="startscript":
        root.destroy();
        MainLoop.update_loop();
    if command=="configwindow":
        switchWindow(S2_SettingWindow.App)
    if command=="settingwinclose":
        print("Window Closed!");
        config.saveConfig();
        switchWindow(S1_StartWindow.App);

def switchWindow(windowClass):
    global root;
    if root is not None:
        root.destroy();
    root = tk.Tk();
    windowClass(root, commandCallback)
    root.mainloop();

if __name__ == '__main__':
    LoadPlugins.read_plugins();
    config.readConfig();
    switchWindow(S1_StartWindow.App);
