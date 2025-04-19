from jinja2 import Environment, FileSystemLoader
import json
import time

start = time.time()

open_retail = "job_starter/prefetch/retail_data.json"
open_logistics = "job_starter/prefetch/logistics_data.json"
open_hospitality = "job_starter/prefetch/hospitality_data.json"

with open(open_retail, "r", encoding="utf-8") as f: # open in read mode
    retail = json.load(f)
with open(open_logistics, "r", encoding="utf-8") as f: # open in read mode
    logistics = json.load(f)
with open(open_hospitality, "r", encoding="utf-8") as f: # open in read mode
    hospitality = json.load(f)

env = Environment(loader=FileSystemLoader("job_starter/templates"))
template = env.get_template("index.html")
html = template.render(retail=retail, logistics=logistics, hospitality=hospitality)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html) # THIS BUILDS INTO DOCS, CAN CAUSE MERGE CONFLICT 

end = time.time()
print(str(end-start) + " seconds to create new job board")