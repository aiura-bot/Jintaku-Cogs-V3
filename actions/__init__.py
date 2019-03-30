from .actions import Actions


def setup(bot):
    n = Actions()
    bot.add_cog(n)
