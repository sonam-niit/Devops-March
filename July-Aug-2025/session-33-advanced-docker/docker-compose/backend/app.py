from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app) #enable cross origin to access from frontend
@app.route('/api')
def hello():
    return jsonify(message="Hello From Python Backend")

if __name__== '__main__':
    app.run(host='0.0.0.0',port=5000)