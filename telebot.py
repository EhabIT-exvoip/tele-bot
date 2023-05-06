import asyncio
import datetime
import telebot

bot = telebot.TeleBot('')
# keep track of the last group message time
response =  """ שלום אני הבוט של טלגרם.
אנחנו עובדים ביום ראשון עד חמישי משעה 17:00-8:00.
כרגע אנחנו לא במשרד ואין לנו גישה לשרתים אז נוכל לעזור מחר רק בבוקר בשעה 8:00.
ערב טוב  """

@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply_to_group_message(message):
    dt = datetime.datetime.now()
    currenttime = dt.time()
    current_weekday = dt.strftime('%A')
    days = ["Sunday", "Monday" , "Tuesday", "Wednesday", "Thursday" ]
    print("day is : " + current_weekday)
    # current_time < datetime.time(hour=4,minute=50)
    workhours = (currenttime > datetime.time(hour=7,minute=50) and currenttime < datetime.time(hour=17,minute=1))
    #print (workhours)
    if ( current_weekday in days and workhours):
        print("working")
        return
    else:
        print("not working")
        bot.reply_to(message, response)

async def main():
    asyncio.create_task(bot.polling(none_stop=True))

asyncio.run(main())