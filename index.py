from http.server import BaseHTTPRequestHandler
import json
import telebot

# التوكن الخاص بك
TOKEN = "7275178891:AAFTCA9Wd5-5LUnOBonUi51NE4glDe5pRH8"
bot = telebot.TeleBot(TOKEN)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            # استقبال الرسالة من تلغرام
            json_string = post_data.decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
        except Exception as e:
            print(e)

        # الرد على تلغرام بأن كل شيء على ما يرام
        self.send_response(200)
        self.end_headers()
        return

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Bot is active on Vercel!".encode('utf-8'))
