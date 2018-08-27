# Imports

from aux_pro import Process
from flask import Flask
from flask import render_template
from database import Database

app = Flask(__name__)
db  = Database()
pro = Process()

@app.route('/')
def index():
	pro.start_process()
	last = db.get_last()
	return render_template('index.html',l=last)


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8888)
