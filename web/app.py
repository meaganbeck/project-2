"""
Meagan Beckstrand's Flask API.
"""

from flask import Flask, abort, send_from_directory, render_template, request
import os.path
import configparser
#use send_from_directory to print errors?

app = Flask(__name__)

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break
    
    if config_path is None:
        raise RuntimeError("Configur")
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]
debug = config["SERVER"]["DEBUG"]

@app.route("/<path:request>") #check name below?
def hello(request):
    path = '/project-2/web/pages/'# + request
    filename = request
    if len(request) > 1:
        if ".." in request or "~" in request:
            abort(403)
        elif os.path.isfile(request):
             return send_from_directory('pages/', request), 200
            #return send_from_directory('pages/', 'trivia.html')
        else:
            abort(404)


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403
@app.errorhandler(404)
def dne(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 5001)
