import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root, commandCallback):
        self.commandCallback = commandCallback;

        root.title("VRChat Chatbox Slideshow")
        root.resizable(width=False, height=False)

        app_name_label = tk.Label(root, text="OSC Chatbox Slideshow", font=("Segoe UI", 20))
        app_name_label.grid(row=0, columnspan=2, padx=10, pady=20)
        app_name_label["justify"] = "center"

        GButton_407=tk.Button(root, text="Start")
        GButton_407["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Segoe UI',size=16)
        GButton_407["font"] = ft
        GButton_407["fg"] = "#000000"
        GButton_407["justify"] = "center"
        GButton_407.grid(row=1,column=0,padx=10,pady=5);
        GButton_407["command"] = self.GButton_407_command

        GButton_17=tk.Button(root, text="Setting...")
        GButton_17["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Segoe UI',size=16)
        GButton_17["font"] = ft
        GButton_17["fg"] = "#000000"
        GButton_17["justify"] = "center"
        GButton_17.grid(row=1,column=1,padx=10,pady=5);
        GButton_17["command"] = self.GButton_17_command

    def GButton_407_command(self):
        self.commandCallback("startscript")

    def GButton_17_command(self):
        self.commandCallback("configwindow")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()