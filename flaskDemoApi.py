from flask import Flask, jsonify

app = Flask(__name__)

#demo data
#simple key -> value pairs dictonary
data = [ {"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"} ]

@app.route('/')
def welcome():
        return "welcome to the API, go to http://127.0.0.1:5000/data to see the JSON data we pass!"

#create routinng for data, we use GET method here
@app.route('/data', methods=['GET']) 
def get_data(): return jsonify(data)

#run app if true
if __name__ == '__main__':
        app.run(debug=True)
