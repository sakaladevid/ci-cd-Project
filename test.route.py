from App import *

def test_Home():
        response=app.test_client().get('/')
        assert b"Hello, World! This is a simple Flask web app." in response.data
        assert response,status_code ==200
