from flask import Blueprint

from models.models import db, DanceModel, StepModel

fillDb_api = Blueprint("fillDb_api", __name__)


@fillDb_api.route("/filldb")
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

