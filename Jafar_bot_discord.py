import discord,random

intents = discord.Intents.default()
intents.message_content = True

main = 1127170468072411148
clips = 1127170468072411149  #id каналов

SAD = ['kitty','mdems','monkey','nechto','sad']
HAP = ['turtle','gendlf','jafarchick','kefka','linivec','minions','obama','lampa']
PORN = ['jas','djin','maximus','move','muha','newyear','patrik','salut','snow']
GAMES = ['govno','trees','dusha']
gifki = list(SAD+HAP+PORN+GAMES)

Jafar = discord.Client(intents=intents)

@Jafar.event
async def on_ready():
    print(f'{Jafar.user} has logged in')

@Jafar.event
async def on_message(message):
    mes = message.content.lower()
    sad_meme = random.choice(SAD)
    happy_meme = random.choice(HAP)
    porno_meme = random.choice(PORN)
    game_meme = random.choice(GAMES)
    file = ''
    if message.author != Jafar.user:
        for gif in gifki:
            if mes.find(gif)==1:
                with open (f'gifki/{gif}.gif','rb') as gifka:
                    file = discord.File(gifka)
            elif 'sad' in mes:
                with open (f'gifki\{sad_meme}.gif','rb') as gifka:
                    file = discord.File(gifka)
            elif 'happy' in mes:
                with open (f'gifki\{happy_meme}.gif','rb') as gifka:
                    file = discord.File(gifka)
            elif 'porn' in mes:
                with open (f'gifki\{porno_meme}.gif','rb') as gifka:
                    file = discord.File(gifka)
            elif 'games' in mes:
                with open (f'gifki\{game_meme}.gif','rb') as gifka:
                    file = discord.File(gifka)
        if mes.startswith('/') and file!='':
            await Jafar.get_channel(clips).send(file=file)
            await message.add_reaction('👍🏽')

Jafar.run('MTEyODI3NDA2ODM2MjI0ODIwMg.G6jqJv.tnGNye1_UI1Tg4FEgCOyoubYkQd9po5g1Rb4tg')