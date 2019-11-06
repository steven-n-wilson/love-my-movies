from flask import Flask, render_template, request
import requests, sys, json, redis

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
r = redis.Redis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)

app = Flask(__name__)

trending = json.loads(html_content1)
trending_test = trending["results"]

discover = json.loads(html_content2)
discover_test = discover["results"]

upcoming = json.loads(html_content3)
upcoming_test = upcoming["results"]

# print(trending_var)

# Initializes counters using redis at base values from request.
#------------------------------------------------------------------------------------
# r.hmset("trending", trending_test)
# r.execute_command("JSON.SET", "object", ".", json.dumps(trending_test))
# for item in trending_test:
#     # if item == "original_title":
#     r.set("title", item)

# print(r.get("title"))

@app.route("/", methods=["GET", "POST"]) # info page
def info():
    # if request.method == "POST":
        # if "button1" in request.form:
        #     r.incr("counter1", 1)
        # if "button2" in request.form:
        #     r.decr("counter1", 1)
        # if "button3" in request.form:
        #     r.incr("counter2", 1)
        # if "button4" in request.form:
        #     r.decr("counter2", 1)
        # if "button5" in request.form:
        #     r.incr("counter3", 1)
        # if "button6" in request.form:
        #     r.decr("counter3", 1)
        # if "button7" in request.form:
        #     r.incr("counter4", 1)
        # if "button8" in request.form:
        #     r.decr("counter4", 1)
        # if "button9" in request.form:
        #     r.incr("counter5", 1)
        # if "button10" in request.form:
        #     r.decr("counter5", 1)
        # if "button11" in request.form:
        #     r.incr("counter6", 1)
        # if "button12" in request.form:
        #     r.decr("counter6", 1)
        # if "button13" in request.form:
        #     r.decr("counter7", 1)
        # if "button14" in request.form:
        #     r.incr("counter7", 1)
        # if "button15" in request.form:
        #     r.decr("counter8", 1)
        # if "button16" in request.form:
        #     r.decr("counter8", 1)
        # if "button17" in request.form:
        #     r.incr("counter9", 1)
        # if "button18" in request.form:
        #     r.decr("counter9", 1)
        # if "button19" in request.form:
        #     r.decr("counter10", 1)
        # if "button20" in request.form:
        #     r.incr("counter10", 1)
        # if "button21" in request.form:
        #     r.decr("counter11", 1)
        # if "button22" in request.form:
        #     r.incr("counter11", 1)
        # if "button23" in request.form:
        #     r.decr("counter12", 1)
        # if "button24" in request.form:
        #     r.incr("counter12", 1)
        # if "button25" in request.form:
        #     r.decr("counter13", 1)
        # if "button26" in request.form:
        #     r.incr("counter13", 1)
        # if "button27" in request.form:
        #     r.decr("counter14", 1)
        # if "button28" in request.form:
        #     r.decr("counter14", 1)
        # if "button29" in request.form:
        #     r.incr("counter15", 1)
        # if "button30" in request.form:
        #     r.decr("counter15", 1)
    return render_template(
        "page_test.html",

        # trending_var = r.hgetall("trending"),
        # trending_var = json.loads(r.execute_command("JSON.GET", "object")),

        trending_var = trending_test,
        discover_var = discover_test,
        upcoming_var = upcoming_test,

        )

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
