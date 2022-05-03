import flask

app = flask.Flask(__name__)

show = ["Ben 10", "Hunter x Hunter", "Naruto", "The Office"]


@app.route("/")
def start():
    return flask.render_template("index.html", shows=show)


app.run()
