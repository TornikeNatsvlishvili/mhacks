from flask import Flask, request, jsonify
from natlang import Article

app = Flask(__name__)

@app.route("/", methods=['POST'])
def root():
    raw_html = request.form['html']
    article = Article(raw_html)
    
    return jsonify({'text': article.text,
        'tokens': article.tokens(),
        'pos-tag': article.pos_tag()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)