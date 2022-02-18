import json
from flask import Blueprint, request, jsonify

from models.models import db, DanceModel

dance_api = Blueprint("dance_api", __name__)


@dance_api.route("/addDance", methods=("POST",))
def adddance():
    body = request.get_json()
    dance_name = str(body["dance_name"])
    steps = str(body["steps"])
    error = None

    if not dance_name or steps:
        error = "Missing Data"
    if DanceModel.query.filter_by(dance_name=dance_name).first() is not None:
        error = f"Dance {dance_name} already exists"

    if error is None:
        add_dance = DanceModel(dance_name, steps)
        db.session.add(add_dance)
        db.session.commit()
        message = f"Added dance {dance_name} successfully"
        return jsonify({"status": "ok", "message": message}), 200
    else:
        return jsonify({"status": "bad", "error": error}), 400


@dance_api.route("/getDances", methods=("GET",))
def getDances():
    response = DanceModel.query.all()
    dances = []
    for item in response:
        dances.append({"name": item.name})
    return jsonify({"dances": dances}), 200


@dance_api.route("/deleteDance", methods=("DELETE",))
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
