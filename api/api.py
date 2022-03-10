import os
from textwrap import fill
from flask import Flask, flash, render_template
from dotenv import load_dotenv
import re

from flask_sqlalchemy import SQLAlchemy
import json
from flask import request, jsonify, flash
from steps import *

load_dotenv()
app = Flask(__name__, static_folder="../build", static_url_path="/")

# connects database using .env values (if no .env exists, please create one using your
# SQL Server details using example.env)
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

    step_name = db.Column(db.String(255), primary_key=True)
    start_position = db.Column(db.Text())
    joint_angles = db.Column(db.Text())
    joint_times = db.Column(db.Text())

    def __init__(self, name, start, angle, time):
        self.step_name = name
        self.start_position = start
        self.joint_angles = angle
        self.joint_times = time

    def __repr__(self):
        return self.step_name

# --------------- DANCE MODEL------------------


class DanceModel(db.Model):
    __tablename__ = "dances"

    dance_name = db.Column(db.String(255), primary_key=True)
    start_position = db.Column(db.Text())
    steps = db.Column(db.Text()) 

    def __init__(self, name, start, step):
        self.dance_name = name
        self.start_position = start
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

    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    for step in fill_db_steps:
        step_name = namestr(step, globals())[0]
        start_position = {}
        angles = json.dumps(step[0])
        times = json.dumps(step[1])
        add_step = StepModel(step_name, start_position, angles, times)
        db.session.add(add_step)
    
    for dance in fill_db_dances:
        dance_name = namestr(dance, globals())[0]
        start_position = {}
        steps = dance
        add_dance = StepModel(dance_name, start_position, steps)
        db.session.add(add_dance)
   
    
    db.session.commit()
    return "db filled"

def matlabtoPython(str_in):
    matlabIndicators = [";", "{", "}"]
    if any(indicator in str_in for indicator in matlabIndicators) or not("," in str_in):
        stringStep = str_in.replace('{', '[')
        stringStep = stringStep.replace('}', ']')
        stringStep = stringStep.replace(';',',')
        # below step replaces anything of type digit -> space -> digit or negative with 
        # digit -> comma -> digit or negative
        # helpful tool for regex: https://pythex.org/
        stringStep = re.sub(r"(\d)\s(\d|-)", r"\1,\2", stringStep)
        # have to do it again to get the missing matches from double usage
        stringStep = re.sub(r"(\d)\s(\d|-)", r"\1,\2", stringStep)
    return stringStep

def validateDance(start_pos, steps):
    # validation for dance here
    return (matlabtoPython(start_pos), matlabtoPython(steps))


@app.route("/dance/addDance", methods=("POST", "GET", ))
def addDance():
    msg = ""
    
    if request.method == "POST":
        dance_name = request.form["dance_name"]
        start_pos = request.form["start_pos"]
        steps = request.form["steps"]
        (start_pos, steps) = validateDance(start_pos, steps)
        
        if not dance_name:
            msg = ("Dance name is required!")
        elif not start_pos:
            msg = ("Start position is required!")
        elif not steps:
            msg = ("Steps are required!")
        elif DanceModel.query.filter_by(dance_name=dance_name).first() is not None:
            msg = (f"Dance {dance_name} already exists")

        else:
            add_dance = DanceModel(dance_name, start_pos, steps)
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
        dances.append({"name": item.name, "start_position": item.start_pos, "steps":item.steps})
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
        message = f"Dance with name {dance_name} removed"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400

def validateStep(start_pos, joint_angles, joint_times):
    # validation for step here
    return (matlabtoPython(start_pos), matlabtoPython(joint_angles), matlabtoPython(joint_times))

@app.route("/step/addStep", methods=("POST", "GET"))
def addStep():
    msg = ""
    
    if request.method == "POST":
        step_name = request.form["step_name"]
        start_pos = request.form["start_pos"]
        joint_angles = request.form["joint_angles"]
        joint_times = request.form["joint_times"]
        (start_pos, joint_angles, joint_times) = validateStep(start_pos, joint_angles, joint_times)

        if not step_name:
            msg = ("Step name is required!")
        elif not start_pos:
            msg = ("Start position is required!")
        elif not joint_angles:
            msg = ("Joint angles are required!")
        elif not joint_times:
            msg = ("Joint times are required!")
        elif StepModel.query.filter_by(step_name=step_name).first() is not None:
            msg = (f"Step {step_name} already exists")

        else:
            add_step = StepModel(step_name, start_pos, joint_angles, joint_times)
            db.session.add(add_step)
            db.session.commit()
            message = f"Added step {step_name} successfully"
            msg = (message)
    return render_template("makeStep.html", msg = msg, url="localhost:5000")

    


@app.route("/step/getSteps", methods=("GET",))
def getSteps():
    response = StepModel.query.all()
    steps = []

    # print(response[0].start_position)
    for item in response:
        steps.append({"step_name": item.step_name, "start_position": item.start_position, 
        "joint_angles": item.joint_angles, "joint_times":item.joint_times})
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
        message = f"Step with name {step_name} removed"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400

