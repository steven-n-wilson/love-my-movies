from flask import Flask, render_template, request
import requests
import sys
import json
import redis

# url variables
url1 = "https://api.themoviedb.org/3/trending/movie/week?api_key=231a360ba06b66e4033e0580923144b1"
url2 = "https://api.themoviedb.org/3/discover/movie?api_key=231a360ba06b66e4033e0580923144b1&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
url3 = "https://api.themoviedb.org/3/movie/upcoming?api_key=231a360ba06b66e4033e0580923144b1&language=en-US&page=1"

# Handles requests
try:
    html_content1 = requests.get(url1).text
except:
    print(f"unable to get {url1}")
    sys.exit(1)
try:
    html_content2 = requests.get(url2).text
except:
    print(f"unable to get {url2}")
    sys.exit(1)
try:
    html_content3 = requests.get(url3).text
except:
    print(f"unable to get {url3}")
    sys.exit(1)

# Creates Redis host and variable
r = redis.Redis(host='redis', port=6379, db=0,
                charset="utf-8", decode_responses=True)

app = Flask(__name__)

trending = json.loads(html_content1)
trending_test = trending["results"]

discover = json.loads(html_content2)
discover_test = discover["results"]

upcoming = json.loads(html_content3)
upcoming_test = upcoming["results"]

print(trending_test)

print(trending_test[0]["id"])

# Initializes counters using redis at base values from request.
# ------------------------------------------------------------------------------------
# r.hmset("trending", trending_test)
# r.execute_command("JSON.SET", "object", ".", json.dumps(trending_test))
# for item in trending_test:
#     # if item == "original_title":
#     r.set("title", item)

# print(r.get("title"))


@app.route("/", methods=["GET", "POST"])  # info page
def info():
    # if request.method == "POST":
    # for n < 61:
    # if "button"+n in request.form:
    # increase the respective counter somehow.

    return render_template(
        "page_test.html",

        # trending_var = r.hgetall("trending"),
        # trending_var = json.loads(r.execute_command("JSON.GET", "object")),

        trending_var=trending_test,
        discover_var=discover_test,
        upcoming_var=upcoming_test,

    )


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")
