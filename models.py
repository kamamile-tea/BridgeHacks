import random
import requests



data = requests.get("http://newsapi.org/v2/everything?%22+%22country=us&language=en&q=+recycle&q=-tech&qInTitle=-apple&q=-sandisk&pageSize=70&sortBy=relevancy&apiKey=4ea6d49c4f8241338277e264329cc030"

  ).json()


  
piecesNews= {
  "sources": {

    1: "",
    2: "",
    3: "",
  },

  "imagesUrls": {

    1: "",
    2: "",
    3: "",
  },

  "titles": {

    1: "",
    2: "",
    3: "",
  },

  "urls": {
    
    1: "",
    2: "",
    3: "",
  },
}


def newsPieces():
  num = random.randint(0, len(data['articles']))

  # Make sure the num doesn't go out of range of the default max articles
  while num >= len(data['articles'])-3:
    print(num, "oopz")
    num = random.randint(0, len(data['articles']))

  count = 1
  print(num)

  for i in range(num, num+3):
    print(num)
    piecesNews["sources"][count] = data["articles"][i]["source"]["name"]
    piecesNews["imagesUrls"][count] = data["articles"][i]["urlToImage"]
    piecesNews["titles"][count] = data["articles"][i]["title"]
    piecesNews["urls"][count] = data["articles"][i]["url"]
    count +=1

  return piecesNews
