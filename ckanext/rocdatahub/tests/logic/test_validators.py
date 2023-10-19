"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.rocdatahub.logic import validators


def test_rocdatahub_reauired_with_valid_value():
    assert validators.rocdatahub_required("value") == "value"


def test_rocdatahub_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.rocdatahub_required(None)
