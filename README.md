# Flask_REST
Study project on flask REST API


# Run server
.venv\Scripts\activate
flask run

# Run docker
docker build -t rest-apis-flask-python .
docker run -p 5005:5000 rest-apis-flask-python
docker compose up
docker compose up --build --force-recreate --no-deps web
docker compose -f docker-compose.yml -f docker-compose.debug.yml up

# Docker - Build Image
## Run container with existing code
docker run -dp 5000:5000 rest-apis-flask-python

## Run container with volume 
host folder synced with container folder (local development)
docker run -dp 5000:5000 -w /app -v "$(pwd): /app" rest-apis-flask-python