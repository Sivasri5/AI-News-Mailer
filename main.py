import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from send_email import send_email
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


url = ("https://newsapi.org/v2//top-headlines?" 
       "category=business&"
       "language=en&"
       "pageSize=8&"
       "sortBy=publishedAt&apiKey="+ NEWS_API_KEY
       )

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
articles =  content["articles"]

#AI summarizing the news
models = init_chat_model(
    model = "gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GEMINI_API_KEY
)

prompt = f"""
You are a news summarizer.
Write a short paragraph analyzing those news. 
Add another second paragraph to tell me how they affect the stock
Summarize the following news article:
{articles}
"""

response = models.invoke(prompt)
final_res = response.content
print(final_res)

body = "Subject: News Summary\n\n" + final_res + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
