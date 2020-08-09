def add_total_page(single_message):
    page = """
    <html>
      <head>
        <style>
        .message_text_top {
            width: 90%;
        }
        .message_text_center {
            width: 90%;
            background-color: #21a6f6;
            padding-right: 10px;
            padding-left: 10px;
            padding-bottom: 2px;
            padding-top: 2px;
            border-radius: 25px;
        }
        .author {
            font-size: 15px;
            position: relative;
            top: 34px;
            right: -20px;
        }
        .time {
            font-size: 15px;
            position: relative;
            top: 8px;
            left: -20px;
            text-align: right;
        }
        </style>
      </head>
      <body>
      """ + single_message + """
      </body>
    <html>
    """
    return page

def add_data_to_message(num, content, author, time):
    message_template = f"""
    <div>
      <div class='message_text_top'>
        <h1 class='author'>{author}</h1>
        <h1 class='time'>{time}</h1>
      </div>
      <div class='message_text_center'>
        <h1 class='content'>{content}</h1>
      </div>
    </div>
    """
    return message_template
