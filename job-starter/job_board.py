import requests
from env import API_ID
from env import API_KEY

# roles = ["retail%20assistant", "kitchen%20assistant", "stockroom%20assistant", "kitchen%20porter", "sales%20assistant", "catering%20assistant", "supermarket%20assistant", "customer%20service", "waiter", "team%20member", "picker%20packer"]

class JobBoard:
    @staticmethod
    def fetch_jobs(roles, page=1):
        jobs_seen = set()
        jobs = []
        exclude = "manager%20supervisor%20executive%20director"

        print("checking page " + str(page))
        for i in range(0, len(roles)):
            print("checking " + roles[i] + " role")

            response = requests.get("https://api.adzuna.com/v1/api/jobs/gb/search/" + str(page) + "?app_id=" + API_ID + "&app_key=" + API_KEY + "&results_per_page=8&what_exclude=" + exclude + "&title_only=" + roles[i] + "&where=London&max_days_old=3&sort_by=date&salary_include_unknown=1")

            for job in response.json()["results"]:
                if job["id"] not in jobs_seen:
                    new_job = []

                    date = job["created"]
                    date = date.split("T")[0]
                    new_job.append(date) #0

                    new_job.append(job["title"]) #1
                    new_job.append(job["description"]) #2
                    new_job.append(job["location"]["display_name"]) #3

                    url = job["redirect_url"]
                    url = url.split("?")[0]
                    new_job.append(url) #4

                    jobs.append(new_job)

                    jobs_seen.add(job["id"])
        print("end of page " + str(page))
        return jobs


