import requests  
from output_module import output
from internet import check_internet_connection   
 
def get_news():
    if check_internet_connection():
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "API KEY"
        }
        main_url = " https://newsapi.org/v1/articles"
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            output(str(i + 1) + " " + results[i]) 
        
        return "So these were the top news today"
    
    else:
        return "Please Check your internet connection first"

    
                       

 