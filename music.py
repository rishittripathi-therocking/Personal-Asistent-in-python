import os
import assistant_details
import file_search
from pygame import mixer
from input_module import take_input
from output_module import output

music_path = "D:\Music"

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
        return "Can't Play Next Right Now"

def previous_song():
    if assistant_details.is_ubuntu():
        os.system('rhythmbox-client --previous')
        return "Playing Previous Song"
    else:
        return "Can't Play Previous Right Now"


def play_specific_song(song_name):
    if assistant_details.is_ubuntu():
        file_search.set_root(music_path)
        songs = file_search.searchFile(song_name)
        try:
            song_uri = songs[0]
            command = 'rhythmbox-client --play--uri="'+song_uri+'"'
            os.system()
            return "Playing Specific Song"
        except:
            return "Song not Found on Computer"
    else:
        file_search.set_root(music_path)
        songs = file_search.searchFile(song_name)
        song_uri = songs[0]
        try:
            mixer.init()
            mixer.music.load(song_uri)
            mixer.music.play()
            while True:
                output("Press 'p' to pause, 'r' to resume 'e' to stop music")
                query = take_input()
                if query == 'p':
                    mixer.music.pause()
                if query == 'r':
                    mixer.music.unpause()
                elif query == 'e':
                    mixer.music.stop()
                    break
            return "Playing Specific Song"
        except:
            return "Song Not Found on your computer"



