# Import Libraries

import os
from flask import Flask
from flask import Response
import json

app = Flask(__name__)


@app.route("/200")
def resp200():
    return Response("{'http_code':200}", status=200, mimetype='application/json')


@app.route("/400")
def resp400():
    return Response("{'http_code':400}", status=400, mimetype='application/json')


@app.route("/health")
def health():
    with (open("app.json") as file):
        jsonFile = json.load(file)
    return Response(str(jsonFile), status=200, mimetype='application/json')


# If file is called directly called, then run the app on the PORT provided defined in ENV or use '6969'.
if __name__ == "__main__":
    app.run("0.0.0.0", port=os.getenv('PORT', 6969))
