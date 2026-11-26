import requests

URL=  "http://127.0.0.1:5000/usuarios"

res= requests.get(f"{URL}/2")
print(res.json())