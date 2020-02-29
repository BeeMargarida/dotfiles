import os
import random
import subprocess
from pathlib import Path

import os
dotfilesDir = os.environ['DOTFILES_DIR']
print(dotfilesDir)

dirName = dotfilesDir + "/Wallpapers/"

listOfFile = os.listdir(dirName)
allFiles = list()
# Iterate over all the entries
for entry in listOfFile:
    # Create full path
    fullPath = os.path.join(dirName, entry)
    # If entry is a directory then get the list of files in this directory 
    if os.path.isdir(fullPath):
        allFiles = allFiles + getListOfFiles(fullPath)
    else:
        allFiles.append(fullPath)
                
# Get random wallpaper
randWallpaper = allFiles[random.randint(0,len(allFiles)-1)]

myCmd = 'wpg -s ' + randWallpaper + ' && wal -i ' + randWallpaper + " && exit"

os.system(myCmd)

# Add this if you want Intellij IDEs to be included
myCmd = 'cd ' + dotfilesDir + ' && ./Apps/intellij/intellijPywalGen.sh  $HOME/.AndroidStudioPreview4.0/config && exit'

os.system(myCmd)

# Update Spotify and Dunst
myCmd = 'spicetify update && rm ~/.Xresources && cp $HOME/.cache/wal/.Xresources $HOME && xrdb -merge ~/.Xresources && cp $HOME/.cache/wal/dunstrc $HOME/.config/dunst/ && killall dunst && dunst && exit'

os.system(myCmd)