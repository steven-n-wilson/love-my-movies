from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests, sys, csv, json, re, os, urllib.request

# url variables
url = "http://ufm.edu/Portal"

# print if needed, gets too noisy
# print(soup.prettify())

print("==================================================================")
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print("unable to get {url}")
    sys.exit(1)
print("1. Portal")
soup = BeautifulSoup(html_content, "html.parser")
# Print Title
title = soup.title.string
print("GET the title and print it:", title)


app = Flask(__name__)

@app.route("/") # info page
def info():
    return render_template("page.html")
    
if __name__ == "__main__":
    app.run(debug=True)
