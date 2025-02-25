from traceback import print_exception

from discord import Embed, Interaction
from discord.ui import Modal, TextInput

class SendNoticeModal(Modal):
    carrier_name = TextInput(
        label='Carrier Name',
        placeholder='Name of the fleet carrier',
        required=True,
        max_length=64,
    )
    carrier_id = TextInput(
        label='Carrier ID',
        placeholder='A1B-C23',
        required=True,
        max_length=7,
    )
    wine_tonnes = TextInput(
        label='Wine Total (tons)',
        placeholder='22000',
        required=True,
        max_length=5,
    )

    def __init__(self, title="Wine Carrier Owner Signup", timeout=None):

        self.carrier_name.default = ""  # Clear modal from previous usages
        self.carrier_id.default = ""  # Clear modal from previous usages
        self.wine_tonnes.default = ""  # Clear modal from previous usages
        super().__init__(title=title, timeout=timeout)

    async def on_submit(self, interaction: Interaction):
        ...
        # TODO: verify data, insert to DB, reply to user

    async def on_error(self, interaction: Interaction, error: Exception) -> None:
        await interaction.response.send_message(f'Oops! Something went wrong: {error}', ephemeral=True)
        print_exception(type(error), error, error.__traceback__)