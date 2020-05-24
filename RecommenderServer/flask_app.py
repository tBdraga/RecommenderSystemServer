from flask import Flask, request, jsonify
from recommender import compute_result

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/recommend')
def recommend():
    print(request.args.get("brandName"))
    return jsonify({'recommendations': compute_result(request.args.get("brandName"))})

if __name__ == '__main__':
    app.run(debug=True)