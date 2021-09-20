"""Simple helath check urls"""
from flask import Blueprint

health_check = Blueprint('healthcheck', __name__)


@health_check.route('/')
def root_health_check():
    """helath check url"""
    return {"status": "ok"}


@health_check.route("/_health")
def url_health():
    """helath check url"""
    return {"status": "ok"}
