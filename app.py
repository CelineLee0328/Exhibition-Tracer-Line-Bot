from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import configparser
from kktix import *
from tixcraft import *
from ibon import *
from news import *

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

access_token = config.get('line-bot', 'channel_access_token')
channel_secret = config.get('line-bot', 'channel_secret')
line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'
#----------------Template title字數限制處理--------------------
def title_length(title):
    if len(title) > 40:
        return title[0:39]
    else:
        return title
#-------------------------------------------------------------

@handler.add(MessageEvent)
def handle_message(event):      
    try:
        type = event.message.type
        if type == 'location':
            address_list = []
            address_number = event.message.address
            # address_number = LocationSendMessage(
            # title = '已傳送下列地址',
            # address = event.message.address,
            # latitude = event.message.latitude,
            # longitude = event.message.longitude
            # )
            address_list.append(address_number)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(address_number))
        if type == 'text':
            message = event.message.text   
            if message == '售票系統查詢':
                template_message = TemplateSendMessage(
                alt_text='Carousel Template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://img.onl/H91Dus',
                            title='KKTIX',
                            text='KKTIX - 活動售票報名，精彩從此開始',
                            actions=[
                                URIAction(
                                    label='進入KKTIX',
                                    uri='https://kktix.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://img.onl/OSgZBj',
                            title='tixCraft',
                            text='tixCraft拓元售票系統',
                            actions=[
                                URIAction(
                                    label='進入tixCraft',
                                    uri='https://tixcraft.com/'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://img.onl/400mpM',
                            title='ibon',
                            text='ibon售票系統',
                            actions=[
                                URIAction(
                                    label='進入ibon',
                                    uri='https://ticket.ibon.com.tw/Index/entertainment'
                                )
                            ]
                        )
                    ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, template_message)
            if message == '最新消息查詢':
                quick_message = TextSendMessage(text='選擇售票系統',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="KKTIX", text="kktix")),
                                    QuickReplyButton(action=MessageAction(label="拓元", text="tixcraft")),
                                    QuickReplyButton(action=MessageAction(label="ibon", text="ibon"))
                                ]))
                line_bot_api.reply_message(event.reply_token, quick_message)
            if message == 'kktix':
                results = kktix_crawler()
                template_message = TemplateSendMessage(
                alt_text='Carousel Template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=results[0]['image'],
                            title=title_length(results[0]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[0]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[1]['image'],
                            title=title_length(results[1]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[1]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[2]['image'],
                            title=title_length(results[2]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[2]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[3]['image'],
                            title=title_length(results[3]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[3]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[4]['image'],
                            title=title_length(results[4]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[4]['href']
                                )
                            ]
                        )
                    ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, template_message) 
            if message == 'tixcraft':
                results = tixcraft_crawler()
                template_message = TemplateSendMessage(
                alt_text='Carousel Template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=results[0]['image'],
                            title=title_length(results[0]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[0]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[1]['image'],
                            title=title_length(results[1]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[1]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[2]['image'],
                            title=title_length(results[2]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[2]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[3]['image'],
                            title=title_length(results[3]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[3]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[4]['image'],
                            title=title_length(results[4]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[4]['href']
                                )
                            ]
                        )
                    ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, template_message) 
            if message == 'ibon':
                results = ibon_crawler()
                template_message = TemplateSendMessage(
                alt_text='Carousel Template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=results[0]['image'],
                            title=title_length(results[0]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[0]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[1]['image'],
                            title=title_length(results[1]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[1]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[2]['image'],
                            title=title_length(results[2]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[2]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[3]['image'],
                            title=title_length(results[3]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[3]['href']
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=results[4]['image'],
                            title=title_length(results[4]['title']),
                            text="點擊查看進入展演頁面",
                            actions=[
                                URIAction(
                                    label='查看',
                                    uri=results[4]['href']
                                )
                            ]
                        )
                    ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, template_message) 
            if message == '新聞搜尋':
                results = news_crawler()
                line_bot_api.reply_message(event.reply_token,  TextSendMessage(text=results))      
            else:  
                reply = '尚未開發"'+ message + '"相關功能，敬請期待'
                line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))
        
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='尚未開發相關功能，敬請期待'))
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    app.run()

