# listener.py
import discord, os

TOKEN      = os.getenv("DISCORD_TOKEN")              # set in Railway Variables
APPEAL_URL = "https://appeal.gg/byPMrtxES3"          # <-- your live form URL

# ─── Intents ───────────────────────────────────────────────────────────────
intents = discord.Intents.none()
intents.guilds = True      # so we know which guild fired the event
intents.bans   = True      # delivers on_member_ban gateway events

bot = discord.Client(intents=intents)

# ─── Bot online ────────────────────────────────────────────────────────────
@bot.event
async def on_ready():
    print(f"[ban-listener] live as {bot.user}")       # shows up in Railway logs

# ─── Ban handler ───────────────────────────────────────────────────────────
@bot.event
async def on_member_ban(guild, user):
    # 1) prove the event fired
    print(f"[ban-listener] Ban event → {user} in {guild.name}")

    # 2) try to DM the appeal link
    try:
        await user.send(
            f"You were banned from **{guild.name}**.\n"
            f"Appeal here ➜ {APPEAL_URL}"
        )
        print(f"[ban-listener] DM sent to {user}")    # success path
    except discord.Forbidden:
        print(f"[ban-listener] DM FAILED for {user} (DMs closed or bot blocked)")

# ─── Run ───────────────────────────────────────────────────────────────────
bot.run(TOKEN)
