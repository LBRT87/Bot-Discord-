import discord
import random
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Buat client bot
client = discord.Client(intents=intents)

COINMARKETCAP_API_KEY = '5d331b45-f705-4d62-8f8a-734bfdd64637'

def get_crypto_price ( symbol ) :
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': symbol.upper(),  # convert ke kapital karena CoinMarketCap minta kapital
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    response = requests.get(url, headers=headers, params=parameters)
    
    # Error handling, kalau symbol gak ditemukan
    if response.status_code != 200:
        return None

    data = response.json()
    try:
        price = data['data'][symbol.upper()]['quote']['USD']['price']
        return round(price, 2)
    except KeyError:
        return None
    
@client.event 
async def on_message (message) : 
    if message.author == client.user : 
        return
    
    # Data 
    greet_words = [
        'hi','hello','hey', 'whatsup','howdy']
    gift_words = [ 'gift']
    sad_words = [
        "sad", 
        "depressed",
        "angry",
        "hurting",
        "stressed"]
    gift_link = [       
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjVvemF1N3N3OWxmaHNlc2xuMHBvaHp5dzk1bXNwZGJqdW1pZDAzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1vSI0fDGF1jleBrabn/giphy.gif",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm1qOWhyN2RweTlzZzVnZDBpZDczd3lldm5sbWh5cnc0bWR4eWg4cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KPDZ55SvovQv6/giphy.gif",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnZncXV0ajZqZGtmNmh5ejR2cXB5bW02ZHczaHhkMXNzdjlrOGd5bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5k5vZwRFZR5aZeniqb/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDNybnp0cDVnbjlqd2QybmR6czA0ajhxN3lqMHRpMW1lNjNiYmc0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hxTPSekZ76kSacFHMb/giphy.gif",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExczI2anh6cjV2b2txMWFxMmkwcWE5eGdsdXBkODFpcGZ4d2w4ZG80cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wBELrJgO6ZtII/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmlvajNhbzF3bjVvM20zcGJkbDl0cWVlaHB3Z2h4eWVha2g5Nzl1bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3vRlT2k2L35Cnn5C/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTVpZGpvZ2M2NTYwNmltank5czRvdDZnMHprNG5mOGNwMmtsY3cwNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/14qb1Uhf40ndw4/giphy.gif",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Q1Y2RrdjUxNnBoaHcwYXZxbjIyZG5uMWFyanNoOXJqNXU0NTB6YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AoTzzu7XUJCwM/giphy.gif",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGpzYnduNWNmZWF1NnhndDF0MTZ1bGptZ255dXRneXowejQ4NnQycCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yiUg3Rhit3FcY/giphy.gif",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExczd6eTY4anZ0NzBtamd5bjJ5czExN3pwdGFoNWVsaDZ2NHlxN2tvcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HAd0YHRvQf6Gk/giphy.gif",
    ]
    encourage_words = [
    "Cheer up! 🤗",
    "Hang in there 😉",
    "You are a great person!👍 ",
    "Come on! You can do it! 💪",
    "Stay strong 🥰 "
    ]
    happy_words = [
        'happy',
        'glad',
        'joyful',
        'satistied',
        'blessed',
    ]
    response_happy = [
        "There you go! 👏",
        "Keep up the good work 👍",
        "Keep it up 🙌",
        "Good job 👍",
        "I’m so proud of you!🥰" 
    ]
    playlist_youtube = [
    "https://youtu.be/k4V3Mo61fJM?si=GgsS1mbNnkKiwffP" , 
    "https://youtu.be/IBTmypxD2mU?si=Iy6MODX605r5ZALi" ,
    "https://youtu.be/NQLvnin2bxs?si=ogxXUvadLm0L6E-Y" ,
    "https://youtu.be/QSWYyoF79oE?si=ONwGPQID3HCrYK-Z" ,
    "https://youtu.be/LLDM_j7Nv6I?si=JiMm6Q3qx1MZ4U8e" ,
    ]
    song_words = [
        'song',
        'music',
        'melody',
        'tune',
        'track',
        'playlist',
    ]
    message.content = message.content.lower()
    print ( message.content )

    if any ( word in message.content for word in greet_words ) : 
        await message.channel.send ( 'Yoooww , Hiii 😍 !!')
    elif any ( word in message.content for word in gift_words ) : 
         gift = random.choice(gift_link)
         await message.channel.send (gift)
    elif any(word in message.content for word in sad_words ) : 
        response1 = random.choice(encourage_words)
        await message.channel.send ( response1 )
    elif any(word in message.content for word in happy_words ) : 
        response2 = random.choice(response_happy)
        await message.channel.send ( response2 )
    elif any ( word in message.content for word in song_words ) :
        await message.channel.send (random.choice(playlist_youtube))
    elif message.content.startswith('$'):
        symbol = message.content[1:]  # hapus $ dari depan
        price = get_crypto_price(symbol)
        if price:
            await message.channel.send(f'Harga {symbol.upper()} saat ini: ${price}')
        else:
            await message.channel.send(f'Sorry, coin {symbol.upper()} tidak ditemukan atau ada error!')
@client.event
async def on_ready() : 
    print ( "we have logged in as {0.user}".format(client))

TOKEN = os.getenv('DISCORD_TOKEN')
client.run (TOKEN)


