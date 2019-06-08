import os
from bottle import route, run

@route('/')
def hello():
        return "Hello World!!\n"

run(host='0.0.0.0',port=int(os.environ.get("PORT", 8080)))
# run(host='0.0.0.0',port=8080)