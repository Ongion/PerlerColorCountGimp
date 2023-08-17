# PerlerColorCountGimp
Script for counting colors in perler-bead design image (1 pixel per bead)

# Instructions
Download `count_colors.py`, and slap that baby in whatever folder GIMP uses to store plugins
By default on Windows, that'll be something like `C:\Users\<your username>\AppData\Roaming\GIMP\<gimp's version number, probably 2.10>\plug-ins`
To get there even faster, just type `%APPDATA'\GIMP\2.10\plug-ins` into your Explorer window!

If you don't have that folder, or if you're running another OS, just check inside GIMP for what folder it's using. It'll be under `Edit -> Preferences -> Folders -> Plug-ins`. Any folder in that list will work, and you can add your own folders if you want to organize stuff better. I'm not your boss.

Once you've done that, just open your image in GIMP! Then hit `Filters -> Perler -> Count Colors`, give it a sec, and it'll pop up a very ugly dialog that lists the hex-codes of your colors and the number of each color you'll need! I already spent way too long getting that to even show up, and couldn't be bothered to make it look prettier. It works, ok?

IMPORTANT NOTE: Make sure your file is 1 pixel per 1 bead! Otherwise, you won't get an accurate count and it'll take longer to run. On a 290x290 bead project (HUGE), this took like 5 seconds to run? I could probably make that faster, but that's a pretty large example. Also, it might pop up another console dialog? With some cryptic messages from GIMP itself about two plugins trying to define the same function (maybe it's just my computer)?? If it does that, sorry, that's not my code, and you can absolutely ignore that. It'll close on its own once you close the color count popup.
