#First piece:

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '8',
    }],
}   



#Second piece:

@bot.command(desc="Please use links, doesn't support search.")
async def play(ctx, url: str):
    if not ctx.message.author.voice:
        await ctx.send('you are not connected to a voice channel')
        return
    else:
        try:
            channel = ctx.message.author.voice.channel
        except:
            await ctx.send(f'Connected to {ctx.message.author.voice.channel.name} and looking for the song!')
    voice_client = await channel.connect()
    await ctx.send("Loading the audio now!")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        for prop in ['title']:
            await ctx.send(f'Now playing "{file.get(prop)}"')
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")
        voice_client.play(discord.FFmpegPCMAudio(path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

#Required imports:
#import discord, youtube_dl
#import discord.ext import commands