from flask import Flask
from message import Message


app = Flask(__name__)
message = Message()

def add_data_to_message():
message_template = """
<div class='message_text'>
    <h1></h1>
</div>
"""

@app.route('/')
def get_messages():
    page = ""
    messages = message.get()
    for x in messages:
        page += f"<h1>{x}</h1>"
    return page



if __name__ == '__main__':
   app.run()
