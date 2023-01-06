import requests
import json

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())

input_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(input_pet, ensure_ascii=False))
print(res.status_code)
print(res.json())
print(type(res.json()))

change_pet = {
  "id": 9223372036854593969,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_rename_pet = requests.put(f"https://petstore.swagger.io/v2/pet",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(change_pet, ensure_ascii=False))
print(res_rename_pet.status_code)
print(res_rename_pet.json())
print(type(res_rename_pet.json()))

delete_pet = {
  "id": 9223372036854593969}

res_delete_pet = requests.delete(f"https://petstore.swagger.io/v2/pet",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(delete_pet, ensure_ascii=False))
print(res_rename_pet.status_code)
print(res_rename_pet.json())
print(type(res_rename_pet.json()))

