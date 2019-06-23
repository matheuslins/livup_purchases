# LivUp Purchases

### About

This is a API which you can see the purchase summary from a LivUp customers.
With this service it's possible monitor the average ticket sizes
from the customers and make predictive models for a decision making.

#### Requirements

- Pip
- Virtual Environment (virtualenv)
- Postgres SQL (psycopg2)

#### Environment vars

Create a `.env` file in root of the project:

````.env
 THERE IS A FILE CALLED '.env-example'
 WHERE SHOW ALL NECESSARY ENVIRONMENTS VARIABLES TO THIS PROJECT
````


#### Pre Run

1 - Install dependencies: ```make setup_dev``` \
2 - Run database migrations: ```make revision && make upgrade```

### Running

- Run API
````python
make run
````
The service is running in: http://localhost:7777/

- Insert data in database

````
Method: POST
Endpoint: /insert
Response: 'ok'
Success Status code: 200 
````

- Show Purchases
````
Method: GET
Endpoint: /purchases
Response: [
    {
        "amount": 34.8,
        "items": [
            {
                "name": "Saint Peter Castanha Do Pará + Arroz + Mix De Legumes",
                "price": 23.7,
                "qty": 1
            },
            {
                "name": "Chips de mandioquinha",
                "price": 3.7,
                "qty": 3
            }
        ],
        "user_id": "58febd18b22f83103aa218af"
    },
    {
        "amount": 97,
        "items": [
            {
                "name": "Castanha de caju",
                "price": 9.7,
                "qty": 10
            }
        ],
        "user_id": "58febd18b22f83103aa218af"
    } ...
]
Success Status code: 200 
````

- Show user purchases
````
Method: GET
Endpoint: /purchases?user_id=58febd18b22f83103aa218af
Response: [
    {
        "amount": 34.8,
        "items": [
            {
                "name": "Saint Peter Castanha Do Pará + Arroz + Mix De Legumes",
                "price": 23.7,
                "qty": 1
            },
            {
                "name": "Chips de mandioquinha",
                "price": 3.7,
                "qty": 3
            }
        ],
        "user_id": "58febd18b22f83103aa218af"
    }
]
Success Status code: 200
````

**Note**: In case hasn't data in database, the API returns 204 as status code


#### Production Environment

`Has the same routes with the host:` https://livupurcharse.herokuapp.com/
