from flask import Flask
import sys
import yaml
import json
import argparse
from github3 import login
from github3 import GitHub
import base64

# g=GitHub('amiforgit','#$123amigithub#$123')
app = Flask(__name__)
fu = sys.argv[1]
g = GitHub()
url= fu.split('/')
l = len(url)
# gh = g.login('zacharyzhong1116', '1101202027zzy')
# amiforgit = g.user('zacharyzhong1116')

#print(base64.b64decode(g.repository(url[l - 2], url[l - 1]).contents("/dev-config.yml").content))

@app.route("/")
def hello1():
    return "Hello World!"

@app.route("/v1/<name>")
def hello2(name):
    if name.endswith('.yml'):
        c = base64.b64decode(g.repository(url[l - 2], url[l - 1]).contents(name).content)
        return c
    if name.endswith('.yaml'):
        name = name[:-5] + ".yml"
        c = base64.b64decode(g.repository(url[l - 2], url[l - 1]).contents(name).content)
        return c
    if name.endswith('.json'):
        name = name[:-5] + ".yml"
        c = base64.b64decode(g.repository(url[l - 2], url[l - 1]).contents(name).content)
        c = json.dumps(yaml.load(c),sort_keys=True, indent=2)
        # retval=(json.dumps(yaml.load(base64.b64decode(g.repository(urlcon[l-2],urlcon[l-1]).contents(name).content))), sort_keys=True, indent=2))
        # retval=base64.b64decode(g.repository(urlcon[l-2],urlcon[l-1]).contents(name).content)
        return c
if __name__ == "__main__":
    app.run()
