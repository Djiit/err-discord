# coding: utf-8
from errbot.backends.test import testbot

import discord


class TestPandascorePlugin(object):
    extra_plugin_dir = '.'

    def test_discord_invite(self, testbot):
        testbot.push_message('!discord')
        assert (f'Invite me to your Discord server: https://discordapp.com/oauth2/authorize?client_id=your_client_id_here&scope=bot&permissions={discord.DISCORD_PERMISSIONS}'
                in testbot.pop_message())
