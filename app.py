from flask import Flask
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

    return "<h1>Not found </h1>"



###3 #######################################################use templates
@app.route("/landing")
def land():
    return  render_template("landing.html")


# base template , then inherit --> persons --> return with response --> send it to the template

@app.route("/persons")
def persons():
    persons = [
        {"id": 1, "name": "Mazen", "image": "pic1.png", "grade": 100},
        {"id": 2, "name": "Safa", "image": "pic2.png", "grade": 100},
        {"id": 3, "name": "Israa", "image": "pic3.png", "grade": 100},
        {"id": 4, "name": "Omar", "image": "pic4.png", "grade": 100},
        {"id": 5, "name": "Helana", "image": "pic4.png", "grade": 100},
    ]
    return render_template("persons/index.html", name='noha', track="python", persons = persons)


@app.route("/persons/<int:id>", endpoint="person.show")
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
        return render_template("persons/show.html", person=person[0])

    return "<h1>Not found </h1>"



# we need to start from terminal
# open it
# export FLASK_APP=app
# export DEBUG=True
# then run flask run

# start server
if __name__ == "__main__":
    app.run(debug=True) # start development server for your flask app
