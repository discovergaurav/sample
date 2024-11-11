from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/api/hello', methods=['GET'])
def hello_api():
    response = {
        "message": "Hello, world!",
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
