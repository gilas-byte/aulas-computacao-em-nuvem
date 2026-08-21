import requests

url = "http://localhost:5000/nota/650"

for _ in range(1000):
    requests.get(url)
print("Requisições concluídas")