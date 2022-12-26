from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
 
from .scraper import Center, Gate, Profile
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
stage = 0
gate = ("0", "1", "2", "3", "4-answer", "5-pattern", "6", "7-role-of-the-self-in-interaction", "8", "9-detail-focus", 
"10", "11", "12", "13", "14", "15-extremes", "16-skills", "17-opinions", "18-correction", "19", 
"20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
"30", "31-democracy", "32", "33", "34", "35", "36", "37", "38", "39", 
"40", "41", "42", "43", "44", "45", "46", "47", "48-depth", "49", 
"50", "51", "52-stillness", "53", "54", "55", "56", "57", "58-joy-of-life", "59-sexuality", 
"60-acceptance", "61-mystery", "62-details", "63-doubt", "64-confusion")
@csrf_exempt
def callback(request):
    global stage
    global gate
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if(stage == 0):
                    if(event.message.text == "gate"):
                        stage = 1
                        line_bot_api.reply_message(  #
                        event.reply_token,
                        TextSendMessage(text="type gate number to know its meaning\n\nEX: 10\n\n" + 
                        "type \'help\' to see how to do\n\n" +
                        "type \'back\' to go to select mode")
                        )
                    elif(event.message.text == "center"):
                        stage = 2
                        line_bot_api.reply_message(  #
                        event.reply_token,
                        TextSendMessage(text="type center name to know its meaning\n\nEX: head\n\n" + 
                        "type \'help\' to see how to do\n\n" +
                        "type \'back\' to go to select mode\ntype in lowercase")
                        )
                    elif(event.message.text == "profile"):
                        stage = 3
                        line_bot_api.reply_message(  #
                        event.reply_token,
                        TextSendMessage(text="type profile number to know its meaning\n\nEX: 1-4\n\n" + 
                        "type \'help\' to see how to do\n\n" +
                        "type \'back\' to go to select mode")
                        )
                    elif(event.message.text == "help"):
                        line_bot_api.reply_message(  #
                        event.reply_token,
                        TextSendMessage(text="type \'gate\' to go to gate-explaination mode\n" +
                        "type \'center\' to go to center-explaination mode\n" +
                        "type \'profile\' to go to profile-explaination mode\n")
                        )
                    else:
                        line_bot_api.reply_message(  #
                        event.reply_token,
                        TextSendMessage(text="type \'gate\' to go to gate-explaination mode\n" +
                        "type \'center\' to go to center-explaination mode\n" +
                        "type \'profile\' to go to profile-explaination mode\n")
                        )

                elif(stage == 1):
                    try:
                        num = int(event.message.text)
                    except:
                        if(event.message.text == "back"):
                            stage = 0
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type \'gate\' to go to gate-explaination mode\n" +
                            "type \'center\' to go to center-explaination mode\n" +
                            "type \'profile\' to go to profile-explaination mode\n")
                            )
                            break
                        elif(event.message.text == "help"):
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type in the number between 1 to 64")
                            )
                        else:
                            line_bot_api.reply_message(  #
                                event.reply_token,
                                TextSendMessage(text="type gate number to know its meaning\n\nEX: 10\n\n" + 
                                "type \'help\' to see how to do\n\n" +
                                "type \'back\' to go to select mode")
                            )
                            break
                    explaination = Gate(gate[num])
                    
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=explaination.scrape())
                    )
                elif(stage == 2):
                    try:
                        num = int(event.message.text)
                    except:
                        if(event.message.text == "back"):
                            stage = 0
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type \'gate\' to go to gate-explaination mode\n" +
                            "type \'center\' to go to center-explaination mode\n" +
                            "type \'profile\' to go to profile-explaination mode\n")
                            )
                            break
                        elif(event.message.text == "help"):
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type in \'head\' \'ajna\' \'throat\' \'g\' \n\'ego\' \'sacral\' \'spleen\' \'root\'")
                            )
                        '''else:
                            line_bot_api.reply_message(  #
                                event.reply_token,
                                TextSendMessage(text="type center name to know its meaning\nEX: head\n" + 
                        "type \'back\' to go to select mode\ntype in lowercase")
                            )
                            break'''
                    explaination = Center(event.message.text)
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=explaination.scrape())
                    )
                elif(stage == 3):
                    try:
                        num = int(event.message.text)
                    except:
                        if(event.message.text == "back"):
                            stage = 0
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type \'gate\' to go to gate-explaination mode\n" +
                            "type \'center\' to go to center-explaination mode\n" +
                            "type \'profile\' to go to profile-explaination mode\n")
                            )
                            break
                        elif(event.message.text == "help"):
                            line_bot_api.reply_message(  #
                            event.reply_token,
                            TextSendMessage(text="type in \'1-3\' \'1-4\' \'2-4\' \'2-5\' \n\'3-5\' \'3-6\' \'4-6\' \'4-1\'\n" +
                            "\'5-1\' \'5-2\' \'6-2\' \'6-3\'")
                            )
                        '''else:
                            line_bot_api.reply_message(  #
                                event.reply_token,
                                TextSendMessage(text="type center name to know its meaning\nEX: head\n" + 
                        "type \'back\' to go to select mode\ntype in lowercase")
                            )
                            break'''
                    explaination = Profile(event.message.text)
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=explaination.scrape())
                    )
                print(event.message)
            
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

