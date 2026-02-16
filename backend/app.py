from flask import Flask, jsonify
from flask_cors import CORS
from luna import get_lunar_data

app = Flask(__name__)
CORS(app)

@app.route('/api/hellocosmos')
def hello_cosmos():
    # Testing endpoint to check if frontend & backend are connected.
    return jsonify({"message": "Hello, Cosmos!"})
    

@app.route('/api/lunar')
def luna_today():
    #Returning the current lunar phase, sign and illumination data
    data = get_lunar_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

    
