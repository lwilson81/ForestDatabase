from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()

# --------------- STEP MODEL------------------


class StepModel(db.Model):
    __tablename__ = "steps"

    step_name = db.Column(db.String(), primary_key=True)
    joints = db.Column(db.String())

    def __init__(self, name, joint):
        self.step_name = name
        self.joints = joint

    def __repr__(self):
        return f"<Step {self.step_name}>"

# --------------- DANCE MODEL------------------


class DanceModel(db.Model):
    __tablename__ = "dances"

    dance_name = db.Column(db.String(), primary_key=True)
    steps = db.Column(db.String()) 

    def __init__(self, name, step):
        self.dance_name = name
        self.steps = step

    def __repr__(self):
        return f"<Dance {self.dance_name}>"



