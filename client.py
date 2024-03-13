import requests

# url = 'http://127.0.0.1:5000/process_string'
url = 'https://aida-async-workflow.uc.r.appspot.com/process_string'
data = {'input_string': 'my name'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json()['result'])
else:
    print("An error occurred: ", response.json())