from flask import Flask, render_template, request, redirect, send_file
from indeed import get_indeed_jobs
from stackoverflow import get_stackoverflow_jobs
from save import save_to_file

app = Flask("hScraper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<username>")
def name(username):
    return f"Hello {username}"


@app.route("/report")
def report():
    job = request.args.get("job")
    if job:
        job = job.lower()

        jobs = db.get(job)
        if not jobs:
            jobs = get_indeed_jobs(job)
            jobs += get_stackoverflow_jobs(job)
            db[job] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", resultsNumber=len(jobs), searchingBy=job, jobs=jobs
    )


@app.route("/export")
def export():
    try:
        job = request.args.get("job")
        if not job:
            raise Exception()
        job = job.lower()
        jobs = db.get(job)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("./")


if __name__ == "__main__":
    app.run()