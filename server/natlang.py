import nltk
from nltk.tree import Tree
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
        temp_ne_chunks = nltk.ne_chunk(self.pos_tags, False)
        self.ne_chunk = []
        for chunk in temp_ne_chunks:
            if type(chunk) is tuple:
                self.ne_chunk.append({'len': 1,
                                       'tokens':[{'phrase': chunk[0], 'tag': chunk[1]}],
                                       'label': None})
            elif type(chunk) is Tree:
                temp_chunk = {'len': 0, 'tokens':[], 'label': chunk.label()};
                for i in range(len(chunk)):
                    temp_chunk['tokens'].append({'phrase': chunk[i][0], 'tag': chunk[i][1]})
                    temp_chunk['len'] += 1
                self.ne_chunk.append(temp_chunk)

        return self.ne_chunk

    def clean(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        ps = soup.find_all("p", class_="story-body-text")
        for p in ps:
            self.text += ' \n' + p.get_text()
        self.text = re.sub('[!"#$%&\'()*+,-.:;<=>?@[\\]^_`{|}~]', '', self.text)
        self.text = re.sub('\s+\”\s+', '" ', self.text)


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
