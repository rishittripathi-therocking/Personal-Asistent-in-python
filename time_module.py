from datetime import datetime
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    julie_Answer = current_time[0:2]+" hours "+current_time[3:5]+" minutes "+current_time[7:]+" seconds"
    return julie_Answer