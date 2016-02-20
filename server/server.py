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

@app.route("/picture/<query>")
def search_image(name):
    query = urllib.parse.urlencode({'q': name})
    result = read_html('http://images.google.com/images?'+query+'&sout=1')
    soup = BeautifulSoup(result,'html.parser')
    ps = soup.find_all("img")
    try:
       value = ps[0].get('src')
       return value
    except Exception as e:
        output = format(e)
        print(output)

@app.route("/search/<query>")
def search(name):
    query = urllib.parse.urlencode({'q': name})
    result = read_html('https://www.google.com/search?'+query)
    soup = BeautifulSoup(result,'html.parser')
    ps = soup.find_all("a")
    try:
       value = ps[0].get('data-href')
       return value
    except Exception as e:
        output = format(e)
        print(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)