import os
from textwrap import fill
from flask import Flask, flash, render_template
from dotenv import load_dotenv
import re

from flask_sqlalchemy import SQLAlchemy
import json
from flask import request, jsonify, flash
from steps import *
from flask import Markup

load_dotenv()
app = Flask(__name__, static_folder="../build", static_url_path="/")

# connects database using .env values (if no .env exists, please create one using your
# SQL Server details using example.env)
app.secret_key = os.getenv("SECRET_KEY")
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "mysql://{username}:{password}@{host}:{port}/{db_name}".format(
#     username=os.getenv("MYSQL_USER"),
#     password=os.getenv("MYSQL_PASSWORD"),
#     host=os.getenv("MYSQL_HOST"),
#     port=os.getenv("MYSQL_POST"),
#     db_name=os.getenv("MYSQL_DB"),
# )
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


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


@app.errorhandler(404)
def not_found(e):
    return "Not found"

@app.route("/dance/makeCSV", methods=("POST", "GET", ))
def makeCSV():
    msg=""
    if request.method=="POST":
        dance_name = (str(body["dance_name"])) if body else (request.form["dance_name"])
        dance = DanceModel.query.filter_by(dance_name=dance_name).first_or_404()
    
    # return {'dance_name': dance.dance_name, 'start_position': dance.start_position,
    #         'steps': dance.steps}
    
    return render_template("makeCSV.html", msg=msg, url="localhost:5000")



@app.route("/filldb")
def filldb():

    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    for step in fill_db_steps:
        step_name = namestr(step, globals())[0]
        try:
            start_position = json.dumps(step[2])
        except:
            start_position = json.dumps([0, 0, 0, 90, 0, 0, 0])
        angles = json.dumps(step[0])
        times = json.dumps(step[1])
        add_step = StepModel(step_name, start_position, angles, times)
        db.session.add(add_step)

    for dance in fill_db_dances:
        dance_name = namestr(dance, globals())[0]
        try:
            start_position = json.dumps(dance[2])
        except:
            start_position = json.dumps([0, 0, 0, 90, 0, 0, 0])
        steps = dance
        add_dance = DanceModel(dance_name, start_position, steps)
        db.session.add(add_dance)

    db.session.commit()
    return "db filled"

@app.route("/")
def index():
    db.create_all()
    # filldb()
    text = """Add Step: <a href='/step/addStep'>/step/addStep</a>\n
              Get All Steps: <a href='/step/getSteps'>/step/getSteps</a>\n
              Get Step: /step/getStep/(step_name)\n
              Delete Step: /step/deleteStep\n
              Clear Step Table: <a href='/step/clearTable'>/step/clearTable</a>\n
              Add Dance: <a href='/dance/addDance'>/dance/addDance</a>\n
              Get All Dances: <a href='/dance/getDances'>/dance/getDances</a>\n
              Get Dance: /dance/getDance/(dance_name)\n
              Delete Dance: /dance/deleteDance\n
              Clear Dance Table: <a href='/dance/clearTable'>/dance/clearTable</a>\n
              Fill Database: <a href='/filldb'>/filldb</a>\n
        """
    text = text.replace('\n', '<br>')
    Markup(text).unescape()
    return text





def matlabtoPython(str_in):
    matlabIndicators = [";", "{", "}"]
    if any(indicator in str_in for indicator in matlabIndicators) or not("," in str_in):
        str_in = str_in.replace('{', '[')
        str_in = str_in.replace('}', ']')
        str_in = str_in.replace(';', ',')
        # below step replaces anything of type digit -> space -> digit or negative with
        # digit -> comma -> digit or negative
        # helpful tool for regex: https://pythex.org/
        str_in = re.sub(r"(\d)\s(\d|-)", r"\1,\2", str_in)
        # have to do it again to get the missing matches from double usage
        str_in = re.sub(r"(\d)\s(\d|-)", r"\1,\2", str_in)
    # if any(i.isalnum() for i in str_in):
    #     str_in.replace
    return json.loads(str_in)


def validateDance(start_pos, steps):
    start_pos = matlabtoPython(start_pos)
    steps = matlabtoPython(steps)
    error_msg = None
    if len(start_pos) != 7:
        error_msg = f"Provide start position for the 7 joints!"
        return (error_msg, start_pos, joint_angles, joint_times)
    for pos in start_pos:
        if pos > 360:
            error_msg = f"Start position can't be over 360 degrees!"
            return (error_msg, start_pos, joint_angles, joint_times)
        if pos < -360:
            error_msg = f"Start position can't be under -360 degrees!"
            return (error_msg, start_pos, joint_angles, joint_times)

    for step in steps:
        if StepModel.query.filter_by(step_name=step).first() is None:
            error_msg = f"Step {step} does not exist yet!"
            return (error_msg, start_pos, steps)

    return (error_msg, json.dumps(start_pos), json.dumps(steps))


@app.route("/dance/addDance", methods=("POST", "GET", ))
def addDance():
    msg = ""

    if request.method == "POST":
        body = request.get_json()
        dance_name = (str(body["dance_name"])) if body else (request.form["dance_name"])
        start_pos = (str(body["start_pos"])) if body else (request.form["start_pos"])
        steps = (str(body["steps"])) if body else (request.form["steps"])

        if not dance_name:
            msg = ("Dance name is required!")
        elif not start_pos:
            msg = ("Start position is required!")
        elif not steps:
            msg = ("Steps are required!")
        elif DanceModel.query.filter_by(dance_name=dance_name).first() is not None:
            msg = (f"Dance {dance_name} already exists")

        else:
            (error, start_pos, steps) = validateDance(start_pos, steps)
            if error:
                msg = error
            else:
                add_dance = DanceModel(dance_name, start_pos, steps)
                db.session.add(add_dance)
                db.session.commit()
                message = f"Added dance {dance_name} successfully"
                msg = (message)
    return render_template("makeDance.html", msg=msg, url="localhost:5000")


@app.route("/dance/getDances", methods=("GET",))
def getDances():
    response = DanceModel.query.all()
    dances = []
    for item in response:
        dances.append({"name": item.dance_name,
                      "start_position": item.start_position, "steps": item.steps})
    return jsonify({"dances": dances}), 200


@app.route('/dance/getDance/<dance_name>')
def getDance(dance_name):
    dance = DanceModel.query.filter_by(dance_name=dance_name).first_or_404()
    return {'dance_name': dance.dance_name, 'start_position': dance.start_position,
            'steps': dance.steps}


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


@app.route("/dance/clearTable")
def clearDances():
    response = DanceModel.query.all()
    for item in response:
        db.session.query(DanceModel).delete()
        db.session.commit()
    return "Dance Table has been cleared"


ang_constraints = [
    (-360, 360),
    (-118, 120),
    (-360, 360),
    (-118, 225),
    (-360, 360),
    (-97, 180),
    (-360, 360)
]


def validateStep(start_pos, joint_angles, joint_times):
    start_pos = matlabtoPython(start_pos)
    joint_angles = matlabtoPython(joint_angles)
    joint_times = matlabtoPython(joint_times)

    error_msg = None
    if len(start_pos) != 7:
        error_msg = f"Provide start position for all 7 joints! Missing {7-len(start_pos)} joints"
        return (error_msg, start_pos, joint_angles, joint_times)
    if len(joint_angles) != 7:
        error_msg = f"Provide angles for all 7 joints! Missing {7-len(joint_angles)} joints"
        return (error_msg, start_pos, joint_angles, joint_times)
    if len(joint_times) != 7:
        error_msg = f"Provide times for all 7 joints! Missing {7-len(joint_times)} joints"
        return (error_msg, start_pos, joint_angles, joint_times)

    for joint_num in range(7):
        time = joint_times[joint_num]
        angle = joint_angles[joint_num]
        lower_bound = ang_constraints[joint_num][0]
        upper_bound = ang_constraints[joint_num][1]

        if isinstance(time, list):
            if not isinstance(angle, list) or (len(time) != len(angle)):
                error_msg = f"Joint {joint_num+1}'s angles and times have different lengths!"
                return (error_msg, start_pos, joint_angles, joint_times)

            for ins in range(len(time)):   
                tim = time[ins]    
                ang = angle[ins] 
                if tim < 0:
                    error_msg = f"Angle {joint_num+1} has a zero or negative time!"
                    return (error_msg, start_pos, joint_angles, joint_times)

                if ang > upper_bound:
                    error_msg = f"Joint {joint_num+1} can't have angles over {upper_bound} degrees!"
                    return (error_msg, start_pos, joint_angles, joint_times)
                if ang < lower_bound:
                    error_msg = f"Joint {joint_num+1} can't have angles under {lower_bound} degrees!"
                    return (error_msg, start_pos, joint_angles, joint_times)

                vel = angle[ins]/time[ins]
                if vel >= 180 or vel <= -180:
                    error_msg = f"One of the movements for angle {joint_num+1} is too fast"
                    return (error_msg, start_pos, joint_angles, joint_times)

        else:
            if time <= 0:
                error_msg = f"Angle {joint_num+1} has a zero or negative time!"
                return (error_msg, start_pos, joint_angles, joint_times)

            if angle > upper_bound:
                error_msg = f"Step {joint_num+1} can't have angles over {upper_bound} degrees!"
                return (error_msg, start_pos, joint_angles, joint_times)
            if angle < lower_bound:
                error_msg = f"Step {joint_num+1} can't have angles under {lower_bound} degrees!"
                return (error_msg, start_pos, joint_angles, joint_times)

            vel = angle/time
            if vel >= 180 or vel <= -180:
                error_msg = f"One of the movements for angle {joint_num+1} is too fast"
                return (error_msg, start_pos, joint_angles, joint_times)

    return (error_msg, json.dumps(start_pos), json.dumps(joint_angles), json.dumps(joint_times))


@app.route("/step/addStep", methods=("POST", "GET"))
def addStep():
    msg = ""

    if request.method == "POST":
        body = request.get_json()
        step_name = (str(body["step_name"])) if body else (request.form["step_name"])
        start_pos = (str(body["start_pos"])) if body else (request.form["start_pos"])
        joint_angles = (str(body["joint_angles"])) if body else (request.form["joint_angles"])
        joint_times = (str(body["joint_times"])) if body else (request.form["joint_times"])

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

        if not msg:
            (error_msg, start_pos, joint_angles, joint_times) = validateStep(
                start_pos, joint_angles, joint_times)
            if not error_msg:
                add_step = StepModel(step_name, start_pos,
                                     joint_angles, joint_times)
                db.session.add(add_step)
                db.session.commit()
                message = f"Added step {step_name} successfully"
                msg = (message)
            else:
                msg = error_msg
    return render_template("makeStep.html", msg=msg, url="localhost:5000")


@app.route("/step/getSteps", methods=("GET",))
def getSteps():
    response = StepModel.query.all()
    steps = []

    # print(response[0].start_position)
    for item in response:
        steps.append({"step_name": item.step_name, "start_position": item.start_position,
                      "joint_angles": item.joint_angles, "joint_times": item.joint_times})
    return jsonify({"steps": steps}), 200


@app.route('/step/getStep/<step_name>')
def getStep(step_name):
    step = StepModel.query.filter_by(step_name=step_name).first_or_404()
    return {'step_name': step.step_name, 'start_position': step.start_position,
            'joint_angles': step.joint_angles, 'joint_times': step.joint_times}


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


@app.route("/step/clearTable")
def clearSteps():
    response = StepModel.query.all()
    for item in response:
        db.session.query(StepModel).delete()
        db.session.commit()
    return "Step Table has been cleared"
