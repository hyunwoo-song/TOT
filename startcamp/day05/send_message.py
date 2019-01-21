import os
import requests


token = os.getenv('TELEGRAM_BOT_TOKEN') 
chat_id = os.getenv('CHAT_ID') 
text = '하위'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

