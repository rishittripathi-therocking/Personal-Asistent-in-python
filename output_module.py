import assistant_details 
from speak import speak
from database import get_speak

def output(o):
    if get_speak() == "on":
        speak(o)
    print(assistant_details.name+':'+o)
    print()