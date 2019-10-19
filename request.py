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

r = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

# with open ("trending_movies2.json", "w+") as f:
#     json.dump(html_content, f, sort_keys=True, indent=4, separators=(",", ": "))

soup = BeautifulSoup(html_content, "html.parser")

app = Flask(__name__)

# with open("trending_movies.json", "w+") as f:
#     json.dump(html_content, f, sort_keys=True, indent=4)

# with open("trending_movies.json", "w+") as f:
#     json.dump(soup, f, sort_keys=True, indent=4)

# r.set(html_content)

# print(r.get("title"))


with open("trending_movies.json", "r", encoding="utf8") as my_file:
    data = json.load(my_file) 

with open("Discover_movies.json", "r", encoding="utf8") as my_f:
    data2 = json.load(my_f) 

# Initializes counters using redis at base values from request.
r.set("counter1", data["results"][0]["vote_count"])
r.set("counter2", data["results"][1]["vote_count"])
r.set("counter3", data["results"][2]["vote_count"])
r.set("counter4", data["results"][3]["vote_count"])
r.set("counter5", data["results"][4]["vote_count"])

r.set("counter6", data2["results"][2]["vote_count"])
r.set("counter7", data2["results"][3]["vote_count"])
r.set("counter8", data2["results"][4]["vote_count"])
r.set("counter9", data2["results"][8]["vote_count"])
r.set("counter10", data2["results"][9]["vote_count"])

# if(increase1):
#     r.incr("counter1")
# Tecnicamente así se haría pero en todos los sitios que he visitado dice que necesito AJAX para afectar Redis.

@app.route("/") # info page
def info():
    return render_template(
        "page.html",
        #--------------------------------------------------------------Trending-----------
        # Spiderman
        poster_1 = data["results"][0]["poster_path"],
        title_1 = data["results"][0]["original_title"],
        average_1 = data["results"][0]["vote_average"],
        overview_1 = data["results"][0]["overview"],
        count_1 = r.get("counter1"),
        
        # The Lion King
        poster_2 = data["results"][1]["poster_path"],
        title_2 = data["results"][1]["original_title"],
        average_2 = data["results"][1]["vote_average"],
        overview_2 = data["results"][1]["overview"],
        count_2 = r.get("counter2"),

        # El Camino
        poster_3 = data["results"][2]["poster_path"],
        title_3 = data["results"][2]["original_title"],
        average_3 = data["results"][2]["vote_average"],
        overview_3 = data["results"][2]["overview"],
        count_3 = r.get("counter3"),

        # Toy Story 4
        poster_4 = data["results"][3]["poster_path"],
        title_4 = data["results"][3]["original_title"],
        average_4 = data["results"][3]["vote_average"],
        overview_4 = data["results"][3]["overview"],
        count_4 = r.get("counter4"),

        # Joker
        poster_5 = data["results"][4]["poster_path"],
        title_5 = data["results"][4]["original_title"],
        average_5 = data["results"][4]["vote_average"],
        overview_5 = data["results"][4]["overview"],
        count_5 = r.get("counter5"),

        #--------------------------------------------------------------Discover-----------
        # Skipped over any movies that have already been used.
        # IT 2
        poster_6 = data2["results"][2]["poster_path"],
        title_6 = data2["results"][2]["original_title"],
        average_6 = data2["results"][2]["vote_average"],
        overview_6 = data2["results"][2]["overview"],
        count_6 = r.get("counter6"),

        # Gemini Man
        poster_7 = data2["results"][3]["poster_path"],
        title_7 = data2["results"][3]["original_title"],
        average_7 = data2["results"][3]["vote_average"],
        overview_7 = data2["results"][3]["overview"],
        count_7 = r.get("counter7"),

        # 23-F
        poster_8 = data2["results"][4]["poster_path"],
        title_8 = data2["results"][4]["original_title"],
        average_8 = data2["results"][4]["vote_average"],
        overview_8 = data2["results"][4]["overview"],
        count_8 = r.get("counter8"),

        # Rambo
        poster_9 = data2["results"][8]["poster_path"],
        title_9 = data2["results"][8]["original_title"],
        average_9 = data2["results"][8]["vote_average"],
        overview_9 = data2["results"][8]["overview"],
        count_9 = r.get("counter9"),

        # Aladdin
        poster_10 = data2["results"][9]["poster_path"],
        title_10 = data2["results"][9]["original_title"],
        average_10 = data2["results"][9]["vote_average"],
        overview_10 = data2["results"][9]["overview"],
        count_10 = r.get("counter10"),

        )

@app.route("/test") # info page
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=False)
