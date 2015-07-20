from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index_page():

    return render_template("index.html")

@app.route("/application-form")
def appForm():



@app.route("/application", methods=['POST'])
def thanks_for_submission():
	firstnm = request.form.get("firstname")
    lastnm = request.form.get("lastname")
    salaryamt = request.form.get("salary")
    jobtitle = request.form.get("job")

    return render_template("thanks.html", firstname = firstnm, lastname = lastnm, salary = salaryamt, job = jobtitle)

if __name__ == "__main__":
    app.run(debug=False)