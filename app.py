from flask import Flask
from message import Message
import load_html


app = Flask(__name__)
message = Message()


@app.route('/')
def get_messages():
    page = ""
    messages = message.get()
    for x in messages:
        page += load_html.add_data_to_message(*x)
    full_page = load_html.add_total_page(page)
    return full_page


if __name__ == '__main__':
    app.run()
