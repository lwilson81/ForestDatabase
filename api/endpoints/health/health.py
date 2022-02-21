from flask import Blueprint

health_api = Blueprint("health_api", __name__)


@health_api.route("/health")
def check_health():
    return f"Works!", 200
