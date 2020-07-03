from flask import Flask
import json
from resources.linkedin import linkedin

app = Flask(__name__)

app.register_blueprint(linkedin)
app.run()
