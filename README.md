# Vocabulary List

next:
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


stuff:

- gnuicorn auto runs on 8000 regardless of compose.yaml (e.g. 5001:5000)