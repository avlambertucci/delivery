from flask import Blueprint, request, render_template

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
  return render_template("index.html")