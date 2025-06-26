import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

try:
    with open("laureates.csv", "r") as f:
        reader = csv.DictReader(f)
        laureates = list(reader)
except Exception as e:
    print(f"Error reading laureates.csv: {e}")
    laureates = []


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()

    # tip: remember that laureate["name"] contains a first name
    for laureate in laureates:
        if search_string in laureate["name"].lower():
            results.append(laureate)
            continue
        if search_string in laureate["surname"].lower():
            results.append(laureate)

    return jsonify(results)

#if __name__ == "__main__":
app.run(debug=True)
