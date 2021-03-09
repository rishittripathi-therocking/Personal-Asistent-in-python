from datetime import datetime
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    julie_Answer = current_time[0:2]+" hours "+current_time[3:5]+" minutes "+current_time[7:]+" seconds"
    return julie_Answer

def get_hours():
    now = datetime.now()
    return now.strftime("%H")

def get_date_today():
    now = datetime.now()
    year = now.strftime("%Y")
    mon = now.strftime("%m")
    day = now.strftime("%d")
    tod = day+"-"+mon+"-"+year
    return tod