import os
from email.mime.text import MIMEText

import requests

from email_util import send_email

API_KEY = os.getenv('NEWS_API')
news_url = ("https://newsapi.org/v2/everything?"
            "q=tesla&"
            "language=en&"
            "from=2025-05-17&"
            "sortBy=publishedAt&"
            f"apiKey={API_KEY}")

request = requests.get(news_url)
content = request.json()
email_articles = []

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"

subject = "Daily News for the Foo's"
email_msg = MIMEText(body)
email_msg["Subject"] = subject

send_email(email_msg)
