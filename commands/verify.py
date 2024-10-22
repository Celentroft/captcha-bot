import discord
from discord import app_commands
from discord.ext import commands
from functions import load_json, embed_color
from views.startVerify import startVerify

class VerifyCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @app_commands.command(name='verify-embed', description="Envoyer l'embed de verification")
    async def verify_embed(self, interaction: discord.Interaction) -> None:
        config = load_json()
        if interaction.user.id != config['buyer']:
            return await interaction.response.send_message("Vous n'ètes pas autorisé à utiliser cette commande.", ephemeral=True)

        embed = discord.Embed(
            title="`🛡️`・Verification",
            description=f"""
*Pour obtenir l'acces au serveur **{interaction.guild.name}**. Merci de bien vouloir completer la verification ci dessous.*
            """,
            color=embed_color()
        )
        view = discord.ui.View(timeout=None)
        view.add_item(startVerify(self.bot))
        await interaction.response.send_message(embed=embed, view=view)
        
async def setup(bot) -> None:
    await bot.add_cog(VerifyCommand(bot))