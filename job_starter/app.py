from flask import Flask, render_template
import json

app = Flask(__name__)
open_url = "job_starter/prefetch/hospitality_data.json"

@app.route("/")
def add_jobs():
    with open(open_url, "r", encoding="utf-8") as f: # open in read mode
        jobs = json.load(f)
        html = render_template("index.html", jobs=jobs)
    return html

if __name__ == "__main__":
    app.run(debug=True)