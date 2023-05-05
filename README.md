# Telegram Surf Bot
Telegram bot which tells users the surf conditions in Rockaway beach, NY. The nyc_surf_bot usings stormglass.io to fetch weather data. Commands are received from the Telegram webhook, and responses posted via the API. See it in action below: 

## Set up your own bot

### 1. Create Telegram bot

If you don't have a [Telegram](https://telegram.org/) account yet, you'll need to download the app and sign up. Once you're good to go, message @BotFather with the command `/newbot`. The BotFather will take you through the steps of creating your bot, and will return the HTTP API key you'll need to communicate with the bot. 

### 2. Sign up for Stormglass.io

You can sign up for a free weather API key at [Stormglass.io](https://stormglass.io/). The free tier allows you 10 API calls per day.

### 3. Update the code. 

I surf most often in Rockaway beach, but you should change the location to the beach you surf at. Update lat/long to do so: 

```
#set the latitude and longitude for Rockaway Beach
latitude = 40.5834
longitude = -73.8227
```
### 4. Package and Deploy the Code

There are a variety of options you can choose to deploy the code. I used a Lambda serverless set up with API Gateway. To deploy to Lambda, you'll want to install requests and associated libraries into the directory you're currently in by running ` pip3 install requests -t .`. Once you've done this, you can zip the directory by running `zip -r9 lambda-deployment-package.zip .`. 

In Lambda, create a new function and upload your code. Set the trigger to API Gateway and great a new API. 

### 5. Set up Telegram Bot Webhook 

In order for Telegram to communicate with your backend, you'll want to set the webhook destination. Use the following code to set your webhook in your favorite browser. 

`https://api.telegram.org/bot{your Telegram bot token}/setWebhook?url={API Gateway URL}&drop_pending_updates=true`

Drop pending updates sets the pending updates to 0. This is helpful in case you're testing and have errors, which Telegram will continue to try to process. Setting it to true resets the webhook. 

You should see the following once you've done this correctly: 

`{"ok":true,"result":true,"description":"Webhook was set"}`

You can also check if the endpoint URL is correct by running: 

`https://api.telegram.org/bot{your Telegram bot token}/getWebhookInfo`

### 6. Starting your bot and adding it to a channel

Go to your bot's DM's and type /start to start it.

**Do not add the bot as a member from your group; for some reason this doesn't work!** You will need to go to your bot, clikc the elipsis in the top right, and click "Info". From there, click "Add to Group or Channel". 

#### Done! Now, whenever you type `/conditions` in the group, you'll receive the surf conditions! 
