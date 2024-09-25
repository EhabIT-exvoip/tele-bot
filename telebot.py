import asyncio
import datetime
import telebot

bot = telebot.TeleBot('')
# keep track of the last group message time
response =  """ 
שלום, אני הבוט טלגרם של ExVoip.
אנחנו עובדים בימי ראשון עד חמישי, משעה 08:00 עד 17:00.
כרגע אנחנו לא במשרד ואין לנו גישה לשרתים, נוכל לעזור רק מחר בבוקר משעה 08:00.
ערב טוב
"""

weekendreply = """
שלום, אני הבוט טלגרם של ExVoip.
אנחנו עובדים בימי ראשון עד חמישי, משעה 08:00 עד 17:00.
כרגע אנחנו לא במשרד ואין לנו גישה לשרתים, נוכל לעזור רק ביום ראשון בבוקר משעה 08:00.
סופ"ש נעים
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