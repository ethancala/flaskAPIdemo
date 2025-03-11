from flask import Flask,render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/fetch-data', methods=['GET']) 
def fetch_data(): 
    response = requests.get('http://127.0.0.1:5000/data')
    data = response.json() 
    return data



if __name__ == '__main__': app.run(port=5001, debug=True) 
    
