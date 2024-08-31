

from flask import Flask, abort
from flask import render_template


# starting the application inside this script use, the __name__ entry point for it
app = Flask(__name__)

# adding my first route
@app.route("/")  # decorator
def hello_world():
    return "<h1 style='color:red;text-align:center'>Hello, World!</h1>"

@app.route("/home/<user>")
def home(user):
    return  user

@app.route("/profile/<int:id>")
def profile(id):  # view function
    # return of view must be http response --> must be string , list, dict
    return f"{id}"


@app.route("/students")
def students():
    students= [
        {"id":1, "name":"Mazen", "image":"pic1.png", "grade":100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]

    return students

@app.route("/students/<int:id>")
def student_details(id):
    students = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]

    student= list(filter(lambda std: std["id"]==id , students))# filter object casted to list
    # print(list(student))
    if student:
        return student[0]

    # return "<h1>Not found </h1>"
    abort(404)



###3 #######################################################use templates
@app.route("/landing")
def land():
    return  render_template("landing.html")


# base template , then inherit --> persons --> return with response --> send it to the template

@app.route("/persons", endpoint='persons.index')
def persons():
    persons = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]
    return render_template("persons/index.html", name='noha', track="python", persons = persons)


@app.route("/persons/<int:id>", endpoint="persons.show")
def person_profile(id):
    persons = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]

    person= list(filter(lambda p: p["id"]==id , persons))# filter object casted to list
    # print(list(student))
    if person:
        return render_template("persons/show.html",
                               person=person[0], image=f"persons/{person[0]['image']}")

    # return "<h1>Not found </h1>"
    abort(404)



# we need to start from terminal
# open it
# export FLASK_APP=app
# then run==> flask run --debug

# to get more info about routes register in your app
"""
    # use command 
    export FLASK_APP=app
    flask shell 
    
    in flask shell
    app.url_map
    app.url_map
    # serving static files ---> inside folder static 
    Map([<Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
    
    
           route    supported method    ---> endpoint  ==== function 
     <Rule '/' (HEAD, GET, OPTIONS) -> hello_world>,
     <Rule '/home/<user>' (HEAD, GET, OPTIONS) -> home>,
     <Rule '/profile/<id>' (HEAD, GET, OPTIONS) -> profile>,
     <Rule '/students' (HEAD, GET, OPTIONS) -> students>,
     <Rule '/students/<id>' (HEAD, GET, OPTIONS) -> student_details>,
     <Rule '/landing' (HEAD, GET, OPTIONS) -> land>,
     <Rule '/persons' (HEAD, GET, OPTIONS) -> persons>,
     <Rule '/persons/<id>' (HEAD, GET, OPTIONS) -> persons.show>])


# before using flask_shell  --> install package ? flask-ipython-shell
pip install flask-shell-ipython
"""

### view --> 404 not found
# define new route --> 404

@app.errorhandler(404)
def error_not_found(error):
    # return "<h1> error </h1>"
    return  render_template("404.html")


##########################33 **************** split route from view function *********************************
def users():
    return render_template("users.index.html")

# I need route for this view ??
app.add_url_rule("/users", view_func=users, endpoint='users.index')




# start server
if __name__ == "__main__":
    app.run(debug=True) # start development server for your flask app
