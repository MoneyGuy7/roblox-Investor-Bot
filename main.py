import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your staff role ID
STAFF_ROLE_ID = 123456789012345678  

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def need_investor(ctx, project_name: str, amount: int, *, description: str):
    """Create a ticket for people needing investors"""
    thread = await ctx.channel.create_thread(
        name=f"Investor Ticket: {project_name}",
        type=discord.ChannelType.public_thread,
        auto_archive_duration=60
    )
    await thread.send(
        f"**Project:** {project_name}\n"
        f"**Points Needed:** {amount}\n"
        f"**Description:** {description}\n\n"
        f"Staff can join to help manage this ticket."
    )
    await thread.send(f"<@&{STAFF_ROLE_ID}> A new investor ticket has been created.")
    await ctx.send(f"Your investor ticket has been created: {thread.mention}", ephemeral=True)

@bot.command()
async def offer_investor(ctx, investor_name: str, *, description: str):
    """Create a ticket for people who want to invest"""
    thread = await ctx.channel.create_thread(
        name=f"Investor Offer: {investor_name}",
        type=discord.ChannelType.public_thread,
        auto_archive_duration=60
    )
    await thread.send(
        f"**Investor:** {investor_name}\n"
        f"**Info:** {description}\n\n"
        f"Staff can join to manage this offer."
    )
    await thread.send(f"<@&{STAFF_ROLE_ID}> A new investor offer ticket has been created.")
    await ctx.send(f"Your investor offer ticket has been created: {thread.mention}", ephemeral=True)

bot.run(os.environ["DISCORD_TOKEN"])
