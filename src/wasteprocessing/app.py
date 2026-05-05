import os
import threading
from dataclasses import asdict
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request, send_from_directory

from wasteprocessing.browser import open_url_in_chromium
from wasteprocessing.database import init_db, list_reports

ROOT = Path(__file__).resolve().parent.parent.parent
GLOBAL_ENV = Path.home() / ".env"
LOCAL_ENV = ROOT / ".env"
DATA_PATH = ROOT / "data" / "waste_research.db"
WEB_ROOT = ROOT / "web"

load_dotenv(GLOBAL_ENV, override=False)
load_dotenv(LOCAL_ENV, override=True)
init_db(DATA_PATH)

app = Flask(__name__, static_folder=str(WEB_ROOT), static_url_path="")


@app.route("/")
def index():
    return send_from_directory(WEB_ROOT, "index.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    results = []

    for report in list_reports(DATA_PATH):
        haystack = " ".join([
            report.agent,
            report.category,
            report.title,
            report.summary,
            report.details,
            report.source,
        ]).lower()
        if not query or query in haystack:
            results.append(asdict(report))

    return jsonify({"query": query, "count": len(results), "results": results})


@app.route("/favicon.ico")
def favicon():
    return redirect("/", code=302)


def open_default_browser() -> None:
    url = "http://127.0.0.1:5000/"
    if open_url_in_chromium(url):
        print(f"Opened browser at {url}")
    else:
        print(f"Unable to locate Chromium-for-Testing; open the URL manually: {url}")


if __name__ == "__main__":
    timer = threading.Timer(1.0, open_default_browser)
    timer.daemon = True
    timer.start()
    app.run(host="127.0.0.1", port=5000, debug=False)
