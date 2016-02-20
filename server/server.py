from flask import Flask, request, jsonify
from .natlang import Article

app = Flask(__name__)

@app.route("/", methods=['POST'])
def root():
    raw_html = request.form['html']
    article = Article(raw_html)
    
    return jsonify({'tokens': article.tokens()})

if __name__ == "__main__":
    app.run(host='0.0.0.0')