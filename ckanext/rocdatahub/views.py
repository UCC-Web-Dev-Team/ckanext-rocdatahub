from flask import Blueprint
from ckan.plugins.toolkit import render

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


def get_blueprints():
    return [rocdatahub]
