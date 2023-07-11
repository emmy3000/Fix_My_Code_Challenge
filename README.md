# Project (0x01. Fix my code)



## Task[0]: Server status

I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).

But I don’t know why it’s not working…

Could you look at it and fix it please?

My code is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/tree/master/status_server/).
<br>
<br>


## SOLUTION

### Fixing the Status Server
The following changes were made to correct the source code of the status server:
<br>

**In /api/v1/app.py file**
```
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
    app.run(host="0.0.0.0", port=8080, threaded=True)
```

* The import statement was switched from `from api.v1.views import app_views` to `from views.index import status`.
* The blueprint registration `app.register_blueprint(app_views)` was removed.
* The server was updated to run on `port 8080` instead of `port 5000`.
<br>

**In /api/v1/views/__init__.py**
```
#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from .index import *
```

* he import statement `from api.v1.views.index import *` was changed to `from .index import *`.
<br>


**In /api/v1/views/index.py**
```
#!/usr/bin/python3
""" Index view
"""
from flask import jsonify
from . import app_views

@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
```

* The import statement `from api.v1.views import app_views` was changed to `from . import app_views`.
<br>

### OUTPUT
```
root@f82226a41eb6:~/Fix_My_Code_Challenge/status_server/api/v1# python -m api.v1.app
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ...
```
```
root@f82226a41eb6:~/Fix_My_Code_Challenge/status_server/api/v1# curl -XGET http://0.0.0.0:5000/api/v1/status
{"error": "Not found"}
root@f82226a41eb6:~/Fix_My_Code_Challenge/status_server/api/v1#
```
