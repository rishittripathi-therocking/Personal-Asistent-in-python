import os
from wallpaper import set_wallpaper, get_wallpaper
from assistant_details import is_ubuntu
import random

def change_wallpaper():
    if is_ubuntu():
        wallpapers_path = '/media/rishit/Rishit/wallpapers'
        wallpapers = os.listdir(wallpapers_path)
        wallpaper = random.choice(wallpapers)
        command = 'gsettings set org.gnome.desktop.background picture-uri file:///'+wallpapers_path +'/'+wallpaper
        os.system(command)
    else:
        get_wallpaper()
        set_wallpaper('location/to/image.jpg')

