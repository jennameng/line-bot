from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dvicnpmTQ5/U9RyORL8JaAUDJJyxko2zgQexPT6JdHesWEc5dHAHPECO0O1oaE5E3ymZvot09xSo1BDwxLG+1CmAmBjAv53Fit191lN4nDsK5cUQpyAXOf3HC+/qE0QCaOT57VgzbPlIADbnbKrspwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3c0031cb6d981c072d7fd1b8de79fe18')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()