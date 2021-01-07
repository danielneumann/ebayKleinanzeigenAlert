## Motivation - Stop spending hours on real estate platforms!
@todo describe

# PropertyAlert - (propAlert)
Small python module that provides basic functionality to register observation links and inform on new entries.
No API required - Only URL of the query.

Right now, it supports:

* ebay Kleinanzeigen: https://www.ebay-kleinanzeigen.de/
* Immo Scout24: https://www.immobilienscout24.de/
* immonet: https://www.immonet.de/

## Install
* Download folder or clone
* cd yourself to the main directory
* Hard code your telegram API key and messageID in the telegramclass.py file.
* Install or run straight from directory.
  * install with ````pip install .  ````
  * run with ````python -m propAlert ````

## Usage & Example
* ```propAlert links [opts] ``` to show, add, remove links
* ```propAlert start``` to start receiving notification


* ```postAlert links add "https://www.ebay...k0l9354r20"``` Assuming you just look through the web page while copy no notification will be send. 
* Typically run as a cron job on an hourly basis.

## Requirements
* A telegram bot API token and your personal conversation id
* Python 3
* click, requests, bs4 and sqlalchemy (arguably sqlalchemy is a little overkill for that purpose)

## Create a bot

Use BotFather and follow this tutorial: https://core.telegram.org/bots#creating-a-new-bot

## Obtain chat ID

# 1- Add the bot to the group.
Go to the group, click on group name, click on Add members, in the searchbox search for your bot like this: @my_bot, select your bot and click add.

# 2- Send a dummy message to the bot.
You can use this example: /my_id @my_bot
(I tried a few messages, not all the messages work. The example above works fine. Maybe the message should start with /)

# 3- Go to following url: https://api.telegram.org/botXXX:YYYY/getUpdates
replace XXX:YYYY with your bot token

# 4- Look for "chat":
{"id":-zzzzzzzzzz, -zzzzzzzzzz is your chat id (with the negative sign).

# 5- Testing: You can test sending a message to the group with a curl:

curl -X POST "https://api.telegram.org/botXXX:YYYY/sendMessage" -d "chat_id=-zzzzzzzzzz&text=my sample text"

## Executing it regularly

## Credits
Thanks to
* @vinc3PO for providing the initial code
* @melloskitten for providing codebase for 