from crypt import methods

from flask import Flask, abort, url_for, request, redirect
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

###############################################################################
############# **** connection with databases ***********
# flask
# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/

from flask_sqlalchemy import SQLAlchemy

# define db url

# initialize instance for my db . ==> connect sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# "sqlite:///test.db"
# sqlite://generate db in projectdit /database.db
# http://url

# connect app with db ?
db = SQLAlchemy(app) # connect db with flask app


##
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String(250))
    salary = db.Column(db.Integer)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"employees/{self.image}")

    @property
    def delete_url(self):
        return  url_for("employees.delete", employee=self.id)

    @property
    def show_url(self):
        return url_for("employees.show", employee=self.id)


# ask app to connect to db --> and create table
# in flask shell  --> db.create_all()
# create table employees
"""
    create new object
    go to flask shell
    1- import model
    from app import Employee
    2- create new object
    emp = Employee()
    emp.name='noha'
    emp.image='pic1.png'
    emp.salary = 4455
    # 3- save object 
    db.session.add(emp)
    db.session.commit()

    # show all objects ?
    # sqlalchemy use ? models functions to run dml on objects 
    1- select * from employees
    employees=Employee.query.all()


    ### save new object 
    emp2= Employee(name='ahmed',image='pic2.png', salary=1000)
    db.session.add(emp2)
    db.session.commit()
    
    
    ### get one object --> show ??

"""

@app.route("/employees", endpoint="employees.index")
def employees_index():
    employees = Employee.query.all()
    return render_template("employees/index.html", employees=employees)


@app.route("/employees/<int:employee>", endpoint="employees.show")
def employees_show(employee):
    #
    # employee = Employee.query.get(employee)
    employee=  db.get_or_404(Employee, employee)
    # return employee.name
    return  render_template("employees/show.html", employee=employee)


# where request object ? http request??
# flask implicitly implement request ???
@app.route("/employees/create", endpoint="employees.create", methods=['GET', "POST"])
# default for request is get ?? if
# you want use post --> you must explicitly say this in app route
def employees_create():
    # get post data ??
    # print("request", request)
    print(request.method, request.form)
    if request.method == "POST":
        emp = Employee(name=request.form["name"], image=request.form["image"], salary=request.form["salary"])
        db.session.add(emp)
        db.session.commit()
        return  redirect(url_for("employees.index"))

    return render_template("employees/create.html")


@app.route("/employees/<int:employee>/delete", endpoint="employees.delete")
def employees_delete(employee):
    emp = db.get_or_404(Employee, employee)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for("employees.index"))



# start server
if __name__ == "__main__":
    app.run(debug=True) # start development server for your flask app
