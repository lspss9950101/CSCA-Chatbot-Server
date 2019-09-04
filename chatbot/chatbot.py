from flask import Flask
import requests
import os

app = Flask(__name__)
link = 'http' + os.environ['HOST_PORT'][3:]

@app.route('/')
def index():
        r = requests.get(link)
        if r.status_code == requests.codes.ok:
                return r.text
        else:
                return r.status_code

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
