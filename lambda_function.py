import os
import requests
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#API keys
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
STORMGLASS_API_KEY = os.environ['STORMGLASS_API_KEY']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']

    #set the latitude and longitude for Rockaway Beach
    latitude = 40.5834
    longitude = -73.8227
    
    logger.info(event)
    if '/conditions' in message['text']:
        #pull the current chat ID
        chat_id = message['chat']['id']

        #obtain and format weather data 
        response = requests.get(f'https://api.stormglass.io/v2/weather/point?lat={latitude}&lng={longitude}&params=waterTemperature,waveHeight', headers={'Authorization': STORMGLASS_API_KEY}).json()
        water_temperature = response['hours'][0]['waterTemperature']['sg']
        wave_height_feet = response['hours'][0]['waveHeight']['sg'] * 3.28084
        
        #format and send telegram message
        telegram_message = f'Water temperature in Rockaway Beach is currently {water_temperature}°C and the waves are {wave_height_feet:.2f} feet high. Happy surfing 🤙🏽'
        telegram_response = requests.post(f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage', json={'chat_id': chat_id, 'text': telegram_message})
        
        # Log the Telegram API response
        logger.info(f'Telegram API response: {telegram_response.text}')
        
    return {
        'statusCode': 200
    }