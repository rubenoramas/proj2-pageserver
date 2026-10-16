import os
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/<path:name>")
def serve(name):
    if ".." in name or "//" in name or name.startswith("~"):
        abort(403)
    if not os.path.isfile(os.path.join("templates", name)):
        abort(404)
    return render_template(name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
