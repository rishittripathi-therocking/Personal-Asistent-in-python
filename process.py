from output_module import output
from time_module import get_time
from database import get_answer_from_memory
def processes(query):
    answer = get_answer_from_memory(query)
    if answer == "Get The Time":
        return ("Time is " + get_time())
    else:
        return "Nothing to Return"