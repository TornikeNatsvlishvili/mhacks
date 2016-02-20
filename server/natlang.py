import nltk
from bs4 import BeautifulSoup
import re

class Article:
    def __init__(self, raw_html):
        self.text = ""
        self.raw_html = raw_html
        self.clean()

    def tokens(self):
        self.tokens = nltk.word_tokenize(self.text)
        return self.tokens

    def pos_tag(self):
        self.pos_tags = nltk.pos_tag(self.tokens)
        return self.pos_tags

    def ne_chunk(self):
        self.ne_chunk = nltk.ne_chunk(self.pos_tags, False)
        return self.ne_chunk

    def clean(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        ps = soup.find_all("p", class_="story-body-text")
        for p in ps:
            self.text += ' \n' + p.get_text()
        self.text = re.sub('[!"#$%&\'()*+,-.:;<=>?@[\\]^_`{|}~]', '', self.text)


def read_html(url):
    try:
        import urllib
        hdr = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }
        req=urllib.request.Request(url, headers=hdr)
        from http.cookiejar import CookieJar
        cj = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        response = opener.open(req)
        raw_response = response.read().decode('utf-8', errors='ignore')
        response.close()
        return raw_response
    except urllib.request.HTTPError as inst:
        output = format(inst)
        print(output)

if __name__ == "__main__":
    url = 'http://www.nytimes.com/2016/02/20/us/politics/republicans-speed-across-south-carolina-as-race-tightens.html'
    html_doc = read_html(url)
    article = Article(html_doc)
    a = article.tokens()
    b = article.pos_tag()
    c = article.ne_chunk()
    print("done")
