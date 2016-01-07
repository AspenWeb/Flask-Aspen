from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

import pytest


@pytest.yield_fixture
def flask_client(harness):
    harness.fs.project.mk(
    ('aspen_flask_app.py', '''
import flask
from aspen.shims import flask as shim

app = flask.Flask(__name__)
app.debug = True
shim.install(app)
'''))
    sys.path.insert(0, harness.fs.project.root)
    from aspen_flask_app import app
    with app.test_client() as flask_client:
        yield flask_client
    sys.path = sys.path[1:]
