from lib.cog import Cog, event
from lib.command import Command, command


class Demo(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @command(aliases=["demo"], description="")
    def test(self, c: Command):
        self.sendmsg("This is a remote module")
