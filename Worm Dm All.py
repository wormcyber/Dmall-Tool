import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Connected As: {bot.user}')

@bot.command(name="dmall", description="DMs every single member.")
async def dmall(ctx, *, message: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You do not have the required permissions to use this command!")
        return

    successful = 0
    failed = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            successful += 1
        except discord.Forbidden:
            failed += 1

    print(f"DM sent to {successful} members. Failed to DM {failed} members due to their privacy settings.")

sexytoken = 'Your Sexy Token Here'


bot.run(sexytoken)
