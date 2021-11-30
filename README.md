##### Desenvolva uma API com a biblioteca FastAPI, com os seguintes requisitos:

1. Autenticação com OAuth2, protegendo todas as rotas, gerando token, que expira a cada hora, e o token deve ser utilizado em todos
os endpoints;
2. Desenvolva um endpoint com request method POST, com payload: User (Str), Order (Float), PreviousOrder (Boolean), retornando um
JSON com a RESPONSE 200 e os items do payload. Lembrando que esse item deve seguir as regras do item 01;
3. Desenvolva um endpoint com request method GET, buscando dados da API OpenBreweries (https://api.openbrewerydb.org/breweries/),
mostrando no resultado apenas um dicionário com os nomes das cervejas que estarão em uma lista.    


Para rodar o projeto:
``` 
$ pip install -r requirements.txt

$ uvicorn --reload cervejarias.main:app
```
O servidor estará disponível em http://127.0.0.1:8000    
Os endpoints disponíveis são:    
- /token    
  - Para ser efetuada e coletada a autenticação/token
- /breweries    
  - Para acessar a API externa e salvar em um dict uma lista com os nomes das cervejarias
- /add_brewery
  - Para efetuar o cadastro de um usuário/cervejaria
- /docs
  - Para acessar a documentação da API


#### Exemplo utilizando a lib requests
```
>>> from cervejarias.main import *   
>>> import requests
>>> import json

>>> token_url = 'http://localhost:8000/token'
>>> cerv_url = 'http://localhost:8000/breweries'
>>> add_url = 'http://localhost:8000/add_brewery'

>>> payload = {'username': 'boreal', 'password': f'{SECRET_KEY}'}
>>> token = requests.post(token_url, data=payload)

>>> access_token = json.loads(token.text)['access_token']

>>> headers = {
  'Authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json',
}

>>> breweries = requests.get(cerv_url, headers=headers)
>>> breweries.json()
{'cervejarias': ['10-56 Brewing Company',
  '10 Barrel Brewing Co',
  '10 Barrel Brewing Co',
  '10 Barrel Brewing Co - Bend Pub',
  '10 Barrel Brewing Co - Boise',
  '10 Barrel Brewing Co - Denver',
  '10 Barrel Brewing Co',
  '10 Barrel Brewing Co',
  '10 Torr Distilling and Brewing',
  '101 Brewery',
  '101 North Brewing Company',
  '105 West Brewing Co',
  '10K Brewing',
  '10th District Brewing Company',
  '11 Below Brewing Company',
  '1188 Brewing Co',
  '12 Acres Brewing Company',
  '12 Gates Brewing Company',
  '12 West Brewing Company',
  '12 West Brewing Company - Production Facility']
}

>>> user_payload = json.dumps({'username': 'Zé da esquina', 'order': 5.75, 'previousorder': False})
>>> user = requests.post(add_url, data=user_payload, headers=headers)    

>>> user.json()
{
 'username': 'Zé da esquina',
 'order': 5.75,
 'previousorder': False
}    

>>> user.status_code
200
```
