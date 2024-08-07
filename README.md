# Vocabulary List

next:
- RBAC https://pythonhosted.org/Flask-Principal/

- https://blog.miguelgrinberg.com/post/restful-authentication-with-flask 

- done: seed_data pws have invalid salt value - come up with better way to seed
    - https://stackoverflow.com/questions/34548846/flask-bcrypt-valueerror-invalid-salt

- complete login/register 
    - using flask login manager, config of login mgmt in auth routes file - maybe move it to it's own file under auth dir

- ORM to Domain object conversion layer

- figure out how to connect react (attn to sessions)
- start documenting endpoint shapes
- start writing tests
- github action for test running


docker compose up --build --remove-orphans

docker-compose -f compose.prod.yaml up -d --build
docker-compose down -v

```
docker exec -it <container> bash
```

```
docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
```

app secret
https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
```
python -c 'import secrets; print(secrets.token_hex())'
```

stuff:

https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

- gnuicorn auto runs on 8000 regardless of compose.yaml (e.g. 5001:5000)