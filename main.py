from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skills
from flask import Flask, render_template
from settings import path


app = Flask(__name__)
@app.route("/")
def page_index():
    candidates = load_candidates_from_json(path)
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidate(uid)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skills/<skills_name>")
def skill(skills_name):
    candidates = get_candidates_by_skills(skills_name)
    return render_template("skills.html", candidates=candidates, skill=skills_name)


app.run()


