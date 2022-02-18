from flask import Blueprint

# Other
from endpoints.health.health import health_api
from endpoints.filldb.filldb import fillDb_api
from endpoints.dance.dance import dance_api
from endpoints.step.step import step_api

# General
exportEndpoints = Blueprint("exportEndpoints", __name__, url_prefix="/api")

exportEndpoints.register_blueprint(health_api)
exportEndpoints.register_blueprint(fillDb_api)
exportEndpoints.register_blueprint(dance_api)
exportEndpoints.register_blueprint(step_api)