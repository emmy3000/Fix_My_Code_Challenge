# Project (0x01. Fix my code)
<br>
## Task[0]: Server status

I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).

But I don’t know why it’s not working…

Could you look at it and fix it please?

My code is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/tree/master/status_server/).

### Solution
* Fixing the Status Server

The following changes were made to correct the source code of the status server:

* In /api/v1/app.py file
```python
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

# Register the status function as a route.
app.add_url_rule('/api/v1/status', view_func=status, methods=['GET'])

if __name__ == "__main__":
    """python -m api.v1.app"""
    port = 5000  # Default port
    try:
        # Attempt to create a socket connection if the default port is already in use
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", port))
        sock.close()
    except socket.error:
        # If the port is already in use, switch to an alternative port (e.g., 8080)
        port = 8080

    app.run(host="0.0.0.0", port=port, threaded=True)
```

* Imported the status function from the views.index module.
* Added the import statement for the socket module.
* Updated the port configuration to use a default port of 5000.
* Added code to check if the default port is already in use and switch to an alternative port (e.g., 8080).
* Started the Flask application with the updated host and port.

### Output

After making the above changes, you can run the following command to start the server:
```bash
root@f82226a41eb6:~/Fix_My_Code_Challenge/status_server# python3 -m api.v1.app
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.6:8080 (Press CTRL+C to quit)
127.0.0.1 - - [14/Jul/2023 12:29:50] "GET /api/v1/status HTTP/1.1" 200 -
```
You should see the server running on http://0.0.0.0:<port>/. The actual port used will depend on whether the default port is available or an alternative port had to be used.

To test the server status, you can use the following command:
```bash
root@f82226a41eb6: curl -XGET http://localhost:<port>/api/v1/status
{"status":"OK"}
```
Please note that you need to replace <port> with the actual port number where the server is running.
