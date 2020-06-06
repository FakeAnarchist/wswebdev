# wswebdev

Repository for the webDev workshop

Comandos úteis:
Venv: source /home/vasco/Desktop/wswebdev/tutorial-env/bin/activate
Docker: docker run -p 8080:8080 -d --name tutorial ericgoebelbecker/resttutorial
docker stop tutorial
docker rm tutorial

# create a PostgreSQL instance
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres

# stop instance
docker stop sqlalchemy-orm-psql

# destroy instance
docker rm sqlalchemy-orm-psql

#set the environment variable manually
FLASK_APP=microblog.py
