import os
import telebot
import yt_dlp

# O GitHub vai injetar o Token aqui através das Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    boas_vindas = (
        "Olá! Eu sou o seu **Assistente de Downloads** 🤖✨\n\n"
        "Sou especializado no download de **vídeos curtos** das redes:\n\n"
        "📱 **Instagram** (Reels e Vídeos)\n"
        "🎬 **TikTok**\n\n"
        "Sempre busco a **melhor qualidade disponível** que caiba no limite do Telegram!"
    )
    bot.reply_to(message, boas_vindas, parse_mode='Markdown')

def download_video(url):
    out_file = f"video_{os.urandom(4).hex()}.mp4"
    
    ydl_opts = {
        'format': 'best[ext=mp4]/best', 
        'outtmpl': out_file,
        'max_filesize': 50 * 1024 * 1024,
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'add_header': [
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language: en-us,en;q=0.5',
            'Sec-Fetch-Mode: navigate',
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return out_file
    except Exception as e:
        print(f"Erro detalhado no yt-dlp: {e}")
        return None

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    
    if "tiktok.com" in url or "instagram.com" in url:
        msg = bot.reply_to(message, "⚡ **Analisando e baixando...**", parse_mode='Markdown')
        
        try:
            filename = download_video(url)
            
            if filename and os.path.exists(filename):
                final_size = os.path.getsize(filename) / (1024 * 1024)
                
                if final_size <= 50:
                    with open(filename, 'rb') as video:
                        bot.send_video(message.chat.id, video, timeout=120)
                    bot.delete_message(message.chat.id, msg.message_id)
                else:
                    bot.edit_message_text("❌ O vídeo excede o limite de 50MB do Telegram.", message.chat.id, msg.message_id)
                
                if os.path.exists(filename):
                    os.remove(filename)
            else:
                bot.edit_message_text("❌ Não foi possível obter este vídeo. Verifique se o link é público.", message.chat.id, msg.message_id)
                
        except Exception as e:
            bot.edit_message_text(f"⚠️ Erro inesperado: {str(e)[:50]}", message.chat.id, msg.message_id)
    
    elif "http" in url:
        bot.reply_to(message, "Sou especializado exclusivamente em **TikTok** e **Instagram**. 📲", parse_mode='Markdown')

print("Bot iniciado no GitHub Actions...")
bot.infinity_polling()
