import os
import requests
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
STORMGLASS_API_KEY = os.environ['STORMGLASS_API_KEY']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']
    
    logger.info(event)
    if '/conditions' in message['text']:
        chat_id = message['chat']['id']
        response = requests.get(f'https://api.stormglass.io/v2/weather/point?lat=40.5834&lng=-73.8227&params=waterTemperature,waveHeight', headers={'Authorization': STORMGLASS_API_KEY}).json()
        water_temperature = response['hours'][0]['waterTemperature']['sg']
        wave_height_feet = response['hours'][0]['waveHeight']['sg'] * 3.28084
        telegram_message = f'Water temperature in Rockaway Beach is currently {water_temperature}°C and the waves are {wave_height_feet:.2f} feet high. Happy surfing 🤙🏽'
        telegram_response = requests.post(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage', json={'chat_id': chat_id, 'text': telegram_message})
        
        # Log the Telegram API response
        logger.info(f'Telegram API response: {telegram_response.text}')
        
    return {
        'statusCode': 200
    }