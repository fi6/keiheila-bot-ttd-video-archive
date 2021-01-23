import json
from khl import Cert
from khl.bot_preview import Bot

with open('./configs/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

cert = Cert(client_id=config['client_id'],
            client_secret=config['client_secret'],
            token=config['token'])

bot = Bot(cmd_prefix=['.', '。'], cert=cert)

bot.add_command()

bot.run()
