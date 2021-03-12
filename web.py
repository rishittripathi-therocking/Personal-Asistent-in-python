import webbrowser

def open_facebook():
    webbrowser.open('https://www.facebook.com')

def open_google():
    webbrowser.open('https://www.google.com')

def open_youtube():
    webbrowser.open('https:/www.youtube.com')

def search_query_on_google(search_string):
    webbrowser.open("https://www.google.com/search?q="+search_string)

def search_query_on_youtube(search_string):
    webbrowser.open("https://www.youtube.com/results?search_query="+search_string)