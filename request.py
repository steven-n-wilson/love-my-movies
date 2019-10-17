from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests, sys, csv, json, re, os, urllib.request, redis

# url variables
url = "https://api.themoviedb.org/3/trending/movie/week?api_key=231a360ba06b66e4033e0580923144b1"



# print if needed, gets too noisy
# print(soup.prettify())

try:
    html_content = requests.get(url).text
except:
    print("unable to get {url}")
    sys.exit(1)
r = redis.Redis()
with open ("trending_movies2.json", "w+") as f:
    json.dump(html_content, f, sort_keys=True, indent=4, separators=(",", ": "))

soup = BeautifulSoup(html_content, "html.parser")

app = Flask(__name__)

# with open("trending_movies.json", "w+") as f:
#     json.dump(html_content, f, sort_keys=True, indent=4)

# r.set(html_content)

# print(r.get("title"))




with open("trending_movies.json", "r") as my_file:
    data = json.load(my_file) 

@app.route("/") # info page
def info():
    return render_template(
        "page.html",
        poster_1 = data["results"][0]["poster_path"],
        title_1 = data["results"][0]["original_title"],
        average_1 = data["results"][0]["vote_average"],
        overview_1 = data["results"][0]["overview"],
        count_1 = data["results"][0]["vote_count"],
        )

@app.route("/test") # info page
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=False)
