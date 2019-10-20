from flask import Flask, render_template
import requests, sys, json, redis

# url variables
url1 = "https://api.themoviedb.org/3/trending/movie/week?api_key=231a360ba06b66e4033e0580923144b1"
url2 = "https://api.themoviedb.org/3/discover/movie?api_key=231a360ba06b66e4033e0580923144b1&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
url3 = "https://api.themoviedb.org/3/movie/upcoming?api_key=231a360ba06b66e4033e0580923144b1&language=en-US&page=1"

# Handles requests
try:
    html_content1 = requests.get(url1).text
except:
    print("unable to get {url1}")
    sys.exit(1)
try:
    html_content2 = requests.get(url2).text
except:
    print("unable to get {url2}")
    sys.exit(1)
try:
    html_content3 = requests.get(url3).text
except:
    print("unable to get {url3}")
    sys.exit(1)

# Creates Redis host and variable
r = redis.Redis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)

# with open ("trending_movies2.json", "w+") as f:
#     json.dump(html_content1, f, sort_keys=True, indent=4, separators=(",", ": "))

app = Flask(__name__)

trending = json.loads(html_content1)
discover = json.loads(html_content2)
upcoming = json.loads(html_content3)

# with open("trending_movies.json", "w+") as f:
#     json.dump(html_content1, f, sort_keys=True, indent=4)

# with open("trending_movies.json", "w+") as f:
#     json.dump(soup1, f, sort_keys=True, indent=4)

# r.set(html_content1)

# print(r.get("title"))


# Reads json files to pass arguments
# with open("trending_movies.json", "r", encoding="utf8") as my_file:
#     data = json.load(my_file) 
# with open("discover_movies.json", "r", encoding="utf8") as my_f:
#     data2 = json.load(my_f) 

# Initializes counters using redis at base values from request.
#------------------------------------------------------------------------------------
r.set("poster1", trending["results"][0]["poster_path"])
r.set("title1", trending["results"][0]["original_title"])
r.set("average1", trending["results"][0]["vote_average"])
r.set("overview1", trending["results"][0]["overview"])
r.set("counter1", trending["results"][0]["vote_count"])

r.set("poster2", trending["results"][1]["poster_path"])
r.set("title2", trending["results"][1]["original_title"])
r.set("average2", trending["results"][1]["vote_average"])
r.set("overview2", trending["results"][1]["overview"])
r.set("counter2", trending["results"][1]["vote_count"])

r.set("poster3", trending["results"][2]["poster_path"])
r.set("title3", trending["results"][2]["original_title"])
r.set("average3", trending["results"][2]["vote_average"])
r.set("overview3", trending["results"][2]["overview"])
r.set("counter3", trending["results"][2]["vote_count"])

r.set("poster4", trending["results"][3]["poster_path"])
r.set("title4", trending["results"][3]["original_title"])
r.set("average4", trending["results"][3]["vote_average"])
r.set("overview4", trending["results"][3]["overview"])
r.set("counter4", trending["results"][3]["vote_count"])

r.set("poster5", trending["results"][4]["poster_path"])
r.set("title5", trending["results"][4]["original_title"])
r.set("average5", trending["results"][4]["vote_average"])
r.set("overview5", trending["results"][4]["overview"])
r.set("counter5", trending["results"][4]["vote_count"])

#------------------------------------------------------------------------------------
r.set("poster6", discover["results"][3]["poster_path"])
r.set("title6", discover["results"][3]["original_title"])
r.set("average6", discover["results"][3]["vote_average"])
r.set("overview6", discover["results"][3]["overview"])
r.set("counter6", discover["results"][3]["vote_count"])

r.set("poster7", discover["results"][6]["poster_path"])
r.set("title7", discover["results"][6]["original_title"])
r.set("average7", discover["results"][6]["vote_average"])
r.set("overview7", discover["results"][6]["overview"])
r.set("counter7", discover["results"][6]["vote_count"])

r.set("poster8", discover["results"][7]["poster_path"])
r.set("title8", discover["results"][7]["original_title"])
r.set("average8", discover["results"][7]["vote_average"])
r.set("overview8", discover["results"][7]["overview"])
r.set("counter8", discover["results"][7]["vote_count"])

r.set("poster9", discover["results"][9]["poster_path"])
r.set("title9", discover["results"][9]["original_title"])
r.set("average9", discover["results"][9]["vote_average"])
r.set("overview9", discover["results"][9]["overview"])
r.set("counter9", discover["results"][9]["vote_count"])

r.set("poster10", discover["results"][10]["poster_path"])
r.set("title10", discover["results"][10]["original_title"])
r.set("average10", discover["results"][10]["vote_average"])
r.set("overview10", discover["results"][10]["overview"])
r.set("counter10", discover["results"][10]["vote_count"])

#------------------------------------------------------------------------------------
r.set("poster11", upcoming["results"][1]["poster_path"])
r.set("title11", upcoming["results"][1]["original_title"])
r.set("average11", upcoming["results"][1]["vote_average"])
r.set("overview11", upcoming["results"][1]["overview"])
r.set("counter11", upcoming["results"][1]["vote_count"])

