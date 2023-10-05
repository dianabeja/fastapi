import requests
body = {
    "age": 64,
    "sex": 1,
    "cp": 3,
    "trestbps": 120,
    "chol": 267,
    "fbs": 0,
    "restecg": 0,
    "thalach": 99,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
    }
response = requests.post(url = 'https://heart-ml-service-dianabeja.cloud.okteto.net/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}
