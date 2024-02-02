from flask import Blueprint
from ckan.plugins.toolkit import render
# from ckanext.rocdatahub.model.data_request import DataRequest

rocdatahub = Blueprint(
    "rocdatahub", __name__)

@rocdatahub.route(u'/ecosystems')
def ecosystem():
    return render(u'home/ecosystem.html')

@rocdatahub.route(u'/maps')
def map():
    return render(u'home/map.html')

@rocdatahub.route(u'/faqs')
def faqs():
    return render(u'home/faqs.html')

@rocdatahub.route(u'/countries')
def countries():
    return render(u'home/countries.html')

@rocdatahub.route(u'/country/<country>')
def country(country):
    return render(u'home/country.html', {'country': country})
# def page():
#     return "Hello, rocdatahub!"


# rocdatahub.add_url_rule(
#     "/rocdatahub/page", view_func=page)

# rocdatahub.add_url_rule(
#     "/data-request", 
#     "create",
#     DataRequest.create,
#     methods=["POST"])


def get_blueprints():
    return [rocdatahub]
