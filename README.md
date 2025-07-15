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

## Adding Apis

[send_app.py](server-python-fastapi/src/openapi_server/apis/send_app.py) is an example of adding a custom api handler by simply subclassing [programs_api_base](server-python-fastapi/src/openapi_server/apis/programs_api_base.py), 
[programs_api](https://github.com/shane-exygy/openapi-server/blob/main/server-python-fastapi/src/openapi_server/apis/programs_api.py#L54) then looks up the child and calls the api handler on it.

Note: that it seems all apis must be defined in the same child as the base class contains them as abstract.  It's unclear the intent in the base or programs_api for using the array, but given this is beta, it may improve later.
