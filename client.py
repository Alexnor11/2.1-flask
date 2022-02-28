import requests

HOST = 'http://127.0.0.1:8080'

# resp = requests.get(f'{HOST}/article/1')

# resp = requests.delete(f'{HOST}/article/1')

resp = requests.post(f'{HOST}/article/', json={
            'username': 'Name_1',
            'title': 'advertisement_1',
            'description': 'new1 description',
            })

print(resp.status_code)
print(resp.text)
