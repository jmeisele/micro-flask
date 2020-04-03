from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello from Flask!'

@app.route('/home', methods=['GET'])
def home():
    return '<h1>Hey!</h1>'

@app.route('/json_data', methods=['POST'])
def json_data():
    payload = request.get_json()
    print(payload)
    return '<h1>You did it!</h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)