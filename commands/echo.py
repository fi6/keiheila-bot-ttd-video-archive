import json
from khl import Cert, Bot
import codecs

# load config from config/config.json,
# replace `path` points to your own config file.
#
# config template: `./config/config.json.example`
# rename it into 'config.json' and filling fields
with open('./configs/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# init Cert for Bot OAuth and data decrypt
# pass `verify_token` to `Cert()` to get a webhook cert
# besides you can pass `type=Cert.Types.WH` explicitly to get a webhook cert
# meanwhile `type=Cert.Types.WS` will gain a websocket cert
cert = Cert(client_id=config['client_id'],
            client_secret=config['client_secret'],
            token=config['token'])

# init Bot
# set params `compress`, `port`, `route` corresponding to your webhook
# callback url.
# use compress=enabled, port=5000, route='/khl-wh' in default
# i.e:
#              callback url                 |       constructor call
#     http://your.domain:5000/khl-wh        |        Bot(cert=cert)
# http://your.domain:5000/khl-wh?compress=0 | Bot(cert=cert, compress=False)
#        http://your.domain:2333            |    Bot(cert=cert, port=2333)
#      http://your.domain:5000/meow         | Bot(cert=cert, route='/meow')
bot = Bot(cmd_prefix=['.', '。'], cert=cert)


# add command, accept optional arguments
# you can invoke this command via:
#   `.echo test`
@bot.command(name='echo')
async def func(session):
    content = codecs.decode(session.msg.content[6:], 'unicode_escape')
    await session.send(content)
    return None

# everything done, go ahead now!
bot.run()
