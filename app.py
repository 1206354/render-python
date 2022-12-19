
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
import os
import main
import config
app = Flask(__name__)

#環境変数取得
line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)    # config.pyで設定したチャネルアクセストークン
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)    # config.pyで設定したチャネルシークレット
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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        #TextSendMessage(text=event.message.text))
        TextSendMessage(text=("return = "+main.test())))
if __name__ == "__main__":
#   app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
