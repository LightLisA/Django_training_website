import requests
from .models import TelegramSettings


def sendTelegram(tg_name, tg_phone):
    if TelegramSettings.objects.get(pk=1):
        settings = TelegramSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat_id)
        text = str(settings.tg_message)

        api = 'https://api.telegram.org/bot'
        method = f"{api}{token}/sendMessage"

        # шукаємо номер і імя щоб підставити їх в смс бота
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise = text
        try:
            request = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise
            })
        except:
            pass
        finally:
            if request.status_code != 200:
                print('Sending Error - checking back-end')
            elif request.status_code == 500

