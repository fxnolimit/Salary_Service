import requests
url = "http://localhost:5000/"

# test PUT
r = requests.put(url=url, params={'id':'3'})
print(r.text)

# test GET
r = requests.get(url=url)
print(r.text)

