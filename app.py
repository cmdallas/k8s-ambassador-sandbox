from flask import Flask, jsonify, abort, request
import urllib.request, json, os
from github import Github


app = Flask(__name__)

DEBUG = os.environ["DEBUG"]
GITHUB_TOKEN = os.environ["GITHUB_READ_TOKEN"]
HOST = os.environ["HOST"]
PORT = os.environ["PORT"]

g = Github(GITHUB_TOKEN)


@app.route("/")
def get_repos():
    r = []

    try:
        args = request.args
        n = int(args["n"])
        l = args["l"]
    except (ValueError, LookupError) as e:
        abort(jsonify(error="Please provide 'n' and 'l' parameters"))

    repositories = g.search_repositories(query="language:" + l)[:n]

    try:
        for repo in repositories:
            with urllib.request.urlopen(repo.url) as url:
                data = json.loads(url.read().decode())
            r.append(data)
        return jsonify({"repos": r, "status": "ok"})
    except IndexError as e:
        return jsonify({"repos": r, "status": "ko"})


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
