from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hellocosmos')
def hello_cosmos():
    # Testing endpoint to check if frontend & backend are connected.
    return jsonify({"message": "Hello, Cosmos!"})
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
