import json
from flask import Blueprint, request, jsonify

from models.models import db, StepModel

step_api = Blueprint("step_api", __name__)


@step_api.route("/addStep", methods=("POST",))
def addStep():
    body = request.get_json()
    step_name = str(body["step_name"])
    joints = str(body["joints"])
    error = None

    if not step_name or not joints:
        error = "Missing Data"
    if StepModel.query.filter_by(step_name=step_name).first() is not None:
        error = f"Step {step_name} already exists"

    if error is None:
        add_step = StepModel(step_name, joints)
        db.session.add(add_step)
        db.session.commit()
        message = f"Added step {step_name} successfully"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400


@step_api.route("/getSteps", methods=("GET",))
def getSteps():
    response = StepModel.query.all()
    steps = []
    for item in response:
        steps.append({"step_name": item.step_name, "joints":item.joints})
    return jsonify({"steps": steps}), 200


@step_api.route("/deleteStep", methods=("DELETE",))
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
