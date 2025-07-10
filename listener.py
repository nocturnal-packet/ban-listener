# listener.py
import discord, os

TOKEN      = os.getenv("DISCORD_TOKEN")
APPEAL_URL = "https://appeal.gg/byPMrtxES3"   #  ← change this!

intents = discord.Intents.none()
intents.guilds = True
intents.bans   = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"ban-listener live as {bot.user}")

@bot.event
async def on_member_ban(guild, user):
    try:
        await user.send(
            f"You were banned from **{guild.name}**.\n"
            f"Appeal here ➜ {APPEAL_URL}"
        )
    except discord.Forbidden:
        pass               # DMs closed or bot blocked

#    async for entry in guild.audit_logs(action=discord.AuditLogAction.ban, limit=1):
#        if entry.target.id == user.id and APPEAL_URL not in (entry.reason or ""):
#            new_reason = f"{entry.reason or 'No reason'} • Appeal: {APPEAL_URL}"
#            await entry.edit(reason=new_reason)

bot.run(TOKEN)
