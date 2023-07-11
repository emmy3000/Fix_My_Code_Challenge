#!/usr/bin/python3
"""
Web server 
"""
from views.index import status
from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=8080, threaded=True)
