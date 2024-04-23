from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    version = os.getenv("VERSION", "v1")
    if version == "v1":
        return "Hello everyone! This is version 1."
    elif version == "v2":
        return "Hello everyone! This is the updated version 2."
    else:
        return "Hello everyone! Version unknown."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
