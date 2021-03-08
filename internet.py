import urllib.request
import wikipedia

def check_internet_connection():
    try:
        urllib.request.urlopen("https://google.com")
        return True
    except:
        return False

def check_on_wiki(query):
    query = query.lower()
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("do you know","")
    query = query.replace("tell me","")
    query = query.strip()
    #print(query)
    try:
        data = wikipedia.summary(query,sentences = 2)
        return data
    except Exception as e:
        return ""

#check_on_wiki("what is Google")

