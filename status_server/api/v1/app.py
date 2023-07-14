#!/usr/bin/python3
"""
Web server 
"""
from .views.index import status
from flask import Flask, jsonify, make_response
import socket

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

# Register the status function as route.
app.add_url_rule('/api/v1/status', view_func=status, methods=['GET'])

if __name__ == "__main__":
    """python -m api.v1.app"""
    port = 5000 # Default port
    try:
        # Attempt to create a socket connection if default port is already in use
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", port))
        sock.close()
    except socket.error:
        # If port is already in use, switch to an alternative port(e.g. 8080)
        port = 8080

    app.run(host="0.0.0.0", port=port, threaded=True)
