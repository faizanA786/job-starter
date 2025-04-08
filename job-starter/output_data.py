from flask import Flask, render_template
from job_board import JobBoard 

app = Flask(__name__)
jobs_seen = set()

@app.route("/")
def add_jobs():
    # retail default category
    roles = ["retail%20assistant", "sales%20assistant", "supermarket%20assistant", "customer%20service", "stockroom%20assistant"]
    jobs_data = JobBoard.fetch_jobs(roles, 1)
    html =  render_template("index.html", jobs=jobs_data)
    return html

if __name__ == "__main__":
    app.run(debug=True)