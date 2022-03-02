import os
from flask import Flask, flash, render_template
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
import json
from flask import request, jsonify, flash

load_dotenv()
app = Flask(__name__, static_folder="../build", static_url_path="/")

app.secret_key = os.getenv("SECRET_KEY")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://{username}:{password}@{host}:{port}/{db_name}".format(
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=os.getenv("MYSQL_POST"),
    db_name=os.getenv("MYSQL_DB"),
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class StepModel(db.Model):
    __tablename__ = "steps"

    step_name = db.Column(db.String(16), primary_key=True)
    joints = db.Column(db.String(16))

    def __init__(self, name, joint):
        self.step_name = name
        self.joints = joint

    def __repr__(self):
        return self.step_name

# --------------- DANCE MODEL------------------


class DanceModel(db.Model):
    __tablename__ = "dances"

    dance_name = db.Column(db.String(16), primary_key=True)
    steps = db.Column(db.String(16)) 

    def __init__(self, name, step):
        self.dance_name = name
        self.steps = step

    def __repr__(self):
        return self.dance_name

# creates tables if doesn't exist already
db.create_all()

@app.errorhandler(404)
def not_found(e):
    return "Not found"


@app.route("/")
def index():
    return "Im here"

@app.route("/filldb")
def filldb():
    # 
    dances = []
    steps = []

    for dance_name in dances:
        add_dance = DanceModel(dance_name, ___)
        db.session.add(add_dance)

    for step_name in steps:
        add_step = StepModel(step_name, ___)
        db.session.add(add_step)

    db.session.commit()
    return "db filled"

def matlabtoPython(str_in):
        stringStep = str_in.replace('{', '[')
        stringStep = stringStep.replace('}', ']')
        stringStep = stringStep.replace(';',' ')
        stringStep = stringStep.replace(' ', ',')
        return stringStep

@app.route("/dance/addDance", methods=("POST", "GET", ))
def adddance():
    msg = ""
    
    if request.method == "POST":
        dance_name = request.form["dance_name"]
        steps = request.form["steps"]
        steps = matlabtoPython(steps)
        print(request.form)

        if not dance_name:
            print("hello?")
            msg = ("Dance name is required!")
        elif not steps:
            msg = ("Steps are required!")
        elif DanceModel.query.filter_by(dance_name=dance_name).first() is not None:
            msg = (f"Dance {dance_name} already exists")

        else:
            add_dance = DanceModel(dance_name, steps)
            db.session.add(add_dance)
            db.session.commit()
            message = f"Added dance {dance_name} successfully"
            msg = (message)
    return render_template("makeDance.html", msg = msg, url="localhost:5000")

   
        
            


@app.route("/dance/getDances", methods=("GET",))
def getDances():
    response = DanceModel.query.all()
    dances = []
    for item in response:
        dances.append({"name": item.name})
    return jsonify({"dances": dances}), 200


@app.route("/dance/deleteDance", methods=("DELETE",))
def deleteDance():
    body = request.get_json()
    dance_name = str(body["dance_name"])
    error = None

    if not dance_name:
        error = "Missing Data"
    if DanceModel.query.filter_by(dance_name=dance_name).first() is None:
        error = f"No dance {dance_name}"

    if error is None:
        DanceModel.query.filter_by(dance_name=dance_name).delete()
        db.session.commit()
        message = f"dance with name {dance_name} removed"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400



@app.route("/step/addStep", methods=("POST", "GET"))
def addStep():
    msg = ""
    
    if request.method == "POST":
        step_name = request.form["step_name"]
        joints = request.form["joints"]
        joints = matlabtoPython(joints)
        print(request.form)

        if not step_name:
            msg = ("Step name is required!")
        elif not joints:
            msg = ("Joints are required!")
        elif StepModel.query.filter_by(step_name=step_name).first() is not None:
            msg = (f"Step {step_name} already exists")

        else:
            add_step = StepModel(step_name, joints)
            db.session.add(add_step)
            db.session.commit()
            message = f"Added step {step_name} successfully"
            msg = (message)
    return render_template("makeStep.html", msg = msg, url="localhost:5000")

    


@app.route("/step/getSteps", methods=("GET",))
def getSteps():
    response = StepModel.query.all()
    steps = []
    for item in response:
        steps.append({"step_name": item.step_name, "joints":item.joints})
    return jsonify({"steps": steps}), 200


@app.route("/step/deleteStep", methods=("DELETE",))
def deleteStep():
    body = request.get_json()
    step_name = str(body["step_name"])
    error = None

    if not step_name:
        error = "Missing Data"
    if StepModel.query.filter_by(step_name=step_name).first() is None:
        error = f"No step {step_name}"

    if error is None:
        StepModel.query.filter_by(step_name=step_name).delete()
        db.session.commit()
        message = f"step with name {step_name} removed"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400

