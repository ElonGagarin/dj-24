import requests

baseUrl = 'http://localhost:8000/api'

print(requests.get(baseUrl+'/sensors/', 
# data= {
#   "sensor": 1,
#   "temperature": 22.3
# }
))
