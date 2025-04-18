import requests
from datetime import datetime
import time
import os

class JobBoard:
    @staticmethod
    def fetch_jobs(roles, page=1):
        API_KEY = os.getenv("ADZUNA_API_KEY")
        API_ID = os.getenv("ADZUNA_API_ID")

        jobs_seen = set()
        jobs = []
        exclude = "experienced%20manager%20supervisor%20executive%20director%20required%20engineer%20bar%20senior%20head"

        today = datetime.today()
        day = today.day

        print("checking page " + str(page))
        for i in range(0, len(roles)):
            print("checking " + roles[i] + " role")
            try:
                response = requests.get("https://api.adzuna.com/v1/api/jobs/gb/search/" + str(page) + "?app_id=" + API_ID + "&app_key=" + API_KEY + "&results_per_page=10&what_exclude=" + exclude + "&title_only=" + roles[i] + "&where=East%20London&distance=10&max_days_old=3&sort_by=date&salary_include_unknown=1")
                print(str(response.status_code))
                time.sleep(2.5)

                print("API response:" + str(response.json()))
                for job in response.json()["results"]:
                    if job["id"] not in jobs_seen:
                        new_job = {}
    
                        day_added = (job["created"].split("T")[0]).split("-")[-1] #only get the day of date
                        if int(day_added) == day:
                            new_job["date"] = "Today"
                        elif int(day_added) == day-1:
                            new_job["date"] = "Yesterday"
                        elif int(day_added) == day-2:
                            new_job["date"] = "2 days ago"
                        elif int(day_added) == day-3:
                            new_job["date"] = "3 days ago"
    
                        new_job["contract_time"] = job.get("contract_time")  # might be unknown
                        new_job["title"] = job["title"]
                        new_job["company"] = job["company"]["display_name"]
                        new_job["location"] = job["location"]["display_name"]
                        new_job["url"] = job["redirect_url"]
    
                        jobs.append(new_job)
                        jobs_seen.add(job["id"])
            except Exception as error:
                print("error, no jobs?" + str(error))
                continue
        print("end of page " + str(page))
        return jobs
