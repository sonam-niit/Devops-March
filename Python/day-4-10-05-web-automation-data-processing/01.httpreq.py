import requests

# Post Method
data = {"name":"sonam","username":"sonam23","email":"sonam@gmail.com"}
response = requests.post('https://jsonplaceholder.typicode.com/users',json=data)
print(response.json())


# Get Method
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print("Status Code: ",response.status_code)
data= response.json()
print('Street: ',data['address']['street'])
print('Suite: ',data['address']['suite'])
print('City: ',data['address']['city'])

# Pass Headers
# headers = {"Authorization: ":"Bearer qwertyuio23456789sdfghjxcvbnm"}
# params={"page":2}
# response = requests.get('https://testapi.com/1234/profile',headers,params )
# print(response.json())