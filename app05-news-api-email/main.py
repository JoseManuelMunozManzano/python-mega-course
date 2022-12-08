import requests

api_key = "4fc543c11a384fba9d0e3dcdb7e8605f"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-08&sortBy=publishedAt&apiKey=" \
      "4fc543c11a384fba9d0e3dcdb7e8605f"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
