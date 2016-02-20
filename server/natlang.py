import nltk
from bs4 import BeautifulSoup

class Article:
    def __init__(self, raw_html):
        self.text = ""
        self.raw_html = raw_html
        self.clean()

    def tokens(self):
        return nltk.word_tokenize(self.text)

    def clean(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        ps = soup.find_all("p", class_="story-body-text")
        for p in ps:
            self.text += p.get_text()

def read_html(url):
    try:
        import urllib
        req=urllib.request.Request(url)
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
    print("done")
