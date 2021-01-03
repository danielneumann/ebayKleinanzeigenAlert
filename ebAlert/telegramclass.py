import requests
try:
    from ebAlert.credential import TOKEN, CHAT_ID
except ImportError:
    TOKEN = "1422553734:AAGrwmugY_GIabMRfojCZGR7y9_GW2_Xwb8"
    CHAT_ID = "1323685085"

def sendMessage(message):
    send_text = """https://api.telegram.org/bot{}/sendMessage?chat_id={}
    &parse_mode=Markdown&text={}""".format(TOKEN,
                                           CHAT_ID,
                                           message)
    response = requests.get(send_text)
    return response.json()['ok']
