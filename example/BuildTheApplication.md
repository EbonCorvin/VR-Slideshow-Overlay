# Build the application

Build ~~a Bitch~~ the application is easy. Just run the following command at the src folder and the built version will be ready in the "release" folder.

```sh
python -m PyInstaller --collect-submodules plugins --hidden-import plugins --distpath release --clean --noconfirm --onefile --add-binary="output_ports/libopenvr_api_64.dll:openvr" vr_overlay.py
```

Please note that the command doesn't copy the plugins to the release folder. You will have to copy the plugins folder from the source code. Remember, the application is useless without the plugins.

pyinstaller has so many build options that you can play around with. You can run

```sh
python -m PyInstaller
```

for more information.

I may (or may not) prepare a batch file for the whole build and copy plugins folder process in the future.
