# OSC Chatbox Slideshow

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## False antivirus alarm

You may get a false antivirus alarm (e.g. Avast) when you are trying to run the built version (exe). Please add the location of the application as an exception in your antivirus software or pull the whole source code and run it in Python instead.

## Description

Please grab the latest stable built version (exe) from the "Releases" section (right panel) or pull the latest source code and run it in Python.

It's a simple OSC chatbox slideshow application that show various information with VRChat's chatbox, just like other chatbox script that you can see in the public worlds.

It comes with 9 slideshow plugins that provide various information, and you can configure most of them to your need with a graphical user interface.

## Features

The application comes with the following slideshow plugins:

- ForegroundWindow.py - Display the title of the top-most window you're on
- GPUUsage.py - Display the GPU usage information (VRAM / Temperature / Usage)
- LocalTime.py - Display local time
- LocalWeather.py - Display your local weather
- MessageBubble.py - Display a line of custom message
- OnlineFriends.py - Display the number of your VRChat online friends and number of your friends who are currently in a private world
- PCUsage.py - Display the PC usage information (RAM / CPU / Usage)
- SpotifyTrack.py - Display the current Spotify track you're listening to
- VRCUptime.py - Display your VRChat uptime (The time passed since you have played VRChat)

Every slideshow plugin is a Python script that you can edit in the “plugins” folder. You can also create your own plugin to display information the original application doesn’t support. Please have a look at the in the “example” folder.

Also, other than outputting to VRChat, you can also enable outputting to other location:

- Text file. Useful if you want the output text to be read by other application, like OBS streaming application.
- ~~OpenVR overlay (Coming Soon™). You can keep the output text to yourself by displaying them in your VR overlay.~~

The application may open to create new output location. For now, you can look at the example folder and see how you create a new output location.

## Installation

If you choose to run osc_start.exe, you are all set already! No additional setup is required.

However, some plugins may require some setting to run. Please go to the setting screen and provide the required setting to use the following plugins:

- SpotifyTrack - client ID and client secret
- OnlineFriends - auth cookie

If you want to run the script by yourself, you may have to install the following library:

- python-osc
- psutil
- GPUtil
- requests

I assume everyone who choose to run the script by themselves already have the experience on Python programming. Please try not to ask me about running the script by themselves.

## Usage

If you downladed the built (exe) version, please run osc_start.exe to start the application. If you pulled the whole source code, please run osc_start.py in Python.

A window will appear after you run the application. You can click on the "Start" button to start outputting text to VRChat immediately; Or click on the "Setting..." button for the "Setting Screen".

## Contributing

To anyone who want to make any contribution to the project. Please feel free to push the plugin you write so that it could be included in the next update of the application. Also, bug fixes and improvement are welcomed.

If you found any bug or area of improvement when you're using the application, please open an issue ticket so that I could investigate and fix it as soon as possible.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Do you know that this project is started upon the request of my beloved friend, the attention seeker, the goofy Yotuber - TwoCool4Yo?

Go check out his Youtube channel, it's full of funny content! :3

## Contact

Normally you can just start a new issue ticket in the project if you found and issue or want to make some suggestion. But if you really want to contact me, feel free to add me on Telegram and Discord, username: EbonCorvin.
