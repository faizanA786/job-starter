import json
from job_board import JobBoard
import time

# LOGISTICS
roles = ["stockroom", "picker%20packer", "warehouse", "parcel"]
job_data = []
for page in range(1, 5): # fetching 4 pages of job ads
    jobs = JobBoard.fetch_jobs(roles, page)
    job_data.extend(jobs) # so its not [[[]]] but rather [[]]

with open("job_starter/prefetch/logistics_data.json", "w", encoding="utf-8") as f: # open file called "logistics_data.json" in write mode
    json.dump(job_data, f, ensure_ascii=False, indent=2) # idented by 2 cos it looks nicer 
time.sleep(30)

# RETAIL
roles = ["retail", "store", "sales", "supermarket", "customer"]
job_data = []
for page in range(1, 5): # fetching 4 pages of job ads
    jobs = JobBoard.fetch_jobs(roles, page)
    job_data.extend(jobs) 

with open("job_starter/prefetch/retail_data.json", "w", encoding="utf-8") as f: # open file called "retail_data.json" in write mode
    json.dump(job_data, f, ensure_ascii=False, indent=2) 
time.sleep(30)

# HOSPITALITY
roles = ["kitchen", "catering", "waiter", "team%20member", "crew%20member"]
job_data = []
for page in range(1, 5): 
    jobs = JobBoard.fetch_jobs(roles, page)
    job_data.extend(jobs) 

with open("job_starter/prefetch/hospitality_data.json", "w", encoding="utf-8") as f: # open file called "hospitality_data.json" in write mode
    json.dump(job_data, f, ensure_ascii=False, indent=2)  