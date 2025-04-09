import json
from job_board import JobBoard

roles = ["stockroom%20assistant", "picker%20packer", "warehouse%20operative"]

job_data = []
for page in range(1, 5): # fetching 4 pages of job ads
    jobs = JobBoard.fetch_jobs(roles, page)
    job_data.extend(jobs) # so its not [[[]]] but rather [[]]

with open("job_starter/prefetch/logistics_data.json", "w", encoding="utf-8") as f: # open file called "logistics_data.json" in write mode
    json.dump(job_data, f, ensure_ascii=False, indent=2) # idented by 2 cos it looks nicer 