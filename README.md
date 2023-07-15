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

* In app.py
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
* Imported the `status` function from the `views.index` module.
* Added the `import` statement for the `socket` module.
* Updated the `port` configuration to use a default `port` of 5000.
* Added code to check if the default `port` is already in use and switch to an alternative `port`(e.g., 8080).
* Added initilization file within sub-directories to define the package's namespace and perform any necessary configurations.
* Started the Flask application with the updated `host` and `port`.

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
You should see the server running on `http://0.0.0.0:<port>/*`. The actual `port` used will depend on whether the default `port` is available or an alternative port had to be used.

To test the server status, you can use the following command:
```python
root@f82226a41eb6: curl -XGET http://localhost:8080/api/v1/status
{"status":"OK"}
```
Please note that you need to replace with the actual `port` number where the server is running.
<br><br>
## Task[1]: My square
I love geometry!

Look [my square](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/blob/master/square.py), it’s perfect? No? Should I change something?

### Solution
* In square.py
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
To execute the corrected code, you can save it in a file named square.py and run it using the python3 command.
```bash
python3 square.py
```

This will execute the code and display the output:
```bash
12/9
108
42
```
The first line represents the string representation of the Square object, followed by the calculated area and perimeter of the square.
<br><br>

## Task[2]: User Model
I’m running into a serious problem!

I just start my OOP project and nothing works…

Could you help me please? My code is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/blob/master/user.py).

Thank you!

### Solution
Fixing the User Class

The following changes were made to correct the User class code:
* In user.py
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
````
The code creates a User object, assigns the email "<u>john@snow.com</u>" to it, and then prints the email value.

The corrected code now properly sets and retrieves the email value without any errors.
<br><br>

## Task[3]: Blog access

I finished and deployed my Rails blog but people are contacting me because they can’t access any of my blog posts… Weird, it works for me…

Could you take a look and fix it? My code base is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/tree/master/blog).

Also, when you’re done, could you add a new feature please?

I would like to add a boolean online for each Post object with a default value true. With this boolean, I will be able to hide/show some blog posts from the listing. I will also need a way to change this boolean in the Post#edit route. Could you do this for me?

Thank you!

### Solution

* Installation:
This can be found in the blog/README.md file

In README.md

```markdown
# README

Blog application:

## How to install it:

- `$ gem install bundler`
- `$ bundle install`
- `$ rails db:migrate RAILS_ENV=development`

## How to run the server

`$ rails s -b 0.0.0.0 -p 5000`

## How to start the rails console

`$ rails c`

## Admin account

- email: `hbtn@hbtn.io`
- password: `toto1234`
```

Examine the routes and controller methods:
* Open the `routes.rb` file located at `config/routes.rb`.

```ruby
Rails.application.routes.draw do
  devise_for :users
  devise_for :installs

  resources :posts do
    resources :comments
  end

  root "posts#index"

  get '/about', to: 'pages#about'
end
```

* Look for the routes related to blog posts usually defined using the resources keyword or individually.
* Ensure that the routes are defined correctly with appropriate HTTP methods `GET`, `POST`, `PATCH`, `DELETE` and point to the correct controller actions.
<br>

Verify controller actions:
* Open the `PostsController` file located at `app/controllers/posts_controller.rb`.

```ruby
class PostsController < ApplicationController
  before_action :authenticate_user!, except: [:index]

  def index
    @posts = Post.all.order('created_at DESC')
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new(post_params)

    if @post.save
      redirect_to @post
    else
      render 'new'
    end
  end

  def show
    @post = Post.find(params[:id])
  end

  def edit
    @post = Post.find(params[:id])
  end

  def update
    @post = Post.find(params[:id])

    if @post.update(post_params)
      redirect_to @post
    else
      render 'edit'
    end
  end

  def destroy
    @post = Post.find(params[:id])
    @post.destroy

    redirect_to posts_path
  end

  private

  def post_params
    params.require(:post).permit(:title, :body)
  end
end
```

* Check the controller methods related to displaying blog posts, such as `index`, `show`, and `new`.
* Make sure they are implemented correctly.
* Ensure that any necessary instance variables are set and the correct views are rendered as shown from line 1 - 6.
<br>

Verify views:
* Open the `views` associated with displaying blog posts, such as `index.html.erb` and `show.html.erb`, located at `app/views/posts/`.
* Check that the views contain the necessary HTML and dynamic content to display the blog posts.
* Ensure that any required instance variables are correctly referenced in the views.

In **index.html.erb**

```html
<h1>Blog Posts</h1>

<% @posts.each do |post| %>
  <h2><%= post.title %></h2>
  <p><%= post.body %></p>
<% end %>
```

By carefully reviewing the `routes`, `controller` methods, and `views`, you can identify any potential issues that may be causing the access problem for your blog posts.

### Output
Execute the ruby on rails command to spring up the server:

```bash
rails server
```
OR
```bash
rails s
```
Server starts without errors.
```bash
Puma starting in single mode...
* Version 3.12.6 (ruby 2.7.6-p219), codename: Llamas in Pajamas
* Min threads: 5, max threads: 5
* Environment: development
* Listening on tcp://localhost:3000
Use Ctrl-C to stop

```
<br>
Execute the `curl` command with the Hostname or IP Address and default port 3000 as arguments to find out if connection can be established.
<br>

