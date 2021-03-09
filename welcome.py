from time_module import get_hours,get_date_today
from output_module import output
from database import get_date,update_date

def greet():

    

    previous_date = get_date()
    today_date = get_date_today()
    update_date(today_date)

    if previous_date == today_date:
        output("Welcome Back")
        
    else:
        hours = int(get_hours())
        
        if hours >= 4 and hours<12:
            output("Good Morning")
        
        elif hours >=12 and hours < 16:
            output("Good Afternoon")

        else:
            output("Good Evening")

greet()

