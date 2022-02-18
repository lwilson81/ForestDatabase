import json
from flask import Blueprint, request, jsonify

from models.models import db, DanceModel

dance_api = Blueprint("dance_api", __name__)


@dance_api.route("/adddance", methods=("POST",))
def adddance():
    body = request.get_json()
    dance = str(body["dance"])
    error = None

    if not dance:
        error = "Missing Data"
    if DanceModel.query.filter_by(name=dance).first() is not None:
        error = f"dance {dance} already exists"

    if error is None:
        add_dance = DanceModel(dance)
        db.session.add(add_dance)
        db.session.commit()
        message = f"Added dance {dance} successfully"
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
    pass
