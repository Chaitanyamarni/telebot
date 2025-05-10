import telebot
import requests
import time

TOKEN = "7667534222:AAGX2T1S2Iym2eWwQwHoL_Qaos32awW5aW0"
bot = telebot.TeleBot(TOKEN)

PLAYER_INFO_URL = "https://zoroinfo-one.vercel.app/api/player-info?id={uid}"
BAN_INFO_URL = "https://zoroban.vercel.app/karna/ban-info?uid={uid}"
LIKES_API = "https://zorolikes.vercel.app/like?uid={uid}&server_name=ind"
SPAM_API = "https://zorospam.vercel.app/send_requests?uid={uid}&region=ind&key=zoro"

@bot.message_handler(commands=["info"])
def player_info(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "⚠️ Usage: /info <UID>", parse_mode="Markdown")
            return

        uid = parts[1]
        bot.reply_to(message, f"⏳ Fetching player info for {uid}...", parse_mode="Markdown")
        response = requests.get(PLAYER_INFO_URL.format(uid=uid), headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        if data.get("status") != "success":
            bot.reply_to(message, f"❌ Player Info Error: {data.get('message', 'Unknown error')}", parse_mode="Markdown")
            return

        player = data["data"]["basic_info"]
        guild = data["data"].get("Guild", {})
        pet = data["data"].get("animal", {})

        text = (
            f"🎮 *Player Info*\n"
            f"🏷 *Name:* `{player.get('name', 'N/A')}`\n"
            f"🆔 *UID:* `{player.get('id', 'N/A')}`\n"
            f"⭐️ *Level:* `{player.get('level', 'N/A')}`\n"
            f"❤️ *Likes:* `{player.get('likes', 'N/A')}`\n"
            f"🌍 *Server:* `{player.get('server', 'N/A')}`\n"
            f"📝 *Bio:* `{player.get('bio', 'N/A')}`\n"
            f"🎫 *Booyah Pass Level:* `{player.get('booyah_pass_level', 'N/A')}`\n"
            f"📅 *Account Created:* `{player.get('account_created', 'N/A')}`\n\n"
            f"👥 *Guild Info*\n"
            f"🏰 *Guild Name:* `{guild.get('name', 'N/A')}`\n"
            f"🔢 *Guild Level:* `{guild.get('level', 'N/A')}`\n"
            f"👥 *Members:* `{guild.get('members_count', 'N/A')}`\n"
            f"👑 *Guild Leader:* `{guild.get('leader', {}).get('name', 'N/A')}`\n\n"
            f"🐾 *Pet Info*\n"
            f"🐕 *Pet Name:* `{pet.get('name', 'N/A')}`\n\n"
            f"⚡️ *Credits:* ZORO"
        )
        bot.reply_to(message, text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=["ban"])
def ban_info(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "⚠️ Usage: /ban <UID>", parse_mode="Markdown")
            return

        uid = parts[1]
        bot.reply_to(message, f"⏳ Checking ban status for {uid}...", parse_mode="Markdown")
        response = requests.get(BAN_INFO_URL.format(uid=uid), headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        text = (
            f"🚫 *Ban Info*\n"
            f"🏷 *Name:* `{data.get('nickname', 'N/A')}`\n"
            f"🌍 *Region:* `{data.get('region', 'N/A')}`\n"
            f"❗️ *Ban Status:* `{data.get('ban_status', 'N/A')}`\n"
            f"⏳ *Ban Period:* `{data.get('ban_period', 'None')}`\n\n"
            f"⚡️ *Credits:* ZORO"
        )
        bot.reply_to(message, text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=["likes"])
def send_likes(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "⚠️ Usage: /likes <UID>", parse_mode="Markdown")
            return

        uid = parts[1]
        bot.reply_to(message, f"⏳ Sending likes to UID: {uid}...", parse_mode="Markdown")
        response = requests.get(LIKES_API.format(uid=uid))
        data = response.json()

        text = (
            f"❤️ *Like Info*\n"
            f"🏷 *Name:* `{data.get('PlayerNickname', 'N/A')}`\n"
            f"🆔 *UID:* `{data.get('UID', 'N/A')}`\n"
            f"👍 *Before:* `{data.get('LikesbeforeCommand', 'N/A')}`\n"
            f"➕ *Given by API:* `{data.get('LikesGivenByAPI', 'N/A')}`\n"
            f"✅ *After:* `{data.get('LikesafterCommand', 'N/A')}`\n\n"
            f"⚡️ *Credits:* ZORO"
        )
        bot.reply_to(message, text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}", parse_mode="Markdown")


@bot.message_handler(commands=["spam"])
def spam_requests(message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "⚠️ Usage: /spam <UID>", parse_mode="Markdown")
            return

        uid = parts[1]
        bot.reply_to(message, f"⏳ Sending spam requests to UID: {uid}...", parse_mode="Markdown")
        response = requests.get(SPAM_API.format(uid=uid))
        data = response.json()

        text = (
            f"🗯 *Spam Info*\n"
            f"🆔 *UID:* `{uid}`\n"
            f"✅ *Success:* `{data.get('success_count', 0)}`\n"
            f"❌ *Failed:* `{data.get('failed_count', 0)}`\n\n"
            f"⚡️ *Credits:* ZORO"
        )
        bot.reply_to(message, text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}", parse_mode="Markdown")


def start_bot():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Bot crashed: {e}")
            time.sleep(5)

# Start the bot
start_bot()
