from os import environ

from errbot import BotPlugin, botcmd, arg_botcmd, webhook
from bottle import redirect


CONFIG_TEMPLATE = {'DISCORD_CLIENT_ID': environ.get('DISCORD_CLIENT_ID', 'your_client_id_here')}
DISCORD_PERMISSIONS = 523328

class Discord(BotPlugin):
    """
    Discord utilities for Errbot
    """

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports
        """
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super().configure(config)
        return

    @webhook('/discord/invite')
    def invite(self, incoming_request):
        """
        A webhook which simply returns a Discord invitation link.
        """
        return redirect(f"https://discordapp.com/oauth2/authorize?client_id={self.config['DISCORD_CLIENT_ID']}&scope=bot&permissions={DISCORD_PERMISSIONS}")

    @botcmd
    def discord(self, message, args):
        """
        Display a Discord invitation link.
        """
        return f"Invite me to your Discord server: https://discordapp.com/oauth2/authorize?client_id={self.config['DISCORD_CLIENT_ID']}&scope=bot&permissions={DISCORD_PERMISSIONS}"
