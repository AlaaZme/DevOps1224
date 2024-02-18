from flask import Flask
from time import sleep
import MainGame
app = Flask(__name__)


@app.route('/')
def index():
    return


app.run(host="0.0.0.0",port=80)

