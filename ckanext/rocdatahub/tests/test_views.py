"""Tests for views.py."""

import pytest

import ckanext.rocdatahub.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "rocdatahub")
@pytest.mark.usefixtures("with_plugins")
def test_rocdatahub_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("rocdatahub.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, rocdatahub!"
