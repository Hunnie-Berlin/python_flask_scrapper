from flask import Flask, render_template, request, redirect

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    keyword = request.args.get("word")
    if keyword:
        keyword = keyword.lower()
        return render_template("report.html", searchingBy=keyword)
    else:
        return redirect("/")


app.run()