import requests
import json

#POST
#Добавляем нового питомца и получаем его ID

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

data = {'name': 'Tayga',
        'status': 'available'}

data = json.dumps(data)

res_1 = requests.post("https://petstore.swagger.io/v2/pet", headers=headers, data=data)

print('Статус запроса: ' + str(res_1.status_code))
print(res_1.json())

#GET
#Получаем информацию об ID и статусе запроса

petID = 9223372036854775807

res_2 = requests.get(f"https://petstore.swagger.io/v2/pet/{petID}", headers=headers)

print('Статус запроса petID: ' + str(res_2.status_code))
print(res_2.json())

#PUT
# Замена статуса доступности животного

data = {'status': 'sold'}

res_3 = requests.put("https://petstore.swagger.io/v2/pet", headers=headers, json=data)

print('Статус запроса: ' + str(res_3.status_code))
print(res_3.json())


#DELETE
#Удаление питомца

res_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{petID}', headers=headers)

print('Статус запроса: ' + str(res_4.status_code))
print(res_4.json())






