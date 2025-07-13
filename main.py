import discord
from discord.ext import commands

TOKEN = 'MTM5MzU2MzkzNTI2MDY3MjA0MA.G8ge0o.Ij95W21NS77hUERXMHpJlM7Wxk2lgY9Lwxsu8g'
ADMIN_ID = 911075179445235722 #1317771149727371317  # Your Discord user ID (right-click your profile -> Copy ID)

intents = discord.Intents.default()
intents.members = True  # Enable member events
intents.message_content = True  # If your bot reads messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Get the admin user
    admin = await bot.fetch_user(ADMIN_ID)
    
    # Send a DM notification
    await admin.send(f'🚨 New member joined: {member.name} ({member.id}) in {member.guild.name}')
    print(f'Sent notification about {member.name}')

bot.run(TOKEN)