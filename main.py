from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    keyword = request.args.get("what")
    location = request.args.get("where")
    if keyword and location:
        keyword = keyword.lower()
        location = location.lower()
        existingJobs = db.get(keyword)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(keyword, location)
            db[keyword] = jobs
        number_of_jobs = len(jobs)
        return render_template(
            "report.html",
            what=keyword,
            where=location,
            job_list=jobs,
            number=number_of_jobs,
        )
    else:
        return redirect("/")


@app.route("/export")
def export():
    try:
        keyword = request.args.get("what")
        location = request.args.get("where")
        if not keyword or not location:
            raise Exception()
        keyword = keyword.lower()
        location = location.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run()
