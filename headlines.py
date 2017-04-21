import feedparser
from flask import Flask

app = Flask(__name__)


RSS_FEEDS = {'bbctech': 'http://feeds.bbci.co.uk/news/technology/rss.xml',
             'xlr8rnews': 'http://feeds.feedburner.com/xlr8rnews',
             'python': 'http://feeds.feedburner.com/PythonInsider',
             'xlr8rmp3': 'http://feeds.feedburner.com/xlr8rmp3s'
             }



@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbctech"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """
<html>
    <body>
        <h1> Headlines </h1>
        <b>{0}</b>
        <i>{1}</i>
        <p>{2}</p>
    </body>
</html>
    """.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)