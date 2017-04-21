import feedparser
from flask import Flask, render_template,request

app = Flask(__name__)


RSS_FEEDS = {'bbctech': 'http://feeds.bbci.co.uk/news/technology/rss.xml',
             'xlr8rnews': 'http://feeds.feedburner.com/xlr8rnews',
             'python': 'http://feeds.feedburner.com/PythonInsider',
             'xlr8rmp3': 'http://feeds.feedburner.com/xlr8rmp3s'
             }



@app.route("/",methods=['GET','POST'])
@app.route("/<publication>")
def get_news(publication="bbctech"):
    query = request.form.get("publicaton")
    if not query or query.lower() not in RSS_FEEDS:
        publication="bbctech"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html",
                           articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)