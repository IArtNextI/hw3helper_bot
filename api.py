from flask import Flask
from flask import request
from pickle import load, dump
from os import mkdir, path

app = Flask(__name__)

@app.route("/api/<username>/<element>", methods=["GET", "POST"])
def resolve(username, element):
    if request.method == "GET":
        if not path.isdir(f"storage/{username}/"):
            mkdir(f"storage/{username}/")
        with open(f"storage/{username}/{element}", "rb") as fin:
            return load(fin)
    else:
        if not path.isdir(f"storage/{username}/"):
            mkdir(f"storage/{username}/")
        with open(f"storage/{username}/{element}", 'wb') as fout:
            dump(request.get_data(), fout)
            return "OK"

app.run("0.0.0.0", 5000, False)