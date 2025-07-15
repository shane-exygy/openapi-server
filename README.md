Experiment to use openapi tools to generate a fastapi server. Note that fastapi is beta support and not well documented.

serve.yml was hand constructed using parts of CiviForm's openapi export for a test program.

## Generate server

`openapi-generator-cli generate -i ./server.yml -g python-fastapi -o ./server-python-fastapi`


## Run the fast api service

See [server docs](/server-python-fastapi/README.md) too

```
cd server-python-fastapi/

PYTHONPATH=src uvicorn openapi_server.main:app --host 0.0.0.0 --port 8080 
```

## Make a test request

`curl -s -H 'accept: application/json' -H 'Content-Type: application/json' -K post_request.txt`
