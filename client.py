import requests


response = requests.post(
    'http://127.0.0.1:5000/advertisements/',
    json={
        'title': 'title1',
        'description': 'description1',
        'user': '1'
    }
)
print(response.status_code)
print(response.json)