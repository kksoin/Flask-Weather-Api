from flask import Flask, jsonify, request
from weather import weather_city
from bs4 import BeautifulSoup as BS
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/city/<string:city>')
def get_product_id(city):
    if len(city) <= 1:
        return {"Status":"Fail","Cause":"Не верный город"}
    else:
        weather = weather_city(city, requests, BS)
        print(request.form)
        return jsonify(weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)