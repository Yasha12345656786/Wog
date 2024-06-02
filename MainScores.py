from flask import render_template, Flask
import os


def score_server():
    try:
        app = Flask(__name__, template_folder='./html')

        @app.route("/")
        def players_points():
            scores = []
            with open("Scores.txt") as f:
                scores = [line.rstrip('\n') for line in f]
            return render_template('PlayersPoints.html', scores=scores, length=len(scores))

        app.run(debug=True)
    except Exception as errors:
        app = Flask(__name__, template_folder='./html')

        @app.route("/")
        def players_points():
            return render_template('PlayersPointsErr.html', errors=errors)

        app.run(debug=True)


score_server()
