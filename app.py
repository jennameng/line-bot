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
    msg = event.message.text
    r = '不好意思。你在說什麼?'
    if msg in ['hi', 'Hi', "HI"]:
        r = '哈囉你好~'
    elif msg = '你吃飽了嗎?':
        r = '還沒'
    elif msg = '你是誰?':
        r = '我是機器人' 
    elif '訂位' in msg:
        r = '你要訂位嗎?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()