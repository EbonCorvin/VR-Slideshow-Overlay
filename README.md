# OSC Chatbox Slideshow

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## False antivirus alarm

It's found that some antivirus may make a false alarm when you're attempting to run this application. It's most likely because most of the anti-virus doesn't like program that has a bunch of file packed together inside it. If you're worried about the false alarm, you can fetch the whole source code and run it as a python script instead.

## Description

Please grab the latest version of the program from the release folder!

You like attention? If the answer is positive, then I hope that this little application can fulfill your daily need of attention! This little python script displays a slidershow of information overhead when you're playing VRChat.

The content of the slideshow is variable, it can range from the most common information like the local time and the spotify track your're currently playing, to some silly information that could grab the eyeballs when you're wandering around in the public world or hanging out with your friends!

The application is easy to run, no python executable is needed, no a bunch of "python -m pip library_name" is required, just run osc_start.exe and you're all set! Of course you can click on the "Setting" button to do some configuration first, but you can also go straight to the "Start" button to start the slideshow immediately.

Feeling nerdy or wanted to do some code change before running it? You can also fetch the source code from the respository, and they're all yours and you can do whatever you want with them!

Also, every slideshow is a plugin in the application. You can locate to the plugins folder, creating your own script and run it immediately! You don't have to fetch the whole source code and do the compilation just to include your pride self-made slideshow plugin!

## Features

With this application, you unlock the ability to display a slideshow with VRChat's OSC chatbox overhead when you're in the game. Every slideshow is a plugin and is loaded on demand, and you can create your own plugin and display the information this application is not currently providing.

The application comes with the following plugins:

- ForegroundWindow.py - Display the title of the top-most window you're on
- GPUUsage.py - Display the GPU usage information (VRAM / Temperature / Usage)
- LocalTime.py - Display local time
- LocalWeather.py - Display your local weather
- MessageBubble.py - Display a line of custom message
- OnlineFriends.py - Display the number of your VRChat online friends and number of your friends who are currently in a private world
- PCUsage.py - Display the PC usage information (RAM / CPU / Usage)
- SpotifyTrack.py - Display the current Spotify track you're listening to
- VRCUptime.py - Display your VRChat uptime (The time passed since you have played VRChat)

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

I assuem everyone who choose to run the scrpt by themselves already have the experience on Python programming. Please try not to ask me about running the script by themeselves.

## Usage

Explain how to use your application. Provide code examples or screenshots if applicable.

## Contributing

To anyone who want to make any contribution to the project.Please feel free to push the plugin you write so that it could be included in the next update of the application. Also, bug fixes and improvement are welcomed.

If you found any bug or area of improvement when you're using the application, please open a issue ticket so that I could investigate and fix it as soon as possible.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Do you know that this project is started upon the request of my beloved friend, the attention seeker, the goofy Yotuber - TwoCool4Yo?

Go check out his Youtube channel, it's full of funny content! :3

## Contact

Normally you can just start a new issue ticket in the project if you found and issue or want to make some suggestion. But if you really want to contact me, feel free to add me on Telegram and Discord, username: EbonCorvin.
