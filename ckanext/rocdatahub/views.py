from flask import Blueprint


rocdatahub = Blueprint(
    "rocdatahub", __name__)


def page():
    return "Hello, rocdatahub!"


rocdatahub.add_url_rule(
    "/rocdatahub/page", view_func=page)


def get_blueprints():
    return [rocdatahub]
