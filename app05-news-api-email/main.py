import requests
from send_email import send_email

api_key = "4fc543c11a384fba9d0e3dcdb7e8605f"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-08&sortBy=publishedAt&apiKey=" \
      "4fc543c11a384fba9d0e3dcdb7e8605f"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(raw_message=body)
