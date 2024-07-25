from flask import Flask, render_template, request
import requests

app = Flask(__name__)

UNSPLASH_ACCESS_KEY = 'lngw9-jaxyfWTp5lBGFWvilpKGCcS9pE_3eNUI_pOHQ'  # Replace with your Unsplash Access Key

def fetch_image_urls(query, count=4):
    url = "https://api.unsplash.com/photos/random"
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'count': count
    }
    response = requests.get(url, params=params)
    print(f"Request URL: {response.url}")  # Print the request URL
    if response.status_code == 200:
        data = response.json()
        print(f"Response JSON: {data}")  # Print the response JSON
        return [img['urls']['regular'] for img in data]
    else:
        print(f"Error: {response.status_code}, {response.text}")
    return []

@app.route('/', methods=['GET', 'POST'])
def home():
    image_urls = []
    if request.method == 'POST':
        input_text = request.form['input_text'].strip().lower()
        image_urls = fetch_image_urls(input_text)
    return render_template('index.html', image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
