import json

def test_principal(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = 'Api Restful <b>(Really!)</b>'
    assert expected == res.get_data(as_text=True)




