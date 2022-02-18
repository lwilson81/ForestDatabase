import json
from flask import Blueprint, request, jsonify

from models.models import db, StepModel

step_api = Blueprint("step_api", __name__)


@step_api.route("/addstep", methods=("POST",))
def addStep():
    body = request.get_json()
    step_name = str(body["step"])
    joints = str(body["joints"])
    error = None

    if not step_name or not joints:
        error = "Missing Data"
    if StepModel.query.filter_by(name=step_name).first() is not None:
        error = f"Step {step_name} already exists"

    if error is None:
        add_step = StepModel(step_name, joints)
        db.session.add(add_step)
        db.session.commit()
        message = f"Added step {step_name} successfully"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400


@step_api.route("/getsteps", methods=("GET",))
def getsteps():
    response = stepModel.query.all()
    steps = []
    for item in response:
        steps.append({"name": item.name})
    return jsonify({"steps": steps}), 200


@step_api.route("/deletestep", methods=("DELETE",))
def deletestep():
    body = request.get_json()
    step = str(body["step"])
    error = None

    if not step:
        error = "Missing Data"
    if stepModel.query.filter_by(name=step).first() is None:
        error = f"No step {step}"

    if error is None:
        stepModel.query.filter_by(name=step).delete()
        db.session.commit()
        message = f"step with name {step} removed"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400
