import json
import discord
from discord import app_commands
from discord.ext import commands
from functions import load_json, embed_color

class configRole(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name="config-role", description="Configurer le role ajouter apres la verification")
    async def config_role(self, interaction: discord.Interaction, role: discord.Role) -> None:
        config = load_json()
        if interaction.user.id != config['buyer']:
            return await interaction.response.send_message("Vous n'ètes pas autorisé à utiliser cette commande.", ephemeral=True)
        
        config['role'] = role.id
        json.dump(config, open('config.json', 'w'), indent=4)
        embed = discord.Embed(
            title="`⭐`・Role Configuré",
            description=f"*Le rôle {role.mention} à bien été configurer comme le role ajouté dès que la verification est validée.*",
            color=embed_color()
        )
        await interaction.response.send_message(embed=embed)
        
async def setup(bot) -> None:
    await bot.add_cog(configRole(bot))