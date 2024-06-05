# VR Slideshow Overlay

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<img width="250" src="https://github.com/EbonCorvin/VR-Slideshow-Overlay/assets/153107703/08332a7c-0bfa-475e-b808-eb3e7dcb25f7">
<img width="250" src="https://github.com/EbonCorvin/VR-Slideshow-Overlay/assets/153107703/df7b7f81-6a8d-42eb-9fbc-face108c264b">
<img width="250" src="https://github.com/EbonCorvin/VR-Slideshow-Overlay/assets/153107703/a6b6c0cd-a116-43f6-820f-2ac4c6d0f552">

(Sorry, I don't have time to make promotional material at the moment, so here are some screenshots of how it looks like in VR)


## False antivirus alarm

You may get a false antivirus alarm (e.g. Avast) when you are trying to run the built version (exe). Please add the location of the application as an exception in your antivirus software or pull the whole source code and run it in Python instead.

## Description

Please grab the latest stable built version (exe) from the "Releases" section (right panel) or pull the latest source code and run it in Python.

It's a simple VR overlay application that show various information in VR Overlay, VRChat's chatbox and / or Text file. Although the program was original made for outputting text to VRChat's chatbox, it can run without having VRChat running at the same time.

It comes with 9 slideshow plugins that provide various information, and you can configure most of them to your need with a graphical user interface.

<img width="320" src="https://github.com/EbonCorvin/VR-Slideshow-Overlay/assets/153107703/447a24b3-80c3-4856-a5d2-bcab690d723c">

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

The program supports outputting to:

- OpenVR overlay. A overlay will attach to the hand of your choose. Currently customization options are limited, and will provide more options in the future update.
- VRChat chatbox. Output the text to VRChat's chatbox via OSC.
- Text file. Useful if you want the output text to be read by other application, like OBS streaming application.

The application may open to create new output location. For now, you can look at the example folder and see how you create a new output location.

## Installation

If you choose to run osc_start.exe, you are all set already! No additional setup is required.

However, some plugins may require some setting to run. Please go to the setting screen and provide the required setting to use the following plugins:

- SpotifyTrack - client ID and client secret
- OnlineFriends - auth cookie

You can learn how to get the mentioned setting in the Wiki page of this project.

If you want to run the script by yourself, you may have to install the following library:

- python-osc
- psutil
- GPUtil
- requests
- openvr
- pillow

I assume everyone who choose to run the script by themselves already have the experience on Python programming. Please try not to ask me about running the script by themselves.

## Usage

If you downladed the built (exe) version, please run vr_overlay.exe to start the application. If you pulled the whole source code, please run vr_overlay.py in Python.

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
