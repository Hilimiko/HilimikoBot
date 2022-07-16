import pkgutil
import disnake

from disnake.ext import commands


class Application(commands.InteractionBot):
    def __init__(self):
        super().__init__(
            Intents=disnake.Intents.all(),
            help_command=None
        )

    def load_cog(self, path: str):
        for file in pkgutil.iter_modules({path}):
            try:
                self.load_extension(f"cogs.{file.name}")
                print("cog {file.name} successfully loaded")
            except Exception as e:
                print(e)