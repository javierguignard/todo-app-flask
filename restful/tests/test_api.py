import json


def test_restful(app, client):
    del app
    res = client.get('/api/V1/todos')
    assert res.status_code == 200
    


def test_restful_post(app, client):
    del app
    text_task = 'Test Tarea Final'
    data = {
        'task':  text_task
    }
    res = client.post('/api/V1/todos', json=data)
    assert res.status_code == 200
    js_res = json.loads(res.data)
    id=js_res[-1][0]
    
    res = client.get('/api/V1/todos/{}'.format(id))
    assert res.status_code == 200
    js = json.loads(res.data)
    assert js.get('item')[1] == text_task

    res = client.get('/api/V1/todos/123456')
    assert res.status_code == 404
    
    

    #res = client.delete('/api/V1/todos/{}'.format(id))
    #assert res.status_code == 200