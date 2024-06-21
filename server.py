from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/api/welcome', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api/ticker/<symbol>', methods=['GET'])
def get_ticker_data(symbol):
    ticker = yf.Ticker(symbol)
    print(ticker.info)
    return jsonify(ticker.info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

