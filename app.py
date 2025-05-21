from flask import Flask, render_template, request
import requests
import Levenshtein
import os

app = Flask(__name__)

def get_random_wikipedia_article():
    """
    Fetch a random Wikipedia article title and its first paragraph using Wikipedia's API.
    """
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "grnnamespace": 0,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }
    response = S.get(url=URL, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    title = page["title"]
    paragraph = page.get("extract", "")
    return title, paragraph

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        real_paragraph = request.form["real_paragraph"]
        guess = request.form["guess"]
        similarity = Levenshtein.ratio(guess.strip().lower(), real_paragraph.strip().lower())
        return render_template("result.html",
                               title=title,
                               real_paragraph=real_paragraph,
                               guess=guess,
                               similarity=round(similarity * 100, 2))
    else:
        title, paragraph = get_random_wikipedia_article()
        return render_template("index.html", title=title, real_paragraph=paragraph)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
