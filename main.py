from flask import Flask

from api.code.controller.codeController import CodeController
from cache.cache import Cache

app = Flask(__name__)
cache = Cache()

CodeController.newController(app, cache)

if __name__ == "__main__":
    app.run(debug=True)


