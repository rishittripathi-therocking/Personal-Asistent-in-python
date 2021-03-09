from output_module import output
from time_module import get_time, get_date_today
from database import get_answer_from_memory, insert_question_and_answer,update_name
from input_module import take_input
from internet import check_internet_connection, check_on_wiki
import assistant_details

def processes(query):
    answer = get_answer_from_memory(query)
    if answer == "":
        output("Don't Know this one Should i search on Internet")
        ans = take_input()
        if "yes" in ans or "y" in ans:
            answer = check_on_wiki(query)
            if answer != "":
                return answer 

    if answer == "Get The Time":
        return ("Time is " + get_time())
    
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "tell date":
        return "Today's date is " + get_date_today()

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
        output("I don't know this one, can you please tell me what is means?")
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