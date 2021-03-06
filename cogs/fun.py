import random
import requests
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # get a random kaomoji bear
    # Usage: >>kaomoji_bear
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kaomoji_bear(self, ctx):
        kaomoji_bears = ["ʕ •ᴥ•ʔ", "ᶘ ᵒᴥᵒᶅ", "ᶘ ⊙ᴥ⊙ᶅ", "ᶘ °㉨°ᶅ", "ᶘಠᴥಠᶅ", "ʕ •́؈•̀)", "ʕ´ڡ｀*ʔ", "ʕ – _ – ʔ", "ʕ – o – ʔ", "（´•(ｪ)•｀）", "ʕ≧(ｴ)≦ ʔ",
                        "ʕ •㉨• ʔ", "ʕó㉨òʔﾉ♡", "ᶘ ᵒ㉨ᵒᶅ", "ʕ´•㉨•`ʔ", "ʕ≧㉨≦ʔ", "ʕ✪㉨✪ʔ", "ʕ ̿–㉨ ̿– ʔ", "ʕ/　·ᴥ·ʔ/", "ʕ； •`ᴥ•´ʔ", "ʕ ˵• ₒ •˵ ʔ",
                        "ʕ •ᴥ•ʔゝ☆", "ᕕʕ •ₒ• ʔ୨", "ʕ　·ᴥʔ", "ʕ·ᴥ·　ʔ", "ʕᴥ·　ʔ", "ʕ •ᴥ•ʔ", "ʕง•ᴥ•ʔง"]
        await ctx.send(" " + random.choice(kaomoji_bears))

    # get a random positive kaomoji
    # Usage: >>kaomoji_positive
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kaomoji_positive(self, ctx):
        positive_kaomojis = ["(* ^ ω ^)", "(´ ∀ ` *)", "(o･ω･o)", "(*≧ω≦*)", "ヽ(*・ω・)ﾉ", "(*꒦ິ꒳꒦ີ)", "☆*:.｡.o(≧▽≦)o.｡.:*☆", "٩(｡•́‿•̀｡)۶", "(˙꒳​˙)",
                         "(๑˃ᴗ˂)ﻭ", "(´･ᴗ･ ` )", "( ‾́ ◡ ‾́ )", "(´ ε ` )♡", "(❤ω❤)", "(„ಡωಡ„)", "(つ≧▽≦)つ", "(つ✧ω✧)つ", "(づ￣ ³￣)づ", "(^_<)〜☆",
                         "( ͡° ͜ʖ ͡°)", "ଘ(੭ˊ꒳​ˋ)੭✧", "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)", "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ", "ヾ(・ω・)メ(・ω・)ノ"]
        await ctx.send(" " + random.choice(positive_kaomojis))

    # get a random negative kaomoji
    # Usage: >>kaomoji_negative
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kaomoji_negative(self, ctx):
        negative_kaomojis = ["(ﾉಥ益ಥ)ﾉ", "(・`ω´・)", "(ﾒ` ﾛ ´)", "ヽ( `д´*)ノ", "୧((#Φ益Φ#))୨", "(凸ಠ益ಠ)凸", "凸( ` ﾛ ´ )凸", "凸(`△´＃)",
                            "(╯︵╰,)", "(╥﹏╥)", "(｡•́︿•̀｡)", "(ಥ﹏ಥ)", "。゜゜(´Ｏ`) ゜゜。", "〜(＞＜)〜", "(ﾒ￣▽￣)︻┳═一", "( ͡° ʖ̯ ͡°)",
                            "( ͠° ͟ʖ ͡°)", "( ͡ಠ ʖ̯ ͡ಠ)", "( ಠ ʖ̯ ಠ)", "(;´༎ຶٹ༎ຶ`)", "(ʘ ʖ̯ ʘ)", "(╯°Д°)╯︵ /(.□ . ＼)", "(ಠ o ಠ)¤=[]:::::>"]
        await ctx.send(" " + random.choice(negative_kaomojis))

    # get a random neutral kaomoji
    # Usage: >>kaomoji_neutral
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kaomoji_neutral(self, ctx):
        neutral_kaomojis = ["٩(ˊ〇ˋ*)و", "(￣^￣)ゞ", "(　･ω･)☞", "(￣﹃￣)", "┬┴┬┴┤(･_├┬┴┬┴", "(シ_ _)シ", "(＾་།＾)", "ε===(っ≧ω≦)っ",
                           "(^◕ᴥ◕^)", "∪･ｪ･∪", "(∪｡∪)｡｡｡zzZ", "(－ω－) zzZ", "(＿ ＿*) Z z z"]
        await ctx.send(" " + random.choice(neutral_kaomojis))

    # get a random cute pic of a cat
    # Usage: >>cat
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(self, ctx):
        url = 'https://some-random-api.ml/img/cat'
        result_url = requests.get(url)
        resultjson=result_url.json()
        embed=discord.Embed(title="here is cat", description="cat",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text="*pet me*")
        await ctx.send(embed=embed)

    # get a random cute pic of a dog
    # Usage: >>dog
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dog(self, ctx):
        url = 'https://some-random-api.ml/img/dog'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed=discord.Embed(title="here is doggo", description="a good boy or girl",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='awww')
        await ctx.send(embed=embed)

    # get a random cute pic of a panda
    # Usage: >>panda
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def panda(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/panda'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='epic panda!', description="panpan",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='cute')
        await ctx.send(embed=embed)

    # get a random cute pic of a redpanda
    # Usage: >>redpanda
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def redpanda(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/red_panda'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='its a panda! but red!', description="red panpan",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='such red')
        await ctx.send(embed=embed)
    
    # get a random cute pic of a birb
    # Usage: >>birb
    @commands.command(aliases=['bird'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def birb(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/birb'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='ebic birb', description="BIRB!",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='borb')
        await ctx.send(embed=embed)

    # get a random cute pic of a fox
    # Usage: >>fox
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fox(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/fox'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='foxes r cute', description="owo fox",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='sly 100')
        await ctx.send(embed=embed)

    # get a random cute pic of a koala
    # Usage: >>koala
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def koala(self, ctx):
        await ctx.trigger_typing()
        url = 'https://some-random-api.ml/img/koala'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed = discord.Embed(title='drop bear!', description="koala",
        colour=discord.Colour.green())
        embed.set_image(url=resultjson['link'])
        embed.set_footer(text='slep')
        await ctx.send(embed=embed)

    # get a random picture of a meme
    # Usage: >>meme
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def meme(self, ctx):
        url = 'https://some-random-api.ml/meme'
        result_url = requests.get(url)
        resultjson = result_url.json()
        embed=discord.Embed(title=resultjson['caption'], description="meme",
        colour=discord.Colour.purple())
        embed.set_image(url=resultjson['image'])
        embed.set_footer(text=f"Category: {resultjson[ 'category']}")
        await ctx.send(embed=embed)
                         
    # Char count
    # Usage: >>char (sentence/word)
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def char(self, ctx, *, args=None):

        if args == None:
            await ctx.send("**Dummy what am I supposed to jumble?**")

        elif args != None:
            argument_length = len(args)
            embed = discord.Embed(title=None, description=f"There are **{argument_length}** letters in **{args}**", color=discord.Colour.dark_purple())
            await ctx.send(embed=embed)

    # LMGTFY (Let Me Google That For You)
    # Usage: >>google (query)
    @commands.command(aliases=['lmgtfy'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def google(self, ctx, *, args):
        if not ' ' in args:
            return await ctx.send(f'<http://lmgtfy.com/?q={args}&pp=1>')
        await ctx.send(f"<http://lmgtfy.com/?q={args.replace(' ', '+')}&pp=1>")

    # Clap
    # Usage: >>clap/sassify/sass (sentence/word)
    # If single arg, returns: a :clap: r :clap: g :clap: s :clap:
    # If multiple args, returns: These :clap: are :clap: multiple :clap: words :clap: 
    @commands.command(aliases=['sassify', 'sass'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clap(self, ctx, *, args):
        if not ' ' in args:
            charList = [char for char in args]
            sendText = ' '.join(map(str, charList))
            return await ctx.send(sendText.replace(' ', ' :clap: '))
        await ctx.send(args.replace(' ', ' :clap: '))

    # Gaymeter
    # Usage: >>howgay/gaymeter [member]
    @commands.command(aliases=['howgay'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gaymeter(self, ctx, member : discord.Member=None):
        if not member: 
            embed = discord.Embed(description=f'{ctx.author.name}, you are {random.randint(0,101)}% gay\n:rainbow_flag:')
            await ctx.send(embed=embed)

        else: 
            embed = discord.Embed(description=f'{member.name} is {random.randint(0,101)}% gay\n:rainbow_flag:')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
