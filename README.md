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

* Imported the status function from the `views.index module`.
* Added the `import` statement for the `socket` module.
* Updated the port configuration to use a default port of 5000.
* Added code to check if the default port is already in use and switch to an alternative port (e.g., 8080).
* Added initilization file within sub-directories to define the package's namespace and perform any necessary configurations.
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
You should see the server running on `http://0.0.0.0:<port>/*`. The actual port used will depend on whether the default port is available or an alternative port had to be used.

To test the server status, you can use the following command:
```bash
root@f82226a41eb6: curl -XGET http://localhost:<port>/api/v1/status
{"status":"OK"}
```
Please note that you need to replace <port> with the actual port number where the server is running.


## Task[1]: My square
I love geometry!

Look [my square](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/blob/master/square.py), it’s perfect? No? Should I change something?

### Solution
* In ~/Fix_My_Code_Challenge/square.py
```python
#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width + self.height) * 2

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
```
Here are the changes made:

* Renamed the class `square` to `Square` (following Python naming conventions).
* Added proper indentation to the class and its methods.
* Changed the method name `PermiterOfMySquare` to `perimeter_of_my_square` (following Python naming conventions).
* Fixed the `__init__` method to initialize the width and height attributes correctly.
* Fixed the calculation of the area in the `area_of_my_square` method.
* Fixed the calculation of the perimeter in the `perimeter_of_my_square` method.

### Output
To execute the corrected code, you can save it in a file named `square.py` and run it using the `python3` command.
```bash
python3 square.py
```

This will execute the code and display the output:
```bash
12/9
108
42
```
The first line represents the string representation of the `Square` object, followed by the calculated area and perimeter of the square.


## Task[2]: User Model
I’m running into a serious problem!

I just start my OOP project and nothing works…

Could you help me please? My code is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/blob/master/user.py).

Thank you!

### Solution
Fixing the User Class

The following changes were made to correct the User class code:
```python
#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email = None

    @property
    def email(self):
        """ Documentation """
        return self.__email
    
    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
```
* The decorator `@email.setter` was moved below the `@property` decorator.
* The `email` setter method now correctly sets the value of `self.__email` attribute when assigning a new email value.
* Added a type check to ensure that the assigned email value is a string. If the value is not a string, a `TypeError` is raised.

### Output
After making the above changes, you can run the following command to execute the code:
```bash
root@f82226a41eb6:~/Fix_My_Code_Challenge# python3 user.py
john@snow.com
```
The code creates a User object, assigns the email "<u>"john@snow.com"</u>"  to it, and then prints the email value.

The corrected code now properly sets and retrieves the email value without any errors.
