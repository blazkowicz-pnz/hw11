from utils import load_candidates_from_json
from settings import path
from flask import Flask
from utils import get_candidate
from utils import get_candidates


app = Flask(__name__)
@app.route("/")
def page_index():


app.run()


