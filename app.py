from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'YOUR_NEWS_API_KEY'  # Replace with your News API key
BASE_URL = 'https://newsapi.org/v2/'

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get('query')
    if query:
        url = f"{BASE_URL}everything?q={query}&apiKey={API_KEY}"
    else:
        url = f"{BASE_URL}top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)
    articles = response.json().get('articles', [])

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
