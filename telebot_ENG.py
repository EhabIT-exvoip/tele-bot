import asyncio
import datetime
import telebot

bot = telebot.TeleBot('')
# keep track of the last group message time
response =  """ 
Hello, I'm ExVoip's Telegram bot.
We work from Sunday to Thursday, from 08:00 to 17:00.
At the moment we are not in the office and we do not have access to the servers, we can only help tomorrow morning from 08:00.
Have a good evening.
"""

weekendreply = """
Hello, I'm ExVoip's Telegram bot.
We work from Sunday to Thursday, from 08:00 to 17:00.
We are currently not in the office and do not have access to the servers, we can only help on Sunday morning from 08:00.
Have a nice weekend.
"""

@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply_to_group_message(message):
    dt = datetime.datetime.now()
    currenttime = dt.time()
    current_weekday = dt.strftime('%A')
    days = ["Sunday", "Monday" , "Tuesday", "Wednesday", "Thursday"]
    weekend = ["Friday", "Saturday"]
    workhours = (currenttime > datetime.time(hour=4,minute=55) and currenttime < datetime.time(hour=14,minute=5))
    thursdayworkhours = (currenttime > datetime.time(hour=14,minute=5))
    if ( current_weekday in days and workhours):
        return
    elif ( current_weekday == "Thursday" and thursdayworkhours):
        bot.reply_to(message, weekendreply)
        return
    elif ( current_weekday in weekend):
        bot.reply_to(message, weekendreply)
        return
    else:
        bot.reply_to(message, response)

async def main():
    asyncio.create_task(bot.polling(none_stop=True))

asyncio.run(main())