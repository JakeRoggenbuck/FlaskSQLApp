from flask import Flask, render_template
from message import Message
import load_html
from time import sleep


app = Flask(__name__)
message = Message()


@app.route('/')
@app.route('/index')
def index():
    users = [ 'Rosalia','Adrianna','Victorias' ]
    return render_template('index.html', title='Welcome', members=users)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
