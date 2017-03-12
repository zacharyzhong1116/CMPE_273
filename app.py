from flask import Flask
import requests
app = Flask(__name__)
url = "https://raw.github.com/zacharyzhong1116/cmpe273-assignment1/master/myyml.yml"
c = requests.get(url).content
@app.route("/")
def hello():
    return c
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
