# tele-bot

The Bot is installed on uptimekuma server (termius) 
http://34.249.146.208/ server - connect from termius.

---
Activate the systemctl process:

Create a new file:
sudo nano /etc/systemd/system/processName.service

On this file:
""
[Unit]
Description=My test service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/ubuntu/telegram-bot/pyTelegramBotAPI/exvoip-bot.py

[Install]
WantedBy=multi-user.target
""

After that:

systemctl start exvoip-bot.service  (The name of the file)



In case of issue with telegram exvoip bots (HE/ENG):

1. systemctl status exvoip-bot.service - see if active
2. systemctl stop exvoip-bot.service - stop the bot 
3. edit the file - at folder - /home/ubuntu/telegram-bot/pyTelegramBotAPI/exvoip-tele.py
4. systemctl start exvoip-bot.service - start the bot