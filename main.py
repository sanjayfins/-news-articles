import requests

query= input("what kind of news you are interested today:")

api="74b0f2c5361d406a9b1d9974fbc7bad0"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-09&sortBy=publishedAt&apiKey={api}"
print(url)
r=requests.get(url)
data=r.json()
articles=(data["articles"])
for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n******************************************************\n")