from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes of the Flask app

@app.route('/news', methods=['GET'])
def get_technology_news():
    try:
        api_key = "7990d9e6e93d40fd9af116f94eecdeef"
        url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=7990d9e6e93d40fd9af116f94eecdeef'
        params = {
            'country': 'in',
            'category': 'technology',
            'apiKey': api_key
        }
        response = requests.get(url, params=params)
        news_data = response.json()
        return jsonify(news_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
