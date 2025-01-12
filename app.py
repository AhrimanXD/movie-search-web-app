from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
        response = requests.get(url)
        data = response.json()
        movies = data["results"]
        return render_template("search_results.html", movies=movies)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
