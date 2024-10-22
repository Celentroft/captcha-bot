import discord
from discord import app_commands
from discord.ext import commands
from functions import embed_color

class HelpCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="help", description="Montrer l'embed d'aide")
    async def helpcommand(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="`🛠️`・Panel d'aide",
            color=embed_color()
        )
        embed.add_field(name="`/verify-embed`", value="*Envoyer l'embed de verification du serveur*", inline=False)
        embed.add_field(name="`/config-role`", value="*Configurer le role ajouté après la verification*", inline=False)
        embed.add_field(name="`/settings`", value="*Afficher la configuration totale du bot*", inline=False)

        await interaction.response.send_message(embed=embed)
        
async def setup(bot) -> None:
    await bot.add_cog(HelpCommand(bot))