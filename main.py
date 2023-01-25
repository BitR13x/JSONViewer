import requests
from bs4 import BeautifulSoup
import json
import os
from termcolor import colored

def processArticle(articles, classname, page):
    result = []
    for article in articles:
        headline = article.find('a', class_=classname )
        if headline and headline.get_text():
            article_obj = dict()
            article_obj["name"] = headline.get_text().strip()
            if headline.get("href")[0] == "/":
                article_obj["href"] = page+headline.get("href")
            else:
                article_obj["href"] = headline.get("href")
            result.append(article_obj)
    return result

def cryptonews():
    page = "https://cryptonews.com"
    response = requests.get(page)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')
    return processArticle(articles, "article__title", page)

def coinmarketnews():
    page = "https://coinmarketcap.com"
    response = requests.get(page+"/headlines/news/")
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', class_=["sc-aef7b723-0", "sc-b1d35755-0", "cGYUCj"])
    return processArticle(articles, ["dNqZZN", "cmc-link"], page)

def searchKeyWords(array, keywords):
    if isinstance(keywords, list):
        result = []
        lowercase_list = [s.lower() for s in keywords]
        for keyword in lowercase_list:
            for obj_index in range(len(array)):
                if keyword in array[obj_index]["name"].lower():
                    result.append(array[obj_index])
        return result
    else:
        print(colored('Only lists are allowed!', 'red'))

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    def savein_current_directory(filename):
        return current_directory+"/"+filename
    
    keywords = ["eth"]
    res1, res2 = coinmarketnews(), cryptonews()
    res1.extend(res2)
    result = searchKeyWords(res1, keywords)
    #with open(savein_current_directory('data.json')) as json_file:
    #    data = json_file.read()

    with open(savein_current_directory('data.json'), 'w') as json_file:
        json.dump(result, json_file, indent=4, sort_keys=True, separators=(',', ': '))

    print(colored("[*]DONE[*]", "green"))

if __name__ == "__main__":
    main()
