from flask import Flask, render_template
import json
import time

start = time.time()
app = Flask(__name__)

open_retail = "job_starter/prefetch/retail_data.json"
open_logistics = "job_starter/prefetch/logistics_data.json"
open_hospitality = "job_starter/prefetch/hospitality_data.json"

with app.app_context(): 
    with open(open_retail, "r", encoding="utf-8") as f: # open in read mode
        retail = json.load(f)
    with open(open_logistics, "r", encoding="utf-8") as f: # open in read mode
        logistics = json.load(f)
    with open(open_hospitality, "r", encoding="utf-8") as f: # open in read mode
        hospitality = json.load(f)

    html = render_template("index.html", retail=retail, logistics=logistics, hospitality=hospitality)

    with open("dist/index.html", "w", encoding="utf-8") as f:
        f.write(html)

end = time.time()
print(str(end-start) + " seconds to create new job board")