import requests


# response = requests.post(
#     'http://127.0.0.1:5000/advertisements/',
#     json={
#         'title': 'title1',
#         'description': 'description1',
#         'user': '1'
#     }
# )

# response = requests.post(
#     'http://127.0.0.1:5000/advertisements/1',
#     json={
#         'title': 'title1111'
#     }
# )

response = requests.get(
    'http://127.0.0.1:5000/advertisements/1',
)

# response = requests.delete(
#     'http://127.0.0.1:5000/advertisements/',
#     json={
#         'id': '1'
#     }
# )

print(response.status_code)
print(response.json())