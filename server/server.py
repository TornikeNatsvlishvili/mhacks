from flask import Flask, request, jsonify
from natlang import Article, read_html
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=['POST'])
def root():
    raw_html = request.form['html']
    article = Article(raw_html)
    
    return jsonify({'text': article.text,
        'tokens': article.tokens(),
        'pos-tag': article.pos_tag(),
        'ne-chunk': article.ne_chunk() })

@app.route("/picture/<query>")
def search_image(query):
    query_param = urllib.parse.urlencode({'q': query})
    result = read_html('http://images.google.com/images?'+query_param+'&sout=1')
    soup = BeautifulSoup(result,'html.parser')
    ps = soup.find_all("img")
    try:
       value = ps[0].get('src')
       return value
    except Exception as e:
        output = format(e)
        print(output)

@app.route("/search/<query>")
def search(query):
    query_param = urllib.parse.urlencode({'q': query})
    result = read_html('https://www.google.com/search?'+query_param)
    soup = BeautifulSoup(result,'html.parser')
    ps = soup.select("h3 > a")
    # ps = soup.find_all("a")
    try:
       value = ps[0].get('href')
       return value
    except Exception as e:
        output = format(e)
        print(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)