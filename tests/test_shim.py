def test_flask_shim_is_importable():
    from aspen.shims import flask as shim
    assert shim

def test_flask_shim_basically_works(harness, flask_client):
    harness.fs.project.mk(('www/index.spt', '''
program = request.args['program']
[-----] text/html
Greetings, {{program}}!
'''))
    response = flask_client.get('/?program=flask')
    assert response.get_data() == 'Greetings, flask!'
