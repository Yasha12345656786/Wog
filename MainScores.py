from flask import render_template, Flask


def score_server():
    try:
        app = Flask(__name__, template_folder='templates/')

        @app.route("/")
        def players_points():
            return render_template('PlayersPoints.html')

        app.run(debug=True)
    except Exception as e:
        app = Flask(__name__, template_folder='templates/')

        @app.route("/")
        def players_points():
            return render_template('PlayersPointsErr.html')
