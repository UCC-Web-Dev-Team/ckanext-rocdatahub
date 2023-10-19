"""Tests for helpers.py."""

import ckanext.rocdatahub.helpers as helpers


def test_rocdatahub_hello():
    assert helpers.rocdatahub_hello() == "Hello, rocdatahub!"
