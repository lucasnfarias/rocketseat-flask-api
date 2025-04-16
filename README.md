# rocketseat-flask-api

API simples com Flask e Banco de dados

## Features

- Auth: user creation, login and logout
- Payments: mimetize pix payment using websockets

## How to run

```sh
# install dependencies
pip3 install -r requirements.txt

# run mysql container
docker-compose up -d

# enter flask shell
flask shell

# create tables
>>> db.create_all()
# create user
>>> user = User(username="lfarias", password="test", role="admin")
>>> db.session.add(user)
# commit your commands
>>> db.session.commit()
>>> exit()
```

# Tests

```sh
cd tests
pytest test_pix.py -v
```
