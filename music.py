import os
import assistant_details

def play_music():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --play')
        return "Playing Music"

    else:
        return "Can't Play Right Now"


def pause_music():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --pause')
        return "Pausing Music"

    else:
        return "Can't Pause Right Now"

def stop_music():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --stop')
        return "Stopping Music"

    else:
        return "Can't Stop Right Now"

def next_song():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --next')
        return "Playing Next Song"

    else:
        return "Can't Stop Right Now"

def previous_song():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --previous')
        return "Playing Previous Song"

    else:
        return "Can't Stop Right Now"