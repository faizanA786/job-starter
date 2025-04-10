import requests
from env import API_ID
from env import API_KEY

class JobBoard:
    @staticmethod
    def fetch_jobs(roles, page=1):
        jobs_seen = set()
        jobs = []
        exclude = "manager%20supervisor%20executive%20director%20required%20engineer%20bar%20senior"

        print("checking page " + str(page))
        for i in range(0, len(roles)):
            print("checking " + roles[i] + " role")

            response = requests.get("https://api.adzuna.com/v1/api/jobs/gb/search/" + str(page) + "?app_id=" + API_ID + "&app_key=" + API_KEY + "&results_per_page=5&what_exclude=" + exclude + "&title_only=" + roles[i] + "&where=East%20London&distance=10&max_days_old=3&sort_by=date&salary_include_unknown=1")

            for job in response.json()["results"]:
                if job["id"] not in jobs_seen:
                    new_job = {}

                    date = job["created"].split("T")[0]
                    new_job["date"] = date

                    new_job["contract_time"] = job.get("contract_time")  # might be unknown
                    new_job["title"] = job["title"]
                    new_job["company"] = job["company"]["display_name"]
                    new_job["location"] = job["location"]["display_name"]
                    new_job["url"] = job["redirect_url"]

                    jobs.append(new_job)
                    jobs_seen.add(job["id"])
        print("end of page " + str(page))
        return jobs


