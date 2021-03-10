from output_module import output
from time_module import get_time, get_date_today
from database import *
from input_module import take_input
from internet import check_internet_connection, check_on_wiki
import assistant_details
from web import open_facebook,open_google,open_youtube
from music import play_music,pause_music,stop_music,next_song,previous_song,play_specific_song

def processes(query):
    answer = get_answer_from_memory(query)
    

    if answer == "Get The Time":
        return ("Time is " + get_time())
    
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "tell date":
        return "Today's date is " + get_date_today()
    
    elif answer == "on speak":
        return update_speech("on")

    elif answer == "off speak":
        return update_speech("off")
    
    elif answer == 'open facebook':
        open_facebook()
        return "I am going to open Facebook Now"
    
    elif answer == 'open google':
        open_google()
        return "I am going to open Google Now"
    
    elif answer == 'open browser':
        open_google()
        return "I am going to open Browser Now"
    
    elif answer == 'play music':
        return play_music()
    
    elif answer == 'pause music':
        return pause_music()

    elif answer == 'stop music':
        return stop_music()

    elif answer == 'play next song':
        return next_song()
    
    elif answer == 'play previous song':
        return previous_song()
    
    elif answer == 'open youtube':
        open_youtube()
        return 'Opening youtube now'
    
    elif answer == 'play specific song':
        output("Enter Song Name")
        song = take_input()
        song = song.lower()
        return play_specific_song(song)
        

    elif answer == "change name":
        output("Okay! What do you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "Can't change. It is my previous Name Sorry"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "Now You can call me " + temp

    else:
        output("Don't Know this one Should i search on Internet")
        ans = take_input()
        if "yes" in ans or "y" in ans:
            answer = check_on_wiki(query)
            if answer != "":
                return answer 
        else:
            output("can you please tell me what is means?")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means","")
                ans = ans.strip()
                value = get_answer_from_memory(ans)
                if value == "":
                    return "Can't help you with this question"
                else:
                    insert_question_and_answer(query,value)
                    return "Thank's I will remember for next time"
            else:
                return "Can't help with this question, Sorry"