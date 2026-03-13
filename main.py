from flask import Flask, render_template
from api.code.controller.codeController import CodeController
from cache.cache import Cache

app = Flask(__name__)
cache = Cache()

CodeController.newController(app, cache)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


