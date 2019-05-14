import flask
app = flask.Flask(__name__)

@app.route("/")

def index():
    return "测试scrapy"

if __name__ == "__main__":
    app.run()