from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_time():
    return f"Текущее время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
 # deploy fix