r.set("poster12", upcoming["results"][2]["poster_path"])
r.set("title12", upcoming["results"][2]["original_title"])
r.set("average12", upcoming["results"][2]["vote_average"])
r.set("overview12", upcoming["results"][2]["overview"])
r.set("counter12", upcoming["results"][2]["vote_count"])

r.set("poster13", upcoming["results"][3]["poster_path"])
r.set("title13", upcoming["results"][3]["original_title"])
r.set("average13", upcoming["results"][3]["vote_average"])
r.set("overview13", upcoming["results"][3]["overview"])
r.set("counter13", upcoming["results"][3]["vote_count"])

r.set("poster14", upcoming["results"][4]["poster_path"])
r.set("title14", upcoming["results"][4]["original_title"])
r.set("average14", upcoming["results"][4]["vote_average"])
r.set("overview14", upcoming["results"][4]["overview"])
r.set("counter14", upcoming["results"][4]["vote_count"])

r.set("poster15", upcoming["results"][5]["poster_path"])
r.set("title15", upcoming["results"][5]["original_title"])
r.set("average15", upcoming["results"][5]["vote_average"])
r.set("overview15", upcoming["results"][5]["overview"])
r.set("counter15", upcoming["results"][5]["vote_count"])

# Handles incr or decr for individual counts
# if(increase1):
#     r.incr("counter1")
# Tecnicamente así se haría pero en todos los sitios que he visitado dice que necesito AJAX para afectar Redis.

@app.route("/") # info page
def info():
    return render_template(
        "page.html",
        #--------------------------------------------------------------Trending-----------
        # Spiderman
        poster_1 = r.get("poster1"),
        title_1 = r.get("title1"),
        average_1 = r.get("average1"),
        overview_1 = r.get("overview1"),
        count_1 = r.get("counter1"),
        
        # The Lion King
        poster_2 = r.get("poster2"),
        title_2 = r.get("title2"),
        average_2 = r.get("average2"),
        overview_2 = r.get("overview2"),
        count_2 = r.get("counter2"),

        # El Camino
        poster_3 = r.get("poster3"),
        title_3 = r.get("title3"),
        average_3 = r.get("average3"),
        overview_3 = r.get("overview3"),
        count_3 = r.get("counter3"),

        # Toy Story 4
        poster_4 = r.get("poster4"),
        title_4 = r.get("title4"),
        average_4 = r.get("average4"),
        overview_4 = r.get("overview4"),
        count_4 = r.get("counter4"),

        # Joker
        poster_5 = r.get("poster5"),
        title_5 = r.get("title5"),
        average_5 = r.get("average5"),
        overview_5 = r.get("overview5"),
        count_5 = r.get("counter5"),

        #--------------------------------------------------------------Discover-----------
        # Skipped over any movies that have already been used.
        # Maleficent
        poster_6 = r.get("poster6"),
        title_6 = r.get("title6"),
        average_6 = r.get("average6"),
        overview_6 = r.get("overview6"),
        count_6 = r.get("counter6"),

        # Gemini Man
        poster_7 = r.get("poster7"),
        title_7 = r.get("title7"),
        average_7 = r.get("average7"),
        overview_7 = r.get("overview7"),
        count_7 = r.get("counter7"),

        # Fast and Furious
        poster_8 = r.get("poster8"),
        title_8 = r.get("title8"),
        average_8 = r.get("average8"),
        overview_8 = r.get("overview8"),
        count_8 = r.get("counter8"),

        # IP 4
        poster_9 = r.get("poster9"),
        title_9 = r.get("title9"),
        average_9 = r.get("average9"),
        overview_9 = r.get("overview9"),
        count_9 = r.get("counter9"),

        # Aladdin
        poster_10 = r.get("poster10"),
        title_10 = r.get("title10"),
        average_10 = r.get("average10"),
        overview_10 = r.get("overview10"),
        count_10 = r.get("counter10"),

        #--------------------------------------------------------------Discover-----------
        # Zombieland
        poster_11 = r.get("poster11"),
        title_11 = r.get("title11"),
        average_11 = r.get("average11"),
        overview_11 = r.get("overview11"),
        count_11 = r.get("counter11"),

        # Terminator
        poster_12 = r.get("poster12"),
        title_12 = r.get("title12"),
        average_12 = r.get("average12"),
        overview_12 = r.get("overview12"),
        count_12 = r.get("counter12"),

        # The Addams Family
        poster_13 = r.get("poster13"),
        title_13 = r.get("title13"),
        average_13 = r.get("average13"),
        overview_13 = r.get("overview13"),
        count_13 = r.get("counter13"),

        # Hustlers
        poster_14 = r.get("poster14"),
        title_14 = r.get("title14"),
        average_14 = r.get("average14"),
        overview_14 = r.get("overview14"),
        count_14 = r.get("counter14"),

        # The Lighthouse
        poster_15 = r.get("poster15"),
        title_15 = r.get("title15"),
        average_15 = r.get("average15"),
        overview_15 = r.get("overview15"),
        count_15 = r.get("counter15"),

        )

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
