from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("JobScrapper")


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
        jobs = get_jobs(keyword, location)
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


app.run()
