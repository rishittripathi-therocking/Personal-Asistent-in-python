from database import get_name
import platform

name = get_name()

def is_ubuntu():
    if 'Linux' == platform.system():
        return True
    else:
        return False 




