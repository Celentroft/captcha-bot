import discord
from discord.ext import commands
from discord import app_commands
from functions import load_json, embed_color

class Settings(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="settings", description="Voir la configuration actuelle du bot")
    async def settings(self, interaction: discord.Interaction) -> None:
        config = load_json()
        if interaction.user.id != config['buyer']:
            return await interaction.response.send_message("Vous n'ètes pas autorisé à utiliser cette commande.", ephemeral=True)
        embed = discord.Embed(
            title="`🧪`・Settings actuels",
            description=f"> `🪡`・**Couleur des embeds:** {config['color']}\n> `👑`・**Owner du bot:** <@{config['buyer']}>\n> `⭐`・**Role verifié:** <@&{config['role']}>",
            color=embed_color()
        )
        return await interaction.response.send_message(embed=embed)
    
async def setup(bot) -> None:
    await bot.add_cog(Settings(bot))