```bash
root@f82226a41eb6:~/Fix_My_Code_Challenge# curl http://0.0.0.0:3000
<!DOCTYPE html>
<html>
  <head>
    <title>RailsBlog</title>
    <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="t8m311FoVhs2Cpqa+KVlr3ApWLrWmPf9lkebbHa+UGiLMGssu4NDZEV5s99MZbHUwmDT5sa+1Ad1+/QalAvVbQ==" />
    <link rel="stylesheet" media="screen" href="/assets/_normalize.self-5515d8e5c01fc121cc3c031106ce82bd395826d1e1593b4bc58f2b1d53b78fa0.css?body=1" />
<link rel="stylesheet" media="screen" href="/assets/comments.self-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.css?body=1" />
<link rel="stylesheet" media="screen" href="/assets/posts.self-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.css?body=1" />
<link rel="stylesheet" media="screen" href="/assets/application.self-492fcbe179244e2a0b1374697cc7d5af5a0d65c090745cb280d75439d759d322.css?body=1" />
<link rel="stylesheet" media="screen" href="http://fonts.googleapis.com/css?family=Raleway:400,700" />
    <link rel="stylesheet" media="all" href="/assets/_normalize.self-5515d8e5c01fc121cc3c031106ce82bd395826d1e1593b4bc58f2b1d53b78fa0.css?body=1" data-turbolinks-track="reload" />
<link rel="stylesheet" media="all" href="/assets/comments.self-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.css?body=1" data-turbolinks-track="reload" />
<link rel="stylesheet" media="all" href="/assets/posts.self-e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.css?body=1" data-turbolinks-track="reload" />
<link rel="stylesheet" media="all" href="/assets/application.self-492fcbe179244e2a0b1374697cc7d5af5a0d65c090745cb280d75439d759d322.css?body=1" data-turbolinks-track="reload" />
    <script src="/assets/jquery.self-bd7ddd393353a8d2480a622e80342adf488fb6006d667e8b42e4c0073393abee.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/jquery_ujs.self-784a997f6726036b1993eb2217c9cb558e1cbb801c6da88105588c56f13b466a.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/turbolinks.self-c5acd7a204f5f25ce7a1d8a0e4d92e28d34c9e2df2c7371cd7af88e147e4ad82.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/action_cable.self-17ebe4af84895fa064a951f57476799066237d7bb5dc4dc351a8b01cca19cce9.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/cable.self-6e0514260c1aa76eaf252412ce74e63f68819fd19bf740595f592c5ba4c36537.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/comments.self-877aef30ae1b040ab8a3aba4e3e309a11d7f2612f44dde450b5c157aa5f95c05.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/posts.self-877aef30ae1b040ab8a3aba4e3e309a11d7f2612f44dde450b5c157aa5f95c05.js?body=1" data-turbolinks-track="reload"></script>
<script src="/assets/application.self-b89234cf2659d7fedea75bca0b8d231ad7dfc2f3f57fcbaf5f44ed9dc384137b.js?body=1" data-turbolinks-track="reload"></script>
  </head>

  <body>
    <div id="sidebar">
      <div id="logo">
        <a href="/">
          <img src="/assets/logo-a739645d849f66cd3063d65f31c0dfa5f1b0d9174bca4e2a549aa2baa09c0426.svg" alt="Logo" />
</a>      </div>

      <ul>
        <li class="category">Website</li>
        <li><a href="/">Blog</a></li>
        <li><a href="/about">About</a></li>
      </ul>

        <p class="sign_in"><a href="/users/sign_in">Admin Login</a></p>
    </div>

    <div id="main_content">
      <div id="header">
          <p>All Posts</p>

      </div>


      <div class="post_wrapper">
  <h2 class="title"><a href="/posts/2">80% of batch 01 students are already working in the tech industry as software engineers. WOOT!</a></h2>
  <p class="date">September, 14, 2017</p>
</div>
<div class="post_wrapper">
  <h2 class="title"><a href="/posts/1">Summer 2017 | Holberton Coding Camp</a></h2>
  <p class="date">September, 14, 2017</p>
</div>


    </div>
  </body>
</html>
```
<br>

Check the server's status for success or failure in connection establishment:
<br>

```bash
root@f82226a41eb6:~/Fix_My_Code_Challenge/blog/config# rails server
Puma starting in single mode...
* Version 3.12.6 (ruby 2.7.6-p219), codename: Llamas in Pajamas
* Min threads: 5, max threads: 5
* Environment: development
* Listening on tcp://localhost:3000
Use Ctrl-C to stop
Started GET "/" for 127.0.0.1 at 2023-07-14 19:32:02 -0700
/root/.rbenv/versions/2.7.6/lib/ruby/gems/2.7.0/gems/activerecord-5.0.1/lib/active_record/connection_adapters/sqlite3_adapter.rb:27: warning: rb_check_safe_obj will be removed in Ruby 3.0
  ActiveRecord::SchemaMigration Load (0.1ms)  SELECT "schema_migrations".* FROM "schema_migrations"
Processing by PostsController#index as */*
  Rendering posts/index.html.erb within layouts/application
  Post Load (0.1ms)  SELECT "posts".* FROM "posts" ORDER BY created_at DESC
  Rendered posts/index.html.erb within layouts/application (198.2ms)
Completed 200 OK in 1797ms (Views: 1695.5ms | ActiveRecord: 0.5ms)

```

From the output it shows a status code of 200 indicating that the connection was successfully established.
