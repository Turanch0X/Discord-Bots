import discord,asyncio,tracemalloc
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content= True
intents.voice_states = True

Djin = discord.Client(intents=intents)
HALLMORE = ['Quite_like_you','Dreams_Beyond','It_is_her','Piece_of_me','Cybernetics','Reignite','Saharas']
CLASSIC = ['Welcome','As the Jurassic World turns','Suite','Rey','Ark','Victory','Jurassic']
TOGETHER = list(HALLMORE+CLASSIC)
path = 0
audio = 0

def is_valid_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@Djin.event
async def on_ready():
    print(f'{Djin.user} has logged in!')

tracemalloc.start()
@Djin.event
async def on_message(message):

    async def check(m):
        return m.author == message.author and m.channel == message.channel
    
    voice_channel = message.author.voice.channel

    if not message.author.bot and voice_channel:      
        voice_client = message.guild.voice_client
        if voice_client is None:
            voice_client = await voice_channel.connect()
            print('Bot is connected.')

        async def music():
            audio = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(path))
            audio.volume = 0.2
            voice_client.play(audio)

            while voice_client.is_playing():
                await asyncio.sleep(1)
    
        if message.content.startswith('!'):
            
            for song in TOGETHER:
                if message.content.find(song)==1:
                    path = f'music\{song}.mp3'
                    audio = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(path))

                    await message.channel.send('Choose the volume (0.1-1.0). You have 30 seconds to think.')
                    volume = 0.2
                    try:
                        reply = await Djin.wait_for('message', check=check, timeout=30.0)
                        volume = float(reply.content)
                    except asyncio.TimeoutError:
                        audio.volume = 0.2
                    
                    audio.volume = volume
                    voice_client.play(audio)

            if 'hallmore' in message.content:
                for song in HALLMORE:
                    path = f'music\HALLMORE\{song}.mp3'
                    await music()
                await voice_client.disconnect()

            if 'classic' in message.content:
                for song in CLASSIC:
                    path = f'music\CLASSIC\{song}.mp3'
                    await music()
                await voice_client.disconnect()

            if 'stop' in message.content:
                if voice_client.is_playing():
                    voice_client.stop()
                await voice_client.disconnect()

tracemalloc.stop()
Djin.run('MTEzMTg5NTA2NTYyNzg2OTIxNA.GwWww_.Eo8mmdObxTYV3B_Zdy4kL3jxA1XsPVKfi0wpHI')