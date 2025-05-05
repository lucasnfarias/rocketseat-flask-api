# rocketseat-flask-api

API simples com Flask e Banco de dados

## Features

- Auth: user creation, login and logout
- Payments: mimetize pix payment using websockets
- Calculators: focus on design patterns
- Chat: use RabbitMQ to create a Telegram Chat Bot

## How to run

```sh
# install dependencies (or use virtual env - check section below)
pip3 install -r requirements.txt

# run mysql container
docker-compose up -d

# enter flask shell
flask --app run.py shell

# create tables
>>> db.create_all()
# create user
>>> user = User(username="lfarias", password="test", role="admin")
>>> db.session.add(user)
# commit your commands
>>> db.session.commit()
>>> exit()
```

# Using Virtualenv

```sh
# install virtualenv
pip3 install virtualenv==20.25.0

# create virtual env
python3 -m virtualenv venv

# enter the virtual env
source venv/bin/activate

# check installed libs
pip3 freeze

# install deps on virtual env
pip3 install -r requirements.txt

# exit virtual env
deactivate
```

# Tests

```sh
pytest -s -v
```

# Chat

To get the chat id from Telegram use this url:
`https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

To run your bot chat, first run the consumer:
`python run_consumer.py`

Then run the api with `python run_api.py` and use chat route to send a message:
`POST http://localhost:3000/chat/telegram/send-message`